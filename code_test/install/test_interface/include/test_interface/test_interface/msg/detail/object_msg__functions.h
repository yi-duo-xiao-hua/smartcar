// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from test_interface:msg/ObjectMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__FUNCTIONS_H_
#define TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "test_interface/msg/rosidl_generator_c__visibility_control.h"

#include "test_interface/msg/detail/object_msg__struct.h"

/// Initialize msg/ObjectMsg message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * test_interface__msg__ObjectMsg
 * )) before or use
 * test_interface__msg__ObjectMsg__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
bool
test_interface__msg__ObjectMsg__init(test_interface__msg__ObjectMsg * msg);

/// Finalize msg/ObjectMsg message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
void
test_interface__msg__ObjectMsg__fini(test_interface__msg__ObjectMsg * msg);

/// Create msg/ObjectMsg message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * test_interface__msg__ObjectMsg__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
test_interface__msg__ObjectMsg *
test_interface__msg__ObjectMsg__create();

/// Destroy msg/ObjectMsg message.
/**
 * It calls
 * test_interface__msg__ObjectMsg__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
void
test_interface__msg__ObjectMsg__destroy(test_interface__msg__ObjectMsg * msg);

/// Check for msg/ObjectMsg message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
bool
test_interface__msg__ObjectMsg__are_equal(const test_interface__msg__ObjectMsg * lhs, const test_interface__msg__ObjectMsg * rhs);

/// Copy a msg/ObjectMsg message.
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
test_interface__msg__ObjectMsg__copy(
  const test_interface__msg__ObjectMsg * input,
  test_interface__msg__ObjectMsg * output);

/// Initialize array of msg/ObjectMsg messages.
/**
 * It allocates the memory for the number of elements and calls
 * test_interface__msg__ObjectMsg__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
bool
test_interface__msg__ObjectMsg__Sequence__init(test_interface__msg__ObjectMsg__Sequence * array, size_t size);

/// Finalize array of msg/ObjectMsg messages.
/**
 * It calls
 * test_interface__msg__ObjectMsg__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
void
test_interface__msg__ObjectMsg__Sequence__fini(test_interface__msg__ObjectMsg__Sequence * array);

/// Create array of msg/ObjectMsg messages.
/**
 * It allocates the memory for the array and calls
 * test_interface__msg__ObjectMsg__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
test_interface__msg__ObjectMsg__Sequence *
test_interface__msg__ObjectMsg__Sequence__create(size_t size);

/// Destroy array of msg/ObjectMsg messages.
/**
 * It calls
 * test_interface__msg__ObjectMsg__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
void
test_interface__msg__ObjectMsg__Sequence__destroy(test_interface__msg__ObjectMsg__Sequence * array);

/// Check for msg/ObjectMsg message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_test_interface
bool
test_interface__msg__ObjectMsg__Sequence__are_equal(const test_interface__msg__ObjectMsg__Sequence * lhs, const test_interface__msg__ObjectMsg__Sequence * rhs);

/// Copy an array of msg/ObjectMsg messages.
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
test_interface__msg__ObjectMsg__Sequence__copy(
  const test_interface__msg__ObjectMsg__Sequence * input,
  test_interface__msg__ObjectMsg__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__FUNCTIONS_H_
