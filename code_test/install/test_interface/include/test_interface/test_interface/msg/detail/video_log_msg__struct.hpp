// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from test_interface:msg/VideoLogMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__STRUCT_HPP_
#define TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'obj_list'
#include "test_interface/msg/detail/object_msg__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__test_interface__msg__VideoLogMsg __attribute__((deprecated))
#else
# define DEPRECATED__test_interface__msg__VideoLogMsg __declspec(deprecated)
#endif

namespace test_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct VideoLogMsg_
{
  using Type = VideoLogMsg_<ContainerAllocator>;

  explicit VideoLogMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->isturning = false;
      this->refer = 0.0f;
      this->linear = 0.0f;
      this->angular = 0.0f;
    }
  }

  explicit VideoLogMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->isturning = false;
      this->refer = 0.0f;
      this->linear = 0.0f;
      this->angular = 0.0f;
    }
  }

  // field types and members
  using _isturning_type =
    bool;
  _isturning_type isturning;
  using _refer_type =
    float;
  _refer_type refer;
  using _obj_list_type =
    std::vector<test_interface::msg::ObjectMsg_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<test_interface::msg::ObjectMsg_<ContainerAllocator>>>;
  _obj_list_type obj_list;
  using _linear_type =
    float;
  _linear_type linear;
  using _angular_type =
    float;
  _angular_type angular;

  // setters for named parameter idiom
  Type & set__isturning(
    const bool & _arg)
  {
    this->isturning = _arg;
    return *this;
  }
  Type & set__refer(
    const float & _arg)
  {
    this->refer = _arg;
    return *this;
  }
  Type & set__obj_list(
    const std::vector<test_interface::msg::ObjectMsg_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<test_interface::msg::ObjectMsg_<ContainerAllocator>>> & _arg)
  {
    this->obj_list = _arg;
    return *this;
  }
  Type & set__linear(
    const float & _arg)
  {
    this->linear = _arg;
    return *this;
  }
  Type & set__angular(
    const float & _arg)
  {
    this->angular = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    test_interface::msg::VideoLogMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const test_interface::msg::VideoLogMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<test_interface::msg::VideoLogMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<test_interface::msg::VideoLogMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      test_interface::msg::VideoLogMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<test_interface::msg::VideoLogMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      test_interface::msg::VideoLogMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<test_interface::msg::VideoLogMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<test_interface::msg::VideoLogMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<test_interface::msg::VideoLogMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__test_interface__msg__VideoLogMsg
    std::shared_ptr<test_interface::msg::VideoLogMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__test_interface__msg__VideoLogMsg
    std::shared_ptr<test_interface::msg::VideoLogMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const VideoLogMsg_ & other) const
  {
    if (this->isturning != other.isturning) {
      return false;
    }
    if (this->refer != other.refer) {
      return false;
    }
    if (this->obj_list != other.obj_list) {
      return false;
    }
    if (this->linear != other.linear) {
      return false;
    }
    if (this->angular != other.angular) {
      return false;
    }
    return true;
  }
  bool operator!=(const VideoLogMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct VideoLogMsg_

// alias to use template instance with default allocator
using VideoLogMsg =
  test_interface::msg::VideoLogMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace test_interface

#endif  // TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__STRUCT_HPP_
