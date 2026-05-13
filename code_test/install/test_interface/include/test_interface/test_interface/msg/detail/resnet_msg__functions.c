// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from test_interface:msg/ResnetMsg.idl
// generated code does not contain a copyright notice
#include "test_interface/msg/detail/resnet_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
test_interface__msg__ResnetMsg__init(test_interface__msg__ResnetMsg * msg)
{
  if (!msg) {
    return false;
  }
  // line_x
  // line_y
  return true;
}

void
test_interface__msg__ResnetMsg__fini(test_interface__msg__ResnetMsg * msg)
{
  if (!msg) {
    return;
  }
  // line_x
  // line_y
}

bool
test_interface__msg__ResnetMsg__are_equal(const test_interface__msg__ResnetMsg * lhs, const test_interface__msg__ResnetMsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // line_x
  if (lhs->line_x != rhs->line_x) {
    return false;
  }
  // line_y
  if (lhs->line_y != rhs->line_y) {
    return false;
  }
  return true;
}

bool
test_interface__msg__ResnetMsg__copy(
  const test_interface__msg__ResnetMsg * input,
  test_interface__msg__ResnetMsg * output)
{
  if (!input || !output) {
    return false;
  }
  // line_x
  output->line_x = input->line_x;
  // line_y
  output->line_y = input->line_y;
  return true;
}

test_interface__msg__ResnetMsg *
test_interface__msg__ResnetMsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__ResnetMsg * msg = (test_interface__msg__ResnetMsg *)allocator.allocate(sizeof(test_interface__msg__ResnetMsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_interface__msg__ResnetMsg));
  bool success = test_interface__msg__ResnetMsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
test_interface__msg__ResnetMsg__destroy(test_interface__msg__ResnetMsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    test_interface__msg__ResnetMsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
test_interface__msg__ResnetMsg__Sequence__init(test_interface__msg__ResnetMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__ResnetMsg * data = NULL;

  if (size) {
    data = (test_interface__msg__ResnetMsg *)allocator.zero_allocate(size, sizeof(test_interface__msg__ResnetMsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_interface__msg__ResnetMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_interface__msg__ResnetMsg__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
test_interface__msg__ResnetMsg__Sequence__fini(test_interface__msg__ResnetMsg__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      test_interface__msg__ResnetMsg__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

test_interface__msg__ResnetMsg__Sequence *
test_interface__msg__ResnetMsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__ResnetMsg__Sequence * array = (test_interface__msg__ResnetMsg__Sequence *)allocator.allocate(sizeof(test_interface__msg__ResnetMsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = test_interface__msg__ResnetMsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
test_interface__msg__ResnetMsg__Sequence__destroy(test_interface__msg__ResnetMsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    test_interface__msg__ResnetMsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
test_interface__msg__ResnetMsg__Sequence__are_equal(const test_interface__msg__ResnetMsg__Sequence * lhs, const test_interface__msg__ResnetMsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!test_interface__msg__ResnetMsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
test_interface__msg__ResnetMsg__Sequence__copy(
  const test_interface__msg__ResnetMsg__Sequence * input,
  test_interface__msg__ResnetMsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(test_interface__msg__ResnetMsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    test_interface__msg__ResnetMsg * data =
      (test_interface__msg__ResnetMsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!test_interface__msg__ResnetMsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          test_interface__msg__ResnetMsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!test_interface__msg__ResnetMsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
