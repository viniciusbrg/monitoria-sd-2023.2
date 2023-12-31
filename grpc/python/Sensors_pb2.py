# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Sensors.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rSensors.proto\"?\n\rSensorRequest\x12\r\n\x05reqId\x18\x01 \x01(\x05\x12\x1f\n\nsensorType\x18\x02 \x01(\x0e\x32\x0b.SensorType\"R\n\x0eSensorResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x1f\n\nsensorType\x18\x03 \x01(\x0e\x32\x0b.SensorType\"G\n\x15SensorRequestStreamed\x12\r\n\x05\x63\x61lls\x18\x01 \x01(\x05\x12\x1f\n\nsensorType\x18\x02 \x01(\x0e\x32\x0b.SensorType\"7\n\x12SensorResponseList\x12!\n\x08response\x18\x01 \x03(\x0b\x32\x0f.SensorResponse*D\n\nSensorType\x12\x07\n\x03\x43PU\x10\x00\x12\x12\n\x0eVIRTUAL_MEMORY\x10\x01\x12\x0f\n\x0bSWAP_MEMORY\x10\x02\x12\x08\n\x04\x44ISK\x10\x03\x32\xf9\x01\n\x07Sensors\x12/\n\ngetMeasure\x12\x0e.SensorRequest\x1a\x0f.SensorResponse\"\x00\x12@\n\x11getMeasuresStream\x12\x16.SensorRequestStreamed\x1a\x0f.SensorResponse\"\x00\x30\x01\x12@\n\x15getSensorResponseList\x12\x0e.SensorRequest\x1a\x13.SensorResponseList\"\x00(\x01\x12\x39\n\x10getBidirectional\x12\x0e.SensorRequest\x1a\x0f.SensorResponse\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Sensors_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SENSORTYPE']._serialized_start=296
  _globals['_SENSORTYPE']._serialized_end=364
  _globals['_SENSORREQUEST']._serialized_start=17
  _globals['_SENSORREQUEST']._serialized_end=80
  _globals['_SENSORRESPONSE']._serialized_start=82
  _globals['_SENSORRESPONSE']._serialized_end=164
  _globals['_SENSORREQUESTSTREAMED']._serialized_start=166
  _globals['_SENSORREQUESTSTREAMED']._serialized_end=237
  _globals['_SENSORRESPONSELIST']._serialized_start=239
  _globals['_SENSORRESPONSELIST']._serialized_end=294
  _globals['_SENSORS']._serialized_start=367
  _globals['_SENSORS']._serialized_end=616
# @@protoc_insertion_point(module_scope)
