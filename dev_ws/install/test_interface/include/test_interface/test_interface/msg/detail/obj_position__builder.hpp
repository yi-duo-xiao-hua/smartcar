// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from test_interface:msg/ObjPosition.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__BUILDER_HPP_
#define TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "test_interface/msg/detail/obj_position__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace test_interface
{

namespace msg
{

namespace builder
{

class Init_ObjPosition_y_down
{
public:
  explicit Init_ObjPosition_y_down(::test_interface::msg::ObjPosition & msg)
  : msg_(msg)
  {}
  ::test_interface::msg::ObjPosition y_down(::test_interface::msg::ObjPosition::_y_down_type arg)
  {
    msg_.y_down = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_interface::msg::ObjPosition msg_;
};

class Init_ObjPosition_y_up
{
public:
  explicit Init_ObjPosition_y_up(::test_interface::msg::ObjPosition & msg)
  : msg_(msg)
  {}
  Init_ObjPosition_y_down y_up(::test_interface::msg::ObjPosition::_y_up_type arg)
  {
    msg_.y_up = std::move(arg);
    return Init_ObjPosition_y_down(msg_);
  }

private:
  ::test_interface::msg::ObjPosition msg_;
};

class Init_ObjPosition_y
{
public:
  explicit Init_ObjPosition_y(::test_interface::msg::ObjPosition & msg)
  : msg_(msg)
  {}
  Init_ObjPosition_y_up y(::test_interface::msg::ObjPosition::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_ObjPosition_y_up(msg_);
  }

private:
  ::test_interface::msg::ObjPosition msg_;
};

class Init_ObjPosition_area
{
public:
  explicit Init_ObjPosition_area(::test_interface::msg::ObjPosition & msg)
  : msg_(msg)
  {}
  Init_ObjPosition_y area(::test_interface::msg::ObjPosition::_area_type arg)
  {
    msg_.area = std::move(arg);
    return Init_ObjPosition_y(msg_);
  }

private:
  ::test_interface::msg::ObjPosition msg_;
};

class Init_ObjPosition_x_right
{
public:
  explicit Init_ObjPosition_x_right(::test_interface::msg::ObjPosition & msg)
  : msg_(msg)
  {}
  Init_ObjPosition_area x_right(::test_interface::msg::ObjPosition::_x_right_type arg)
  {
    msg_.x_right = std::move(arg);
    return Init_ObjPosition_area(msg_);
  }

private:
  ::test_interface::msg::ObjPosition msg_;
};

class Init_ObjPosition_x_left
{
public:
  explicit Init_ObjPosition_x_left(::test_interface::msg::ObjPosition & msg)
  : msg_(msg)
  {}
  Init_ObjPosition_x_right x_left(::test_interface::msg::ObjPosition::_x_left_type arg)
  {
    msg_.x_left = std::move(arg);
    return Init_ObjPosition_x_right(msg_);
  }

private:
  ::test_interface::msg::ObjPosition msg_;
};

class Init_ObjPosition_x
{
public:
  Init_ObjPosition_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ObjPosition_x_left x(::test_interface::msg::ObjPosition::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_ObjPosition_x_left(msg_);
  }

private:
  ::test_interface::msg::ObjPosition msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_interface::msg::ObjPosition>()
{
  return test_interface::msg::builder::Init_ObjPosition_x();
}

}  // namespace test_interface

#endif  // TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__BUILDER_HPP_
