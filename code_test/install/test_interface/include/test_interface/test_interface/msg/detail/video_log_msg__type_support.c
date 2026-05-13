// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from test_interface:msg/VideoLogMsg.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "test_interface/msg/detail/video_log_msg__rosidl_typesupport_introspection_c.h"
#include "test_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "test_interface/msg/detail/video_log_msg__functions.h"
#include "test_interface/msg/detail/video_log_msg__struct.h"


// Include directives for member types
// Member `obj_list`
#include "test_interface/msg/object_msg.h"
// Member `obj_list`
#include "test_interface/msg/detail/object_msg__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  test_interface__msg__VideoLogMsg__init(message_memory);
}

void test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_fini_function(void * message_memory)
{
  test_interface__msg__VideoLogMsg__fini(message_memory);
}

size_t test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__size_function__VideoLogMsg__obj_list(
  const void * untyped_member)
{
  const test_interface__msg__ObjectMsg__Sequence * member =
    (const test_interface__msg__ObjectMsg__Sequence *)(untyped_member);
  return member->size;
}

const void * test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__get_const_function__VideoLogMsg__obj_list(
  const void * untyped_member, size_t index)
{
  const test_interface__msg__ObjectMsg__Sequence * member =
    (const test_interface__msg__ObjectMsg__Sequence *)(untyped_member);
  return &member->data[index];
}

void * test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__get_function__VideoLogMsg__obj_list(
  void * untyped_member, size_t index)
{
  test_interface__msg__ObjectMsg__Sequence * member =
    (test_interface__msg__ObjectMsg__Sequence *)(untyped_member);
  return &member->data[index];
}

void test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__fetch_function__VideoLogMsg__obj_list(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const test_interface__msg__ObjectMsg * item =
    ((const test_interface__msg__ObjectMsg *)
    test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__get_const_function__VideoLogMsg__obj_list(untyped_member, index));
  test_interface__msg__ObjectMsg * value =
    (test_interface__msg__ObjectMsg *)(untyped_value);
  *value = *item;
}

void test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__assign_function__VideoLogMsg__obj_list(
  void * untyped_member, size_t index, const void * untyped_value)
{
  test_interface__msg__ObjectMsg * item =
    ((test_interface__msg__ObjectMsg *)
    test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__get_function__VideoLogMsg__obj_list(untyped_member, index));
  const test_interface__msg__ObjectMsg * value =
    (const test_interface__msg__ObjectMsg *)(untyped_value);
  *item = *value;
}

bool test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__resize_function__VideoLogMsg__obj_list(
  void * untyped_member, size_t size)
{
  test_interface__msg__ObjectMsg__Sequence * member =
    (test_interface__msg__ObjectMsg__Sequence *)(untyped_member);
  test_interface__msg__ObjectMsg__Sequence__fini(member);
  return test_interface__msg__ObjectMsg__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_message_member_array[5] = {
  {
    "isturning",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(test_interface__msg__VideoLogMsg, isturning),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "refer",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(test_interface__msg__VideoLogMsg, refer),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "obj_list",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(test_interface__msg__VideoLogMsg, obj_list),  // bytes offset in struct
    NULL,  // default value
    test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__size_function__VideoLogMsg__obj_list,  // size() function pointer
    test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__get_const_function__VideoLogMsg__obj_list,  // get_const(index) function pointer
    test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__get_function__VideoLogMsg__obj_list,  // get(index) function pointer
    test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__fetch_function__VideoLogMsg__obj_list,  // fetch(index, &value) function pointer
    test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__assign_function__VideoLogMsg__obj_list,  // assign(index, value) function pointer
    test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__resize_function__VideoLogMsg__obj_list  // resize(index) function pointer
  },
  {
    "linear",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(test_interface__msg__VideoLogMsg, linear),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "angular",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(test_interface__msg__VideoLogMsg, angular),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_message_members = {
  "test_interface__msg",  // message namespace
  "VideoLogMsg",  // message name
  5,  // number of fields
  sizeof(test_interface__msg__VideoLogMsg),
  test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_message_member_array,  // message members
  test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_init_function,  // function to initialize message memory (memory has to be allocated)
  test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_message_type_support_handle = {
  0,
  &test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_test_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, test_interface, msg, VideoLogMsg)() {
  test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, test_interface, msg, ObjectMsg)();
  if (!test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_message_type_support_handle.typesupport_identifier) {
    test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &test_interface__msg__VideoLogMsg__rosidl_typesupport_introspection_c__VideoLogMsg_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
