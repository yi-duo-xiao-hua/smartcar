// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from test_interface:msg/VideoLogMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__BUILDER_HPP_
#define TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "test_interface/msg/detail/video_log_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace test_interface
{

namespace msg
{

namespace builder
{

class Init_VideoLogMsg_angular
{
public:
  explicit Init_VideoLogMsg_angular(::test_interface::msg::VideoLogMsg & msg)
  : msg_(msg)
  {}
  ::test_interface::msg::VideoLogMsg angular(::test_interface::msg::VideoLogMsg::_angular_type arg)
  {
    msg_.angular = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_interface::msg::VideoLogMsg msg_;
};

class Init_VideoLogMsg_linear
{
public:
  explicit Init_VideoLogMsg_linear(::test_interface::msg::VideoLogMsg & msg)
  : msg_(msg)
  {}
  Init_VideoLogMsg_angular linear(::test_interface::msg::VideoLogMsg::_linear_type arg)
  {
    msg_.linear = std::move(arg);
    return Init_VideoLogMsg_angular(msg_);
  }

private:
  ::test_interface::msg::VideoLogMsg msg_;
};

class Init_VideoLogMsg_obj_list
{
public:
  explicit Init_VideoLogMsg_obj_list(::test_interface::msg::VideoLogMsg & msg)
  : msg_(msg)
  {}
  Init_VideoLogMsg_linear obj_list(::test_interface::msg::VideoLogMsg::_obj_list_type arg)
  {
    msg_.obj_list = std::move(arg);
    return Init_VideoLogMsg_linear(msg_);
  }

private:
  ::test_interface::msg::VideoLogMsg msg_;
};

class Init_VideoLogMsg_refer
{
public:
  explicit Init_VideoLogMsg_refer(::test_interface::msg::VideoLogMsg & msg)
  : msg_(msg)
  {}
  Init_VideoLogMsg_obj_list refer(::test_interface::msg::VideoLogMsg::_refer_type arg)
  {
    msg_.refer = std::move(arg);
    return Init_VideoLogMsg_obj_list(msg_);
  }

private:
  ::test_interface::msg::VideoLogMsg msg_;
};

class Init_VideoLogMsg_isturning
{
public:
  Init_VideoLogMsg_isturning()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_VideoLogMsg_refer isturning(::test_interface::msg::VideoLogMsg::_isturning_type arg)
  {
    msg_.isturning = std::move(arg);
    return Init_VideoLogMsg_refer(msg_);
  }

private:
  ::test_interface::msg::VideoLogMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_interface::msg::VideoLogMsg>()
{
  return test_interface::msg::builder::Init_VideoLogMsg_isturning();
}

}  // namespace test_interface

#endif  // TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__BUILDER_HPP_
