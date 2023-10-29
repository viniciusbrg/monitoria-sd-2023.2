import psutil
from concurrent import futures
import grpc
from datetime import datetime

# Servicer is the 'base' for our services, we'll provide the implementation for the RPC methods overriding this.
from Sensors_pb2_grpc import SensorsServicer, add_SensorsServicer_to_server

from Sensors_pb2 import SensorType, SensorResponse, SensorResponseList

def get_timestamp(): return str(datetime.now())
def get_cpu(): return str(psutil.cpu_percent(2))
def getUsedMemory(): return str(psutil.virtual_memory().percent)
def getUsedSwap(): return str(psutil.swap_memory().percent)
def getUsedDisk(): return str(psutil.disk_usage('/').percent)

sensors_dict = {
    SensorType.CPU: get_cpu,
    SensorType.VIRTUAL_MEMORY: getUsedMemory,
    SensorType.SWAP_MEMORY: getUsedSwap,
    SensorType.DISK: getUsedDisk
}

class SensorsServicerImpl(SensorsServicer):
    def getMeasure(self, request, context):
        print("got request")
        print(request)
        sensor_type = request.sensorType
        measure = sensors_dict[sensor_type]()

        return SensorResponse(timestamp=get_timestamp(), data=measure, sensorType=sensor_type)

    def getMeasuresStream(self, request, context):
        print("got request")
        print(request)
        sensor_type = request.sensorType
        n = request.calls
        for i in range(n):
            yield SensorResponse(timestamp=get_timestamp(), data=sensors_dict[sensor_type](), sensorType=sensor_type)

    def getSensorResponseList(self, request_iterator, context):
        # iterate over requests, produce final result
        responses = []
        for request in request_iterator:
            print("got request")
            print(request)
            sensor_type = request.sensorType
            response = SensorResponse(timestamp=get_timestamp(), data=sensors_dict[sensor_type](), sensorType=sensor_type)
            responses.append(response)
        return SensorResponseList(response=responses)


    def getBidirectional(self, request_iterator, context):
        # iterate over requests, produce results while iterating
        for request in request_iterator:
            print("got request")
            print(request)
            sensor_type = request.sensorType
            yield SensorResponse(timestamp=get_timestamp(), data=sensors_dict[sensor_type](), sensorType=sensor_type)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
add_SensorsServicer_to_server(SensorsServicerImpl(), server)
server.add_insecure_port("[::]:15000")
server.start()
server.wait_for_termination()
