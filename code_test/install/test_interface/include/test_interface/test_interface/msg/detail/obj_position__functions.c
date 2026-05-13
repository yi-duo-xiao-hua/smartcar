// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from test_interface:msg/ObjPosition.idl
// generated code does not contain a copyright notice
#include "test_interface/msg/detail/obj_position__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
test_interface__msg__ObjPosition__init(test_interface__msg__ObjPosition * msg)
{
  if (!msg) {
    return false;
  }
  // x
  // x_left
  // x_right
  // area
  // y
  // y_up
  // y_down
  return true;
}

void
test_interface__msg__ObjPosition__fini(test_interface__msg__ObjPosition * msg)
{
  if (!msg) {
    return;
  }
  // x
  // x_left
  // x_right
  // area
  // y
  // y_up
  // y_down
}

bool
test_interface__msg__ObjPosition__are_equal(const test_interface__msg__ObjPosition * lhs, const test_interface__msg__ObjPosition * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // x_left
  if (lhs->x_left != rhs->x_left) {
    return false;
  }
  // x_right
  if (lhs->x_right != rhs->x_right) {
    return false;
  }
  // area
  if (lhs->area != rhs->area) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  // y_up
  if (lhs->y_up != rhs->y_up) {
    return false;
  }
  // y_down
  if (lhs->y_down != rhs->y_down) {
    return false;
  }
  return true;
}

bool
test_interface__msg__ObjPosition__copy(
  const test_interface__msg__ObjPosition * input,
  test_interface__msg__ObjPosition * output)
{
  if (!input || !output) {
    return false;
  }
  // x
  output->x = input->x;
  // x_left
  output->x_left = input->x_left;
  // x_right
  output->x_right = input->x_right;
  // area
  output->area = input->area;
  // y
  output->y = input->y;
  // y_up
  output->y_up = input->y_up;
  // y_down
  output->y_down = input->y_down;
  return true;
}

test_interface__msg__ObjPosition *
test_interface__msg__ObjPosition__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__ObjPosition * msg = (test_interface__msg__ObjPosition *)allocator.allocate(sizeof(test_interface__msg__ObjPosition), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_interface__msg__ObjPosition));
  bool success = test_interface__msg__ObjPosition__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
test_interface__msg__ObjPosition__destroy(test_interface__msg__ObjPosition * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    test_interface__msg__ObjPosition__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
test_interface__msg__ObjPosition__Sequence__init(test_interface__msg__ObjPosition__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__ObjPosition * data = NULL;

  if (size) {
    data = (test_interface__msg__ObjPosition *)allocator.zero_allocate(size, sizeof(test_interface__msg__ObjPosition), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_interface__msg__ObjPosition__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_interface__msg__ObjPosition__fini(&data[i - 1]);
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
test_interface__msg__ObjPosition__Sequence__fini(test_interface__msg__ObjPosition__Sequence * array)
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
      test_interface__msg__ObjPosition__fini(&array->data[i]);
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

test_interface__msg__ObjPosition__Sequence *
test_interface__msg__ObjPosition__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__ObjPosition__Sequence * array = (test_interface__msg__ObjPosition__Sequence *)allocator.allocate(sizeof(test_interface__msg__ObjPosition__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = test_interface__msg__ObjPosition__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
test_interface__msg__ObjPosition__Sequence__destroy(test_interface__msg__ObjPosition__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    test_interface__msg__ObjPosition__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
test_interface__msg__ObjPosition__Sequence__are_equal(const test_interface__msg__ObjPosition__Sequence * lhs, const test_interface__msg__ObjPosition__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!test_interface__msg__ObjPosition__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
test_interface__msg__ObjPosition__Sequence__copy(
  const test_interface__msg__ObjPosition__Sequence * input,
  test_interface__msg__ObjPosition__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(test_interface__msg__ObjPosition);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    test_interface__msg__ObjPosition * data =
      (test_interface__msg__ObjPosition *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!test_interface__msg__ObjPosition__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          test_interface__msg__ObjPosition__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!test_interface__msg__ObjPosition__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
