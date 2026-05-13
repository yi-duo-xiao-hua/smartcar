// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from test_interface:msg/ObjectMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__STRUCT_H_
#define TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'obj_type'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/ObjectMsg in the package test_interface.
typedef struct test_interface__msg__ObjectMsg
{
  rosidl_runtime_c__String obj_type;
  int32_t xl;
  int32_t xr;
  int32_t yu;
  int32_t yd;
  int32_t distance;
} test_interface__msg__ObjectMsg;

// Struct for a sequence of test_interface__msg__ObjectMsg.
typedef struct test_interface__msg__ObjectMsg__Sequence
{
  test_interface__msg__ObjectMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_interface__msg__ObjectMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__STRUCT_H_
