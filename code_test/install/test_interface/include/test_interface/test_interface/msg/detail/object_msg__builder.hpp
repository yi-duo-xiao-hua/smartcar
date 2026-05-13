// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from test_interface:msg/ObjectMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__BUILDER_HPP_
#define TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "test_interface/msg/detail/object_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace test_interface
{

namespace msg
{

namespace builder
{

class Init_ObjectMsg_distance
{
public:
  explicit Init_ObjectMsg_distance(::test_interface::msg::ObjectMsg & msg)
  : msg_(msg)
  {}
  ::test_interface::msg::ObjectMsg distance(::test_interface::msg::ObjectMsg::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_interface::msg::ObjectMsg msg_;
};

class Init_ObjectMsg_yd
{
public:
  explicit Init_ObjectMsg_yd(::test_interface::msg::ObjectMsg & msg)
  : msg_(msg)
  {}
  Init_ObjectMsg_distance yd(::test_interface::msg::ObjectMsg::_yd_type arg)
  {
    msg_.yd = std::move(arg);
    return Init_ObjectMsg_distance(msg_);
  }

private:
  ::test_interface::msg::ObjectMsg msg_;
};

class Init_ObjectMsg_yu
{
public:
  explicit Init_ObjectMsg_yu(::test_interface::msg::ObjectMsg & msg)
  : msg_(msg)
  {}
  Init_ObjectMsg_yd yu(::test_interface::msg::ObjectMsg::_yu_type arg)
  {
    msg_.yu = std::move(arg);
    return Init_ObjectMsg_yd(msg_);
  }

private:
  ::test_interface::msg::ObjectMsg msg_;
};

class Init_ObjectMsg_xr
{
public:
  explicit Init_ObjectMsg_xr(::test_interface::msg::ObjectMsg & msg)
  : msg_(msg)
  {}
  Init_ObjectMsg_yu xr(::test_interface::msg::ObjectMsg::_xr_type arg)
  {
    msg_.xr = std::move(arg);
    return Init_ObjectMsg_yu(msg_);
  }

private:
  ::test_interface::msg::ObjectMsg msg_;
};

class Init_ObjectMsg_xl
{
public:
  explicit Init_ObjectMsg_xl(::test_interface::msg::ObjectMsg & msg)
  : msg_(msg)
  {}
  Init_ObjectMsg_xr xl(::test_interface::msg::ObjectMsg::_xl_type arg)
  {
    msg_.xl = std::move(arg);
    return Init_ObjectMsg_xr(msg_);
  }

private:
  ::test_interface::msg::ObjectMsg msg_;
};

class Init_ObjectMsg_obj_type
{
public:
  Init_ObjectMsg_obj_type()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ObjectMsg_xl obj_type(::test_interface::msg::ObjectMsg::_obj_type_type arg)
  {
    msg_.obj_type = std::move(arg);
    return Init_ObjectMsg_xl(msg_);
  }

private:
  ::test_interface::msg::ObjectMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_interface::msg::ObjectMsg>()
{
  return test_interface::msg::builder::Init_ObjectMsg_obj_type();
}

}  // namespace test_interface

#endif  // TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__BUILDER_HPP_
