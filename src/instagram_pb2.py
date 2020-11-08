# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/instagram.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import grpc_proto_validator.validator_pb2 as validator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/instagram.proto',
  package='instagram',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x15proto/instagram.proto\x12\tinstagram\x1a\x0fvalidator.proto\"\xee\x05\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tpermalink\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x12\n\ncreated_at\x18\x04 \x01(\t\x12\x17\n\x0f\x63reated_at_time\x18\x05 \x01(\t\x12\x12\n\ntext_clean\x18\x06 \x01(\t\x12\x0c\n\x04text\x18\x07 \x01(\t\x12\x16\n\x0etext_sentiment\x18\x08 \x01(\t\x12\x0f\n\x07user_id\x18\t \x01(\t\x12\x11\n\tuser_name\x18\n \x01(\t\x12\x0c\n\x04name\x18\x0b \x01(\t\x12\x18\n\x10user_description\x18\x0c \x01(\t\x12\x15\n\ruser_verified\x18\r \x01(\x08\x12\x1c\n\x14user_followers_count\x18\x0e \x01(\x03\x12\x1c\n\x14user_following_count\x18\x0f \x01(\x03\x12\x1b\n\x13user_timeline_count\x18\x10 \x01(\x05\x12\x1c\n\x14user_highlight_count\x18\x11 \x01(\x05\x12\x12\n\nis_private\x18\x12 \x01(\x08\x12\x15\n\ruser_link_url\x18\x13 \x01(\t\x12\x1e\n\x16user_profile_image_url\x18\x14 \x01(\t\x12\x12\n\nlike_count\x18\x15 \x01(\x03\x12\x15\n\rcomment_count\x18\x16 \x01(\x03\x12\x18\n\x10video_view_count\x18\x17 \x01(\x03\x12$\n\x08mentions\x18\x18 \x03(\x0b\x32\x12.instagram.Mention\x12$\n\x08hashtags\x18\x19 \x03(\x0b\x32\x12.instagram.Hashtag\x12\x12\n\nengagement\x18\x1a \x01(\x03\x12\x17\n\x0fpotential_reach\x18\x1b \x01(\x03\x12\x17\n\x0f\x65ngagement_rate\x18\x1c \x01(\x02\x12\x17\n\x0f\x63omment_disable\x18\x1d \x01(\x08\x12\x10\n\x08is_video\x18\x1e \x01(\x08\x12\x11\n\tvideo_url\x18\x1f \x01(\t\x12\x13\n\x0b\x64isplay_url\x18  \x01(\t\"\x17\n\x07Mention\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x17\n\x07Hashtag\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x81\x01\n\x10instagramRequest\x12\x16\n\x07keyword\x18\x01 \x01(\tB\x05\x9a\x42\x02`\x01\x12\x1a\n\x0bsearch_type\x18\x02 \x01(\tB\x05\x9a\x42\x02`\x01\x12\x14\n\x05since\x18\x03 \x01(\tB\x05\x9a\x42\x02`\x01\x12\x14\n\x05until\x18\x04 \x01(\tB\x05\x9a\x42\x02`\x01\x12\r\n\x05proxy\x18\x05 \x01(\t\"V\n\x11instagramResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08updateAt\x18\x02 \x01(\t\x12\x1e\n\x05items\x18\x03 \x03(\x0b\x32\x0f.instagram.Item2Y\n\tinstagram\x12L\n\rStreamRequest\x12\x1b.instagram.instagramRequest\x1a\x1c.instagram.instagramResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[validator__pb2.DESCRIPTOR,])




_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='instagram.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='instagram.Item.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permalink', full_name='instagram.Item.permalink', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='instagram.Item.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='instagram.Item.created_at', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at_time', full_name='instagram.Item.created_at_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_clean', full_name='instagram.Item.text_clean', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='instagram.Item.text', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_sentiment', full_name='instagram.Item.text_sentiment', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='instagram.Item.user_id', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='instagram.Item.user_name', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='instagram.Item.name', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_description', full_name='instagram.Item.user_description', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_verified', full_name='instagram.Item.user_verified', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_followers_count', full_name='instagram.Item.user_followers_count', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_following_count', full_name='instagram.Item.user_following_count', index=14,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_timeline_count', full_name='instagram.Item.user_timeline_count', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_highlight_count', full_name='instagram.Item.user_highlight_count', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_private', full_name='instagram.Item.is_private', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_link_url', full_name='instagram.Item.user_link_url', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_profile_image_url', full_name='instagram.Item.user_profile_image_url', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='like_count', full_name='instagram.Item.like_count', index=20,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment_count', full_name='instagram.Item.comment_count', index=21,
      number=22, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_view_count', full_name='instagram.Item.video_view_count', index=22,
      number=23, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mentions', full_name='instagram.Item.mentions', index=23,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hashtags', full_name='instagram.Item.hashtags', index=24,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engagement', full_name='instagram.Item.engagement', index=25,
      number=26, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='potential_reach', full_name='instagram.Item.potential_reach', index=26,
      number=27, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engagement_rate', full_name='instagram.Item.engagement_rate', index=27,
      number=28, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment_disable', full_name='instagram.Item.comment_disable', index=28,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_video', full_name='instagram.Item.is_video', index=29,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_url', full_name='instagram.Item.video_url', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_url', full_name='instagram.Item.display_url', index=31,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=804,
)


_MENTION = _descriptor.Descriptor(
  name='Mention',
  full_name='instagram.Mention',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='instagram.Mention.text', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=806,
  serialized_end=829,
)


_HASHTAG = _descriptor.Descriptor(
  name='Hashtag',
  full_name='instagram.Hashtag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='instagram.Hashtag.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=831,
  serialized_end=854,
)


_INSTAGRAMREQUEST = _descriptor.Descriptor(
  name='instagramRequest',
  full_name='instagram.instagramRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword', full_name='instagram.instagramRequest.keyword', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\232B\002`\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_type', full_name='instagram.instagramRequest.search_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\232B\002`\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='since', full_name='instagram.instagramRequest.since', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\232B\002`\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='until', full_name='instagram.instagramRequest.until', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\232B\002`\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy', full_name='instagram.instagramRequest.proxy', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=857,
  serialized_end=986,
)


_INSTAGRAMRESPONSE = _descriptor.Descriptor(
  name='instagramResponse',
  full_name='instagram.instagramResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='instagram.instagramResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateAt', full_name='instagram.instagramResponse.updateAt', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='instagram.instagramResponse.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=988,
  serialized_end=1074,
)

_ITEM.fields_by_name['mentions'].message_type = _MENTION
_ITEM.fields_by_name['hashtags'].message_type = _HASHTAG
_INSTAGRAMRESPONSE.fields_by_name['items'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['Mention'] = _MENTION
DESCRIPTOR.message_types_by_name['Hashtag'] = _HASHTAG
DESCRIPTOR.message_types_by_name['instagramRequest'] = _INSTAGRAMREQUEST
DESCRIPTOR.message_types_by_name['instagramResponse'] = _INSTAGRAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'proto.instagram_pb2'
  # @@protoc_insertion_point(class_scope:instagram.Item)
  })
_sym_db.RegisterMessage(Item)

Mention = _reflection.GeneratedProtocolMessageType('Mention', (_message.Message,), {
  'DESCRIPTOR' : _MENTION,
  '__module__' : 'proto.instagram_pb2'
  # @@protoc_insertion_point(class_scope:instagram.Mention)
  })
_sym_db.RegisterMessage(Mention)

Hashtag = _reflection.GeneratedProtocolMessageType('Hashtag', (_message.Message,), {
  'DESCRIPTOR' : _HASHTAG,
  '__module__' : 'proto.instagram_pb2'
  # @@protoc_insertion_point(class_scope:instagram.Hashtag)
  })
_sym_db.RegisterMessage(Hashtag)

instagramRequest = _reflection.GeneratedProtocolMessageType('instagramRequest', (_message.Message,), {
  'DESCRIPTOR' : _INSTAGRAMREQUEST,
  '__module__' : 'proto.instagram_pb2'
  # @@protoc_insertion_point(class_scope:instagram.instagramRequest)
  })
_sym_db.RegisterMessage(instagramRequest)

instagramResponse = _reflection.GeneratedProtocolMessageType('instagramResponse', (_message.Message,), {
  'DESCRIPTOR' : _INSTAGRAMRESPONSE,
  '__module__' : 'proto.instagram_pb2'
  # @@protoc_insertion_point(class_scope:instagram.instagramResponse)
  })
_sym_db.RegisterMessage(instagramResponse)


_INSTAGRAMREQUEST.fields_by_name['keyword']._options = None
_INSTAGRAMREQUEST.fields_by_name['search_type']._options = None
_INSTAGRAMREQUEST.fields_by_name['since']._options = None
_INSTAGRAMREQUEST.fields_by_name['until']._options = None

_INSTAGRAM = _descriptor.ServiceDescriptor(
  name='instagram',
  full_name='instagram.instagram',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1076,
  serialized_end=1165,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamRequest',
    full_name='instagram.instagram.StreamRequest',
    index=0,
    containing_service=None,
    input_type=_INSTAGRAMREQUEST,
    output_type=_INSTAGRAMRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INSTAGRAM)

DESCRIPTOR.services_by_name['instagram'] = _INSTAGRAM

# @@protoc_insertion_point(module_scope)
