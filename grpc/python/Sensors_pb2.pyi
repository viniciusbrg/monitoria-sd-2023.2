from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SensorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CPU: _ClassVar[SensorType]
    VIRTUAL_MEMORY: _ClassVar[SensorType]
    SWAP_MEMORY: _ClassVar[SensorType]
    DISK: _ClassVar[SensorType]
CPU: SensorType
VIRTUAL_MEMORY: SensorType
SWAP_MEMORY: SensorType
DISK: SensorType

class SensorRequest(_message.Message):
    __slots__ = ["reqId", "sensorType"]
    REQID_FIELD_NUMBER: _ClassVar[int]
    SENSORTYPE_FIELD_NUMBER: _ClassVar[int]
    reqId: int
    sensorType: SensorType
    def __init__(self, reqId: _Optional[int] = ..., sensorType: _Optional[_Union[SensorType, str]] = ...) -> None: ...

class SensorResponse(_message.Message):
    __slots__ = ["timestamp", "data", "sensorType"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SENSORTYPE_FIELD_NUMBER: _ClassVar[int]
    timestamp: str
    data: str
    sensorType: SensorType
    def __init__(self, timestamp: _Optional[str] = ..., data: _Optional[str] = ..., sensorType: _Optional[_Union[SensorType, str]] = ...) -> None: ...

class SensorRequestStreamed(_message.Message):
    __slots__ = ["calls", "sensorType"]
    CALLS_FIELD_NUMBER: _ClassVar[int]
    SENSORTYPE_FIELD_NUMBER: _ClassVar[int]
    calls: int
    sensorType: SensorType
    def __init__(self, calls: _Optional[int] = ..., sensorType: _Optional[_Union[SensorType, str]] = ...) -> None: ...

class SensorResponseList(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _containers.RepeatedCompositeFieldContainer[SensorResponse]
    def __init__(self, response: _Optional[_Iterable[_Union[SensorResponse, _Mapping]]] = ...) -> None: ...
