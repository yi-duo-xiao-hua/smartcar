// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from test_interface:msg/ObjPosition.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__STRUCT_H_
#define TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ObjPosition in the package test_interface.
typedef struct test_interface__msg__ObjPosition
{
  int32_t x;
  int32_t x_left;
  int32_t x_right;
  int32_t area;
  int32_t y;
  int32_t y_up;
  int32_t y_down;
} test_interface__msg__ObjPosition;

// Struct for a sequence of test_interface__msg__ObjPosition.
typedef struct test_interface__msg__ObjPosition__Sequence
{
  test_interface__msg__ObjPosition * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_interface__msg__ObjPosition__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__STRUCT_H_
