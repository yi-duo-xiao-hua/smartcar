// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from test_interface:msg/VideoLogMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__STRUCT_H_
#define TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'obj_list'
#include "test_interface/msg/detail/object_msg__struct.h"

/// Struct defined in msg/VideoLogMsg in the package test_interface.
typedef struct test_interface__msg__VideoLogMsg
{
  bool isturning;
  float refer;
  test_interface__msg__ObjectMsg__Sequence obj_list;
  float linear;
  float angular;
} test_interface__msg__VideoLogMsg;

// Struct for a sequence of test_interface__msg__VideoLogMsg.
typedef struct test_interface__msg__VideoLogMsg__Sequence
{
  test_interface__msg__VideoLogMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_interface__msg__VideoLogMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__STRUCT_H_
