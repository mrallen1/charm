# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/hex_pb_names.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/hex_pb_names.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x18proto/hex_pb_names.proto\"#\n\x05Names\x12\x1a\n\x08packages\x18\x01 \x03(\x0b\x32\x08.Package\"*\n\x07Package\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_NAMES = _descriptor.Descriptor(
  name='Names',
  full_name='Names',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packages', full_name='Names.packages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=63,
)


_PACKAGE = _descriptor.Descriptor(
  name='Package',
  full_name='Package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Package.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='Package.namespace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=107,
)

_NAMES.fields_by_name['packages'].message_type = _PACKAGE
DESCRIPTOR.message_types_by_name['Names'] = _NAMES
DESCRIPTOR.message_types_by_name['Package'] = _PACKAGE

Names = _reflection.GeneratedProtocolMessageType('Names', (_message.Message,), dict(
  DESCRIPTOR = _NAMES,
  __module__ = 'proto.hex_pb_names_pb2'
  # @@protoc_insertion_point(class_scope:Names)
  ))
_sym_db.RegisterMessage(Names)

Package = _reflection.GeneratedProtocolMessageType('Package', (_message.Message,), dict(
  DESCRIPTOR = _PACKAGE,
  __module__ = 'proto.hex_pb_names_pb2'
  # @@protoc_insertion_point(class_scope:Package)
  ))
_sym_db.RegisterMessage(Package)


# @@protoc_insertion_point(module_scope)
