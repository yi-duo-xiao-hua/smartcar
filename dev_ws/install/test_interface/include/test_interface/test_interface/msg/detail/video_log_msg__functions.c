// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from test_interface:msg/VideoLogMsg.idl
// generated code does not contain a copyright notice
#include "test_interface/msg/detail/video_log_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `obj_list`
#include "test_interface/msg/detail/object_msg__functions.h"

bool
test_interface__msg__VideoLogMsg__init(test_interface__msg__VideoLogMsg * msg)
{
  if (!msg) {
    return false;
  }
  // isturning
  // refer
  // obj_list
  if (!test_interface__msg__ObjectMsg__Sequence__init(&msg->obj_list, 0)) {
    test_interface__msg__VideoLogMsg__fini(msg);
    return false;
  }
  // linear
  // angular
  return true;
}

void
test_interface__msg__VideoLogMsg__fini(test_interface__msg__VideoLogMsg * msg)
{
  if (!msg) {
    return;
  }
  // isturning
  // refer
  // obj_list
  test_interface__msg__ObjectMsg__Sequence__fini(&msg->obj_list);
  // linear
  // angular
}

bool
test_interface__msg__VideoLogMsg__are_equal(const test_interface__msg__VideoLogMsg * lhs, const test_interface__msg__VideoLogMsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // isturning
  if (lhs->isturning != rhs->isturning) {
    return false;
  }
  // refer
  if (lhs->refer != rhs->refer) {
    return false;
  }
  // obj_list
  if (!test_interface__msg__ObjectMsg__Sequence__are_equal(
      &(lhs->obj_list), &(rhs->obj_list)))
  {
    return false;
  }
  // linear
  if (lhs->linear != rhs->linear) {
    return false;
  }
  // angular
  if (lhs->angular != rhs->angular) {
    return false;
  }
  return true;
}

bool
test_interface__msg__VideoLogMsg__copy(
  const test_interface__msg__VideoLogMsg * input,
  test_interface__msg__VideoLogMsg * output)
{
  if (!input || !output) {
    return false;
  }
  // isturning
  output->isturning = input->isturning;
  // refer
  output->refer = input->refer;
  // obj_list
  if (!test_interface__msg__ObjectMsg__Sequence__copy(
      &(input->obj_list), &(output->obj_list)))
  {
    return false;
  }
  // linear
  output->linear = input->linear;
  // angular
  output->angular = input->angular;
  return true;
}

test_interface__msg__VideoLogMsg *
test_interface__msg__VideoLogMsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__VideoLogMsg * msg = (test_interface__msg__VideoLogMsg *)allocator.allocate(sizeof(test_interface__msg__VideoLogMsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_interface__msg__VideoLogMsg));
  bool success = test_interface__msg__VideoLogMsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
test_interface__msg__VideoLogMsg__destroy(test_interface__msg__VideoLogMsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    test_interface__msg__VideoLogMsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
test_interface__msg__VideoLogMsg__Sequence__init(test_interface__msg__VideoLogMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__VideoLogMsg * data = NULL;

  if (size) {
    data = (test_interface__msg__VideoLogMsg *)allocator.zero_allocate(size, sizeof(test_interface__msg__VideoLogMsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_interface__msg__VideoLogMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_interface__msg__VideoLogMsg__fini(&data[i - 1]);
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
test_interface__msg__VideoLogMsg__Sequence__fini(test_interface__msg__VideoLogMsg__Sequence * array)
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
      test_interface__msg__VideoLogMsg__fini(&array->data[i]);
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

test_interface__msg__VideoLogMsg__Sequence *
test_interface__msg__VideoLogMsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__VideoLogMsg__Sequence * array = (test_interface__msg__VideoLogMsg__Sequence *)allocator.allocate(sizeof(test_interface__msg__VideoLogMsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = test_interface__msg__VideoLogMsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
test_interface__msg__VideoLogMsg__Sequence__destroy(test_interface__msg__VideoLogMsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    test_interface__msg__VideoLogMsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
test_interface__msg__VideoLogMsg__Sequence__are_equal(const test_interface__msg__VideoLogMsg__Sequence * lhs, const test_interface__msg__VideoLogMsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!test_interface__msg__VideoLogMsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
test_interface__msg__VideoLogMsg__Sequence__copy(
  const test_interface__msg__VideoLogMsg__Sequence * input,
  test_interface__msg__VideoLogMsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(test_interface__msg__VideoLogMsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    test_interface__msg__VideoLogMsg * data =
      (test_interface__msg__VideoLogMsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!test_interface__msg__VideoLogMsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          test_interface__msg__VideoLogMsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!test_interface__msg__VideoLogMsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
