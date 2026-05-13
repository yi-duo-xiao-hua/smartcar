// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from test_interface:msg/VideoLogMsg.idl
// generated code does not contain a copyright notice
#include "test_interface/msg/detail/video_log_msg__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "test_interface/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "test_interface/msg/detail/video_log_msg__struct.h"
#include "test_interface/msg/detail/video_log_msg__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "test_interface/msg/detail/object_msg__functions.h"  // obj_list

// forward declare type support functions
size_t get_serialized_size_test_interface__msg__ObjectMsg(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_test_interface__msg__ObjectMsg(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, test_interface, msg, ObjectMsg)();


using _VideoLogMsg__ros_msg_type = test_interface__msg__VideoLogMsg;

static bool _VideoLogMsg__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _VideoLogMsg__ros_msg_type * ros_message = static_cast<const _VideoLogMsg__ros_msg_type *>(untyped_ros_message);
  // Field name: isturning
  {
    cdr << (ros_message->isturning ? true : false);
  }

  // Field name: refer
  {
    cdr << ros_message->refer;
  }

  // Field name: obj_list
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, test_interface, msg, ObjectMsg
      )()->data);
    size_t size = ros_message->obj_list.size;
    auto array_ptr = ros_message->obj_list.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_serialize(
          &array_ptr[i], cdr))
      {
        return false;
      }
    }
  }

  // Field name: linear
  {
    cdr << ros_message->linear;
  }

  // Field name: angular
  {
    cdr << ros_message->angular;
  }

  return true;
}

static bool _VideoLogMsg__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _VideoLogMsg__ros_msg_type * ros_message = static_cast<_VideoLogMsg__ros_msg_type *>(untyped_ros_message);
  // Field name: isturning
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->isturning = tmp ? true : false;
  }

  // Field name: refer
  {
    cdr >> ros_message->refer;
  }

  // Field name: obj_list
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, test_interface, msg, ObjectMsg
      )()->data);
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->obj_list.data) {
      test_interface__msg__ObjectMsg__Sequence__fini(&ros_message->obj_list);
    }
    if (!test_interface__msg__ObjectMsg__Sequence__init(&ros_message->obj_list, size)) {
      fprintf(stderr, "failed to create array for field 'obj_list'");
      return false;
    }
    auto array_ptr = ros_message->obj_list.data;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_deserialize(
          cdr, &array_ptr[i]))
      {
        return false;
      }
    }
  }

  // Field name: linear
  {
    cdr >> ros_message->linear;
  }

  // Field name: angular
  {
    cdr >> ros_message->angular;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_test_interface
size_t get_serialized_size_test_interface__msg__VideoLogMsg(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _VideoLogMsg__ros_msg_type * ros_message = static_cast<const _VideoLogMsg__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name isturning
  {
    size_t item_size = sizeof(ros_message->isturning);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name refer
  {
    size_t item_size = sizeof(ros_message->refer);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name obj_list
  {
    size_t array_size = ros_message->obj_list.size;
    auto array_ptr = ros_message->obj_list.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_test_interface__msg__ObjectMsg(
        &array_ptr[index], current_alignment);
    }
  }
  // field.name linear
  {
    size_t item_size = sizeof(ros_message->linear);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name angular
  {
    size_t item_size = sizeof(ros_message->angular);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _VideoLogMsg__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_test_interface__msg__VideoLogMsg(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_test_interface
size_t max_serialized_size_test_interface__msg__VideoLogMsg(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: isturning
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: refer
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: obj_list
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_test_interface__msg__ObjectMsg(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: linear
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: angular
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = test_interface__msg__VideoLogMsg;
    is_plain =
      (
      offsetof(DataType, angular) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _VideoLogMsg__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_test_interface__msg__VideoLogMsg(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_VideoLogMsg = {
  "test_interface::msg",
  "VideoLogMsg",
  _VideoLogMsg__cdr_serialize,
  _VideoLogMsg__cdr_deserialize,
  _VideoLogMsg__get_serialized_size,
  _VideoLogMsg__max_serialized_size
};

static rosidl_message_type_support_t _VideoLogMsg__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_VideoLogMsg,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, test_interface, msg, VideoLogMsg)() {
  return &_VideoLogMsg__type_support;
}

#if defined(__cplusplus)
}
#endif
