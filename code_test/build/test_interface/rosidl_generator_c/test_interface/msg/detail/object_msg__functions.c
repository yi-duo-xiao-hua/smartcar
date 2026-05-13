// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from test_interface:msg/ObjectMsg.idl
// generated code does not contain a copyright notice
#include "test_interface/msg/detail/object_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `obj_type`
#include "rosidl_runtime_c/string_functions.h"

bool
test_interface__msg__ObjectMsg__init(test_interface__msg__ObjectMsg * msg)
{
  if (!msg) {
    return false;
  }
  // obj_type
  if (!rosidl_runtime_c__String__init(&msg->obj_type)) {
    test_interface__msg__ObjectMsg__fini(msg);
    return false;
  }
  // xl
  // xr
  // yu
  // yd
  // distance
  return true;
}

void
test_interface__msg__ObjectMsg__fini(test_interface__msg__ObjectMsg * msg)
{
  if (!msg) {
    return;
  }
  // obj_type
  rosidl_runtime_c__String__fini(&msg->obj_type);
  // xl
  // xr
  // yu
  // yd
  // distance
}

bool
test_interface__msg__ObjectMsg__are_equal(const test_interface__msg__ObjectMsg * lhs, const test_interface__msg__ObjectMsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // obj_type
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->obj_type), &(rhs->obj_type)))
  {
    return false;
  }
  // xl
  if (lhs->xl != rhs->xl) {
    return false;
  }
  // xr
  if (lhs->xr != rhs->xr) {
    return false;
  }
  // yu
  if (lhs->yu != rhs->yu) {
    return false;
  }
  // yd
  if (lhs->yd != rhs->yd) {
    return false;
  }
  // distance
  if (lhs->distance != rhs->distance) {
    return false;
  }
  return true;
}

bool
test_interface__msg__ObjectMsg__copy(
  const test_interface__msg__ObjectMsg * input,
  test_interface__msg__ObjectMsg * output)
{
  if (!input || !output) {
    return false;
  }
  // obj_type
  if (!rosidl_runtime_c__String__copy(
      &(input->obj_type), &(output->obj_type)))
  {
    return false;
  }
  // xl
  output->xl = input->xl;
  // xr
  output->xr = input->xr;
  // yu
  output->yu = input->yu;
  // yd
  output->yd = input->yd;
  // distance
  output->distance = input->distance;
  return true;
}

test_interface__msg__ObjectMsg *
test_interface__msg__ObjectMsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__ObjectMsg * msg = (test_interface__msg__ObjectMsg *)allocator.allocate(sizeof(test_interface__msg__ObjectMsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_interface__msg__ObjectMsg));
  bool success = test_interface__msg__ObjectMsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
test_interface__msg__ObjectMsg__destroy(test_interface__msg__ObjectMsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    test_interface__msg__ObjectMsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
test_interface__msg__ObjectMsg__Sequence__init(test_interface__msg__ObjectMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__ObjectMsg * data = NULL;

  if (size) {
    data = (test_interface__msg__ObjectMsg *)allocator.zero_allocate(size, sizeof(test_interface__msg__ObjectMsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_interface__msg__ObjectMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_interface__msg__ObjectMsg__fini(&data[i - 1]);
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
test_interface__msg__ObjectMsg__Sequence__fini(test_interface__msg__ObjectMsg__Sequence * array)
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
      test_interface__msg__ObjectMsg__fini(&array->data[i]);
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

test_interface__msg__ObjectMsg__Sequence *
test_interface__msg__ObjectMsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interface__msg__ObjectMsg__Sequence * array = (test_interface__msg__ObjectMsg__Sequence *)allocator.allocate(sizeof(test_interface__msg__ObjectMsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = test_interface__msg__ObjectMsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
test_interface__msg__ObjectMsg__Sequence__destroy(test_interface__msg__ObjectMsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    test_interface__msg__ObjectMsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
test_interface__msg__ObjectMsg__Sequence__are_equal(const test_interface__msg__ObjectMsg__Sequence * lhs, const test_interface__msg__ObjectMsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!test_interface__msg__ObjectMsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
test_interface__msg__ObjectMsg__Sequence__copy(
  const test_interface__msg__ObjectMsg__Sequence * input,
  test_interface__msg__ObjectMsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(test_interface__msg__ObjectMsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    test_interface__msg__ObjectMsg * data =
      (test_interface__msg__ObjectMsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!test_interface__msg__ObjectMsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          test_interface__msg__ObjectMsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!test_interface__msg__ObjectMsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
