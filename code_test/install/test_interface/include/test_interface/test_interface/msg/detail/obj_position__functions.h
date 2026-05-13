// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from test_interface:msg/ObjPosition.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__FUNCTIONS_H_
#define TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "test_interface/msg/rosidl_generator_c__visibility_control.h"

#include "test_interface/msg/detail/obj_position__struct.h"

/// Initialize msg/ObjPosition message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * test_interface__msg__ObjPosition
 * )) before or use
 * test_interface__msg__ObjPosition__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
bool
test_interface__msg__ObjPosition__init(test_interface__msg__ObjPosition * msg);

/// Finalize msg/ObjPosition message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
void
test_interface__msg__ObjPosition__fini(test_interface__msg__ObjPosition * msg);

/// Create msg/ObjPosition message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * test_interface__msg__ObjPosition__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
test_interface__msg__ObjPosition *
test_interface__msg__ObjPosition__create();

/// Destroy msg/ObjPosition message.
/**
 * It calls
 * test_interface__msg__ObjPosition__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
void
test_interface__msg__ObjPosition__destroy(test_interface__msg__ObjPosition * msg);

/// Check for msg/ObjPosition message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
bool
test_interface__msg__ObjPosition__are_equal(const test_interface__msg__ObjPosition * lhs, const test_interface__msg__ObjPosition * rhs);

/// Copy a msg/ObjPosition message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
bool
test_interface__msg__ObjPosition__copy(
  const test_interface__msg__ObjPosition * input,
  test_interface__msg__ObjPosition * output);

/// Initialize array of msg/ObjPosition messages.
/**
 * It allocates the memory for the number of elements and calls
 * test_interface__msg__ObjPosition__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
bool
test_interface__msg__ObjPosition__Sequence__init(test_interface__msg__ObjPosition__Sequence * array, size_t size);

/// Finalize array of msg/ObjPosition messages.
/**
 * It calls
 * test_interface__msg__ObjPosition__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
void
test_interface__msg__ObjPosition__Sequence__fini(test_interface__msg__ObjPosition__Sequence * array);

/// Create array of msg/ObjPosition messages.
/**
 * It allocates the memory for the array and calls
 * test_interface__msg__ObjPosition__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
test_interface__msg__ObjPosition__Sequence *
test_interface__msg__ObjPosition__Sequence__create(size_t size);

/// Destroy array of msg/ObjPosition messages.
/**
 * It calls
 * test_interface__msg__ObjPosition__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
void
test_interface__msg__ObjPosition__Sequence__destroy(test_interface__msg__ObjPosition__Sequence * array);

/// Check for msg/ObjPosition message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
bool
test_interface__msg__ObjPosition__Sequence__are_equal(const test_interface__msg__ObjPosition__Sequence * lhs, const test_interface__msg__ObjPosition__Sequence * rhs);

/// Copy an array of msg/ObjPosition messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
bool
test_interface__msg__ObjPosition__Sequence__copy(
  const test_interface__msg__ObjPosition__Sequence * input,
  test_interface__msg__ObjPosition__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__FUNCTIONS_H_
