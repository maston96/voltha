# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voltha.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import health_pb2 as health__pb2
import logical_layer_pb2 as logical__layer__pb2
import adapter_pb2 as adapter__pb2
import example_service_pb2 as example__service__pb2

from common_pb2 import *
from health_pb2 import *
from logical_layer_pb2 import *
from adapter_pb2 import *
from example_service_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='voltha.proto',
  package='voltha',
  syntax='proto3',
  serialized_pb=_b('\n\x0cvoltha.proto\x12\x06voltha\x1a\x0c\x63ommon.proto\x1a\x0chealth.proto\x1a\x13logical_layer.proto\x1a\radapter.proto\x1a\x15\x65xample_service.protoB<\n\x13org.opencord.volthaB\x0cVolthaProtos\xaa\x02\x16Opencord.Voltha.VolthaP\x00P\x01P\x02P\x03P\x04\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,health__pb2.DESCRIPTOR,logical__layer__pb2.DESCRIPTOR,adapter__pb2.DESCRIPTOR,example__service__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023org.opencord.volthaB\014VolthaProtos\252\002\026Opencord.Voltha.Voltha'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)