# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/twitter.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import validator_pb2 as validator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/twitter.proto',
  package='twitter',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x13proto/twitter.proto\x12\x07twitter\x1a\x0fvalidator.proto\"\x92\x07\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tpermalink\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x12\n\ncreated_at\x18\x04 \x01(\t\x12\x17\n\x0f\x63reated_at_time\x18\x05 \x01(\t\x12\x16\n\x0e\x66ull_text_norm\x18\x06 \x01(\t\x12\x17\n\x0f\x66ull_text_clean\x18\x07 \x01(\t\x12\x11\n\tfull_text\x18\x08 \x01(\t\x12\x16\n\x0etext_sentiment\x18\t \x01(\t\x12\x0f\n\x07user_id\x18\n \x01(\t\x12\x11\n\tuser_name\x18\x0b \x01(\t\x12\x13\n\x0bscreen_name\x18\x0c \x01(\t\x12\x18\n\x10user_description\x18\r \x01(\t\x12\x15\n\ruser_verified\x18\x0e \x01(\x08\x12\x17\n\x0fuser_created_at\x18\x0f \x01(\t\x12\x1c\n\x14user_followers_count\x18\x10 \x01(\x05\x12\x1a\n\x12user_friends_count\x18\x11 \x01(\x05\x12\x1b\n\x13user_statuses_count\x18\x12 \x01(\x05\x12\x1d\n\x15user_favourites_count\x18\x13 \x01(\x05\x12\x19\n\x11user_listed_count\x18\x14 \x01(\x05\x12\x18\n\x10user_media_count\x18\x15 \x01(\x05\x12\x15\n\ruser_location\x18\x16 \x01(\x05\x12\x16\n\x0euser_protected\x18\x17 \x01(\x08\x12\x15\n\ruser_link_url\x18\x18 \x01(\t\x12\x1e\n\x16user_profile_image_url\x18\x19 \x01(\t\x12\x13\n\x0breply_count\x18\x1a \x01(\x05\x12\x15\n\rretweet_count\x18\x1b \x01(\x05\x12\x12\n\nlike_count\x18\x1c \x01(\x05\x12\x13\n\x0bquote_count\x18\x1d \x01(\x05\x12\x17\n\x0f\x63onversation_id\x18\x1e \x01(\x05\x12\x0e\n\x06\x64\x65vice\x18\x1f \x01(\t\x12\x0c\n\x04lang\x18  \x01(\t\x12!\n\x05media\x18! \x03(\x0b\x32\x12.twitter.mediaItem\x12\"\n\x08mentions\x18\" \x03(\x0b\x32\x10.twitter.Mention\x12\"\n\x08hashtags\x18# \x03(\x0b\x32\x10.twitter.Hashtag\x12\x12\n\nengagement\x18$ \x01(\x03\x12\x17\n\x0fpotential_reach\x18% \x01(\x03\x12\x17\n\x0f\x65ngagement_rate\x18& \x01(\x02\":\n\tmediaItem\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x1f\n\x06source\x18\x02 \x03(\x0b\x32\x0f.twitter.Source\"/\n\x06Source\x12\x13\n\x0bpreview_url\x18\x01 \x01(\t\x12\x10\n\x08\x66ull_url\x18\x02 \x01(\t\"-\n\x07Mention\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\"\x17\n\x07Hashtag\x12\x0c\n\x04text\x18\x01 \x01(\t\"p\n\x0etwitterRequest\x12\x16\n\x07keyword\x18\x01 \x01(\tB\x05\x9a\x42\x02`\x01\x12\x1a\n\x0bsearch_type\x18\x02 \x01(\tB\x05\x9a\x42\x02`\x01\x12\x14\n\x05since\x18\x03 \x01(\tB\x05\x9a\x42\x02`\x01\x12\x14\n\x05until\x18\x04 \x01(\tB\x05\x9a\x42\x02`\x01\"R\n\x0ftwitterResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08updateAt\x18\x02 \x01(\t\x12\x1c\n\x05items\x18\x03 \x03(\x0b\x32\r.twitter.Item2O\n\x07twitter\x12\x44\n\rStreamRequest\x12\x17.twitter.twitterRequest\x1a\x18.twitter.twitterResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[validator__pb2.DESCRIPTOR,])




_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='twitter.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='twitter.Item.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permalink', full_name='twitter.Item.permalink', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='twitter.Item.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='twitter.Item.created_at', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at_time', full_name='twitter.Item.created_at_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_text_norm', full_name='twitter.Item.full_text_norm', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_text_clean', full_name='twitter.Item.full_text_clean', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_text', full_name='twitter.Item.full_text', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_sentiment', full_name='twitter.Item.text_sentiment', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='twitter.Item.user_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='twitter.Item.user_name', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='screen_name', full_name='twitter.Item.screen_name', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_description', full_name='twitter.Item.user_description', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_verified', full_name='twitter.Item.user_verified', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_created_at', full_name='twitter.Item.user_created_at', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_followers_count', full_name='twitter.Item.user_followers_count', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_friends_count', full_name='twitter.Item.user_friends_count', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_statuses_count', full_name='twitter.Item.user_statuses_count', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_favourites_count', full_name='twitter.Item.user_favourites_count', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_listed_count', full_name='twitter.Item.user_listed_count', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_media_count', full_name='twitter.Item.user_media_count', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_location', full_name='twitter.Item.user_location', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_protected', full_name='twitter.Item.user_protected', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_link_url', full_name='twitter.Item.user_link_url', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_profile_image_url', full_name='twitter.Item.user_profile_image_url', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reply_count', full_name='twitter.Item.reply_count', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retweet_count', full_name='twitter.Item.retweet_count', index=26,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='like_count', full_name='twitter.Item.like_count', index=27,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quote_count', full_name='twitter.Item.quote_count', index=28,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversation_id', full_name='twitter.Item.conversation_id', index=29,
      number=30, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='twitter.Item.device', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lang', full_name='twitter.Item.lang', index=31,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='media', full_name='twitter.Item.media', index=32,
      number=33, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mentions', full_name='twitter.Item.mentions', index=33,
      number=34, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hashtags', full_name='twitter.Item.hashtags', index=34,
      number=35, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engagement', full_name='twitter.Item.engagement', index=35,
      number=36, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='potential_reach', full_name='twitter.Item.potential_reach', index=36,
      number=37, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engagement_rate', full_name='twitter.Item.engagement_rate', index=37,
      number=38, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=50,
  serialized_end=964,
)


_MEDIAITEM = _descriptor.Descriptor(
  name='mediaItem',
  full_name='twitter.mediaItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='twitter.mediaItem.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='twitter.mediaItem.source', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=966,
  serialized_end=1024,
)


_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='twitter.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='preview_url', full_name='twitter.Source.preview_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_url', full_name='twitter.Source.full_url', index=1,
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
  serialized_start=1026,
  serialized_end=1073,
)


_MENTION = _descriptor.Descriptor(
  name='Mention',
  full_name='twitter.Mention',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='twitter.Mention.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='twitter.Mention.display_name', index=1,
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
  serialized_start=1075,
  serialized_end=1120,
)


_HASHTAG = _descriptor.Descriptor(
  name='Hashtag',
  full_name='twitter.Hashtag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='twitter.Hashtag.text', index=0,
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
  serialized_start=1122,
  serialized_end=1145,
)


_TWITTERREQUEST = _descriptor.Descriptor(
  name='twitterRequest',
  full_name='twitter.twitterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword', full_name='twitter.twitterRequest.keyword', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\232B\002`\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_type', full_name='twitter.twitterRequest.search_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\232B\002`\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='since', full_name='twitter.twitterRequest.since', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\232B\002`\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='until', full_name='twitter.twitterRequest.until', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\232B\002`\001', file=DESCRIPTOR),
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
  serialized_start=1147,
  serialized_end=1259,
)


_TWITTERRESPONSE = _descriptor.Descriptor(
  name='twitterResponse',
  full_name='twitter.twitterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='twitter.twitterResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateAt', full_name='twitter.twitterResponse.updateAt', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='twitter.twitterResponse.items', index=2,
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
  serialized_start=1261,
  serialized_end=1343,
)

_ITEM.fields_by_name['media'].message_type = _MEDIAITEM
_ITEM.fields_by_name['mentions'].message_type = _MENTION
_ITEM.fields_by_name['hashtags'].message_type = _HASHTAG
_MEDIAITEM.fields_by_name['source'].message_type = _SOURCE
_TWITTERRESPONSE.fields_by_name['items'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['mediaItem'] = _MEDIAITEM
DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
DESCRIPTOR.message_types_by_name['Mention'] = _MENTION
DESCRIPTOR.message_types_by_name['Hashtag'] = _HASHTAG
DESCRIPTOR.message_types_by_name['twitterRequest'] = _TWITTERREQUEST
DESCRIPTOR.message_types_by_name['twitterResponse'] = _TWITTERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'proto.twitter_pb2'
  # @@protoc_insertion_point(class_scope:twitter.Item)
  })
_sym_db.RegisterMessage(Item)

mediaItem = _reflection.GeneratedProtocolMessageType('mediaItem', (_message.Message,), {
  'DESCRIPTOR' : _MEDIAITEM,
  '__module__' : 'proto.twitter_pb2'
  # @@protoc_insertion_point(class_scope:twitter.mediaItem)
  })
_sym_db.RegisterMessage(mediaItem)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'proto.twitter_pb2'
  # @@protoc_insertion_point(class_scope:twitter.Source)
  })
_sym_db.RegisterMessage(Source)

Mention = _reflection.GeneratedProtocolMessageType('Mention', (_message.Message,), {
  'DESCRIPTOR' : _MENTION,
  '__module__' : 'proto.twitter_pb2'
  # @@protoc_insertion_point(class_scope:twitter.Mention)
  })
_sym_db.RegisterMessage(Mention)

Hashtag = _reflection.GeneratedProtocolMessageType('Hashtag', (_message.Message,), {
  'DESCRIPTOR' : _HASHTAG,
  '__module__' : 'proto.twitter_pb2'
  # @@protoc_insertion_point(class_scope:twitter.Hashtag)
  })
_sym_db.RegisterMessage(Hashtag)

twitterRequest = _reflection.GeneratedProtocolMessageType('twitterRequest', (_message.Message,), {
  'DESCRIPTOR' : _TWITTERREQUEST,
  '__module__' : 'proto.twitter_pb2'
  # @@protoc_insertion_point(class_scope:twitter.twitterRequest)
  })
_sym_db.RegisterMessage(twitterRequest)

twitterResponse = _reflection.GeneratedProtocolMessageType('twitterResponse', (_message.Message,), {
  'DESCRIPTOR' : _TWITTERRESPONSE,
  '__module__' : 'proto.twitter_pb2'
  # @@protoc_insertion_point(class_scope:twitter.twitterResponse)
  })
_sym_db.RegisterMessage(twitterResponse)


_TWITTERREQUEST.fields_by_name['keyword']._options = None
_TWITTERREQUEST.fields_by_name['search_type']._options = None
_TWITTERREQUEST.fields_by_name['since']._options = None
_TWITTERREQUEST.fields_by_name['until']._options = None

_TWITTER = _descriptor.ServiceDescriptor(
  name='twitter',
  full_name='twitter.twitter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1345,
  serialized_end=1424,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamRequest',
    full_name='twitter.twitter.StreamRequest',
    index=0,
    containing_service=None,
    input_type=_TWITTERREQUEST,
    output_type=_TWITTERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TWITTER)

DESCRIPTOR.services_by_name['twitter'] = _TWITTER

# @@protoc_insertion_point(module_scope)
