import random

from Sensors_pb2_grpc import SensorsServicer, SensorsStub
from Sensors_pb2 import SensorRequest, SensorType, SensorRequestStreamed
import grpc
from google.protobuf.json_format import MessageToJson
from time import sleep

channel = grpc.insecure_channel('localhost:15000')
stub = SensorsStub(channel)

def simple():
    print(stub.getMeasure(SensorRequest(reqId=1, sensorType=SensorType.CPU)))
    print(stub.getMeasure(SensorRequest(reqId=2, sensorType=SensorType.DISK)))

def server_stream():
    for result in stub.getMeasuresStream(SensorRequestStreamed(sensorType=SensorType.CPU)):
        print(result)

def client_stream():
    requests = [SensorRequest(reqId=1, sensorType=SensorType.CPU),
                SensorRequest(reqId=2, sensorType=SensorType.VIRTUAL_MEMORY),
                SensorRequest(reqId=3, sensorType=SensorType.CPU),
                SensorRequest(reqId=4, sensorType=SensorType.DISK),
                ]

    print(stub.getSensorResponseList(iter(requests)))

def bidirectional_stream():
    def requests(n, t):
        for i in range(n):
            choice = random.choice([SensorType.CPU, SensorType.VIRTUAL_MEMORY])
            yield SensorRequest(reqId=i, sensorType=choice)
            sleep(random.randint(1, t))

    for response in stub.getBidirectional(requests(10, 4)): print(response)

# simple()
# server_stream()
# client_stream()
bidirectional_stream()