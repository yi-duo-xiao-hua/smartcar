// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from test_interface:msg/ObjPosition.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__STRUCT_HPP_
#define TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__test_interface__msg__ObjPosition __attribute__((deprecated))
#else
# define DEPRECATED__test_interface__msg__ObjPosition __declspec(deprecated)
#endif

namespace test_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ObjPosition_
{
  using Type = ObjPosition_<ContainerAllocator>;

  explicit ObjPosition_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0l;
      this->x_left = 0l;
      this->x_right = 0l;
      this->area = 0l;
      this->y = 0l;
      this->y_up = 0l;
      this->y_down = 0l;
    }
  }

  explicit ObjPosition_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0l;
      this->x_left = 0l;
      this->x_right = 0l;
      this->area = 0l;
      this->y = 0l;
      this->y_up = 0l;
      this->y_down = 0l;
    }
  }

  // field types and members
  using _x_type =
    int32_t;
  _x_type x;
  using _x_left_type =
    int32_t;
  _x_left_type x_left;
  using _x_right_type =
    int32_t;
  _x_right_type x_right;
  using _area_type =
    int32_t;
  _area_type area;
  using _y_type =
    int32_t;
  _y_type y;
  using _y_up_type =
    int32_t;
  _y_up_type y_up;
  using _y_down_type =
    int32_t;
  _y_down_type y_down;

  // setters for named parameter idiom
  Type & set__x(
    const int32_t & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__x_left(
    const int32_t & _arg)
  {
    this->x_left = _arg;
    return *this;
  }
  Type & set__x_right(
    const int32_t & _arg)
  {
    this->x_right = _arg;
    return *this;
  }
  Type & set__area(
    const int32_t & _arg)
  {
    this->area = _arg;
    return *this;
  }
  Type & set__y(
    const int32_t & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__y_up(
    const int32_t & _arg)
  {
    this->y_up = _arg;
    return *this;
  }
  Type & set__y_down(
    const int32_t & _arg)
  {
    this->y_down = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    test_interface::msg::ObjPosition_<ContainerAllocator> *;
  using ConstRawPtr =
    const test_interface::msg::ObjPosition_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<test_interface::msg::ObjPosition_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<test_interface::msg::ObjPosition_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      test_interface::msg::ObjPosition_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<test_interface::msg::ObjPosition_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      test_interface::msg::ObjPosition_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<test_interface::msg::ObjPosition_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<test_interface::msg::ObjPosition_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<test_interface::msg::ObjPosition_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__test_interface__msg__ObjPosition
    std::shared_ptr<test_interface::msg::ObjPosition_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__test_interface__msg__ObjPosition
    std::shared_ptr<test_interface::msg::ObjPosition_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ObjPosition_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    if (this->x_left != other.x_left) {
      return false;
    }
    if (this->x_right != other.x_right) {
      return false;
    }
    if (this->area != other.area) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->y_up != other.y_up) {
      return false;
    }
    if (this->y_down != other.y_down) {
      return false;
    }
    return true;
  }
  bool operator!=(const ObjPosition_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ObjPosition_

// alias to use template instance with default allocator
using ObjPosition =
  test_interface::msg::ObjPosition_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace test_interface

#endif  // TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__STRUCT_HPP_
