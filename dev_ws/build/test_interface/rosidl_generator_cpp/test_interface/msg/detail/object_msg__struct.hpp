// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from test_interface:msg/ObjectMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__STRUCT_HPP_
#define TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__test_interface__msg__ObjectMsg __attribute__((deprecated))
#else
# define DEPRECATED__test_interface__msg__ObjectMsg __declspec(deprecated)
#endif

namespace test_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ObjectMsg_
{
  using Type = ObjectMsg_<ContainerAllocator>;

  explicit ObjectMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->obj_type = "";
      this->xl = 0l;
      this->xr = 0l;
      this->yu = 0l;
      this->yd = 0l;
      this->distance = 0l;
    }
  }

  explicit ObjectMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : obj_type(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->obj_type = "";
      this->xl = 0l;
      this->xr = 0l;
      this->yu = 0l;
      this->yd = 0l;
      this->distance = 0l;
    }
  }

  // field types and members
  using _obj_type_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _obj_type_type obj_type;
  using _xl_type =
    int32_t;
  _xl_type xl;
  using _xr_type =
    int32_t;
  _xr_type xr;
  using _yu_type =
    int32_t;
  _yu_type yu;
  using _yd_type =
    int32_t;
  _yd_type yd;
  using _distance_type =
    int32_t;
  _distance_type distance;

  // setters for named parameter idiom
  Type & set__obj_type(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->obj_type = _arg;
    return *this;
  }
  Type & set__xl(
    const int32_t & _arg)
  {
    this->xl = _arg;
    return *this;
  }
  Type & set__xr(
    const int32_t & _arg)
  {
    this->xr = _arg;
    return *this;
  }
  Type & set__yu(
    const int32_t & _arg)
  {
    this->yu = _arg;
    return *this;
  }
  Type & set__yd(
    const int32_t & _arg)
  {
    this->yd = _arg;
    return *this;
  }
  Type & set__distance(
    const int32_t & _arg)
  {
    this->distance = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    test_interface::msg::ObjectMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const test_interface::msg::ObjectMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<test_interface::msg::ObjectMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<test_interface::msg::ObjectMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      test_interface::msg::ObjectMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<test_interface::msg::ObjectMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      test_interface::msg::ObjectMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<test_interface::msg::ObjectMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<test_interface::msg::ObjectMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<test_interface::msg::ObjectMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__test_interface__msg__ObjectMsg
    std::shared_ptr<test_interface::msg::ObjectMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__test_interface__msg__ObjectMsg
    std::shared_ptr<test_interface::msg::ObjectMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ObjectMsg_ & other) const
  {
    if (this->obj_type != other.obj_type) {
      return false;
    }
    if (this->xl != other.xl) {
      return false;
    }
    if (this->xr != other.xr) {
      return false;
    }
    if (this->yu != other.yu) {
      return false;
    }
    if (this->yd != other.yd) {
      return false;
    }
    if (this->distance != other.distance) {
      return false;
    }
    return true;
  }
  bool operator!=(const ObjectMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ObjectMsg_

// alias to use template instance with default allocator
using ObjectMsg =
  test_interface::msg::ObjectMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace test_interface

#endif  // TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__STRUCT_HPP_
