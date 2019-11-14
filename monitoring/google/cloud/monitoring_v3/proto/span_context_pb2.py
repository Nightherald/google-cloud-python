# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_v3/proto/span_context.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_v3/proto/span_context.proto",
    package="google.monitoring.v3",
    syntax="proto3",
    serialized_options=_b(
        "\n\030com.google.monitoring.v3B\020SpanContextProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3"
    ),
    serialized_pb=_b(
        '\n3google/cloud/monitoring_v3/proto/span_context.proto\x12\x14google.monitoring.v3" \n\x0bSpanContext\x12\x11\n\tspan_name\x18\x01 \x01(\tB\xa8\x01\n\x18\x63om.google.monitoring.v3B\x10SpanContextProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3b\x06proto3'
    ),
)


_SPANCONTEXT = _descriptor.Descriptor(
    name="SpanContext",
    full_name="google.monitoring.v3.SpanContext",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="span_name",
            full_name="google.monitoring.v3.SpanContext.span_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=77,
    serialized_end=109,
)

DESCRIPTOR.message_types_by_name["SpanContext"] = _SPANCONTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpanContext = _reflection.GeneratedProtocolMessageType(
    "SpanContext",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SPANCONTEXT,
        __module__="google.cloud.monitoring_v3.proto.span_context_pb2",
        __doc__="""The context of a span, attached to google.api.Distribution.Exemplars in
  google.api.Distribution values during aggregation.
  
  It contains the name of a span with format:
  projects/[PROJECT\_ID]/traces/[TRACE\_ID]/spans/[SPAN\_ID]
  
  
  Attributes:
      span_name:
          The resource name of the span in the following format:  ::
          projects/[PROJECT_ID]/traces/[TRACE_ID]/spans/[SPAN_ID]
          [TRACE\_ID] is a unique identifier for a trace within a
          project; it is a 32-character hexadecimal encoding of a
          16-byte array.  [SPAN\_ID] is a unique identifier for a span
          within a trace; it is a 16-character hexadecimal encoding of
          an 8-byte array.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.SpanContext)
    ),
)
_sym_db.RegisterMessage(SpanContext)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
