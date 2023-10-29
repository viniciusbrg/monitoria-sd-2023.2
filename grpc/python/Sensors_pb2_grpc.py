# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Sensors_pb2 as Sensors__pb2


class SensorsStub(object):
    """(Method definitions not shown)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getMeasure = channel.unary_unary(
                '/Sensors/getMeasure',
                request_serializer=Sensors__pb2.SensorRequest.SerializeToString,
                response_deserializer=Sensors__pb2.SensorResponse.FromString,
                )
        self.getMeasuresStream = channel.unary_stream(
                '/Sensors/getMeasuresStream',
                request_serializer=Sensors__pb2.SensorRequestStreamed.SerializeToString,
                response_deserializer=Sensors__pb2.SensorResponse.FromString,
                )
        self.getSensorResponseList = channel.stream_unary(
                '/Sensors/getSensorResponseList',
                request_serializer=Sensors__pb2.SensorRequest.SerializeToString,
                response_deserializer=Sensors__pb2.SensorResponseList.FromString,
                )
        self.getBidirectional = channel.stream_stream(
                '/Sensors/getBidirectional',
                request_serializer=Sensors__pb2.SensorRequest.SerializeToString,
                response_deserializer=Sensors__pb2.SensorResponse.FromString,
                )


class SensorsServicer(object):
    """(Method definitions not shown)
    """

    def getMeasure(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMeasuresStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getSensorResponseList(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBidirectional(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SensorsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getMeasure': grpc.unary_unary_rpc_method_handler(
                    servicer.getMeasure,
                    request_deserializer=Sensors__pb2.SensorRequest.FromString,
                    response_serializer=Sensors__pb2.SensorResponse.SerializeToString,
            ),
            'getMeasuresStream': grpc.unary_stream_rpc_method_handler(
                    servicer.getMeasuresStream,
                    request_deserializer=Sensors__pb2.SensorRequestStreamed.FromString,
                    response_serializer=Sensors__pb2.SensorResponse.SerializeToString,
            ),
            'getSensorResponseList': grpc.stream_unary_rpc_method_handler(
                    servicer.getSensorResponseList,
                    request_deserializer=Sensors__pb2.SensorRequest.FromString,
                    response_serializer=Sensors__pb2.SensorResponseList.SerializeToString,
            ),
            'getBidirectional': grpc.stream_stream_rpc_method_handler(
                    servicer.getBidirectional,
                    request_deserializer=Sensors__pb2.SensorRequest.FromString,
                    response_serializer=Sensors__pb2.SensorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Sensors', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Sensors(object):
    """(Method definitions not shown)
    """

    @staticmethod
    def getMeasure(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Sensors/getMeasure',
            Sensors__pb2.SensorRequest.SerializeToString,
            Sensors__pb2.SensorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMeasuresStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Sensors/getMeasuresStream',
            Sensors__pb2.SensorRequestStreamed.SerializeToString,
            Sensors__pb2.SensorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getSensorResponseList(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Sensors/getSensorResponseList',
            Sensors__pb2.SensorRequest.SerializeToString,
            Sensors__pb2.SensorResponseList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBidirectional(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Sensors/getBidirectional',
            Sensors__pb2.SensorRequest.SerializeToString,
            Sensors__pb2.SensorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
