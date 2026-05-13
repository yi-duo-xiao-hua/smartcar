// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from test_interface:msg/ResnetMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__STRUCT_H_
#define TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ResnetMsg in the package test_interface.
typedef struct test_interface__msg__ResnetMsg
{
  int32_t line_x;
  int32_t line_y;
} test_interface__msg__ResnetMsg;

// Struct for a sequence of test_interface__msg__ResnetMsg.
typedef struct test_interface__msg__ResnetMsg__Sequence
{
  test_interface__msg__ResnetMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_interface__msg__ResnetMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__STRUCT_H_
