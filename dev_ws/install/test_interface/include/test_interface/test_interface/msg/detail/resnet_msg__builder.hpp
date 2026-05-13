// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from test_interface:msg/ResnetMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__BUILDER_HPP_
#define TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "test_interface/msg/detail/resnet_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace test_interface
{

namespace msg
{

namespace builder
{

class Init_ResnetMsg_line_y
{
public:
  explicit Init_ResnetMsg_line_y(::test_interface::msg::ResnetMsg & msg)
  : msg_(msg)
  {}
  ::test_interface::msg::ResnetMsg line_y(::test_interface::msg::ResnetMsg::_line_y_type arg)
  {
    msg_.line_y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_interface::msg::ResnetMsg msg_;
};

class Init_ResnetMsg_line_x
{
public:
  Init_ResnetMsg_line_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ResnetMsg_line_y line_x(::test_interface::msg::ResnetMsg::_line_x_type arg)
  {
    msg_.line_x = std::move(arg);
    return Init_ResnetMsg_line_y(msg_);
  }

private:
  ::test_interface::msg::ResnetMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_interface::msg::ResnetMsg>()
{
  return test_interface::msg::builder::Init_ResnetMsg_line_x();
}

}  // namespace test_interface

#endif  // TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__BUILDER_HPP_
