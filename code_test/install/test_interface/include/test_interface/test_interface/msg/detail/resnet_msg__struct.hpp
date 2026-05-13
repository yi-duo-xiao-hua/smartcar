// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from test_interface:msg/ResnetMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__STRUCT_HPP_
#define TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__test_interface__msg__ResnetMsg __attribute__((deprecated))
#else
# define DEPRECATED__test_interface__msg__ResnetMsg __declspec(deprecated)
#endif

namespace test_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ResnetMsg_
{
  using Type = ResnetMsg_<ContainerAllocator>;

  explicit ResnetMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->line_x = 0l;
      this->line_y = 0l;
    }
  }

  explicit ResnetMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->line_x = 0l;
      this->line_y = 0l;
    }
  }

  // field types and members
  using _line_x_type =
    int32_t;
  _line_x_type line_x;
  using _line_y_type =
    int32_t;
  _line_y_type line_y;

  // setters for named parameter idiom
  Type & set__line_x(
    const int32_t & _arg)
  {
    this->line_x = _arg;
    return *this;
  }
  Type & set__line_y(
    const int32_t & _arg)
  {
    this->line_y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    test_interface::msg::ResnetMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const test_interface::msg::ResnetMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<test_interface::msg::ResnetMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<test_interface::msg::ResnetMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      test_interface::msg::ResnetMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<test_interface::msg::ResnetMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      test_interface::msg::ResnetMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<test_interface::msg::ResnetMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<test_interface::msg::ResnetMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<test_interface::msg::ResnetMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__test_interface__msg__ResnetMsg
    std::shared_ptr<test_interface::msg::ResnetMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__test_interface__msg__ResnetMsg
    std::shared_ptr<test_interface::msg::ResnetMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ResnetMsg_ & other) const
  {
    if (this->line_x != other.line_x) {
      return false;
    }
    if (this->line_y != other.line_y) {
      return false;
    }
    return true;
  }
  bool operator!=(const ResnetMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ResnetMsg_

// alias to use template instance with default allocator
using ResnetMsg =
  test_interface::msg::ResnetMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace test_interface

#endif  // TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__STRUCT_HPP_
