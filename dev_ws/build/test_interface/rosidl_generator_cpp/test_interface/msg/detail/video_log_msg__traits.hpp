// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from test_interface:msg/VideoLogMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__TRAITS_HPP_
#define TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "test_interface/msg/detail/video_log_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'obj_list'
#include "test_interface/msg/detail/object_msg__traits.hpp"

namespace test_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const VideoLogMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: isturning
  {
    out << "isturning: ";
    rosidl_generator_traits::value_to_yaml(msg.isturning, out);
    out << ", ";
  }

  // member: refer
  {
    out << "refer: ";
    rosidl_generator_traits::value_to_yaml(msg.refer, out);
    out << ", ";
  }

  // member: obj_list
  {
    if (msg.obj_list.size() == 0) {
      out << "obj_list: []";
    } else {
      out << "obj_list: [";
      size_t pending_items = msg.obj_list.size();
      for (auto item : msg.obj_list) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: linear
  {
    out << "linear: ";
    rosidl_generator_traits::value_to_yaml(msg.linear, out);
    out << ", ";
  }

  // member: angular
  {
    out << "angular: ";
    rosidl_generator_traits::value_to_yaml(msg.angular, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const VideoLogMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: isturning
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "isturning: ";
    rosidl_generator_traits::value_to_yaml(msg.isturning, out);
    out << "\n";
  }

  // member: refer
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "refer: ";
    rosidl_generator_traits::value_to_yaml(msg.refer, out);
    out << "\n";
  }

  // member: obj_list
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.obj_list.size() == 0) {
      out << "obj_list: []\n";
    } else {
      out << "obj_list:\n";
      for (auto item : msg.obj_list) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: linear
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "linear: ";
    rosidl_generator_traits::value_to_yaml(msg.linear, out);
    out << "\n";
  }

  // member: angular
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angular: ";
    rosidl_generator_traits::value_to_yaml(msg.angular, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const VideoLogMsg & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace test_interface

namespace rosidl_generator_traits
{

[[deprecated("use test_interface::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const test_interface::msg::VideoLogMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  test_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use test_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const test_interface::msg::VideoLogMsg & msg)
{
  return test_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<test_interface::msg::VideoLogMsg>()
{
  return "test_interface::msg::VideoLogMsg";
}

template<>
inline const char * name<test_interface::msg::VideoLogMsg>()
{
  return "test_interface/msg/VideoLogMsg";
}

template<>
struct has_fixed_size<test_interface::msg::VideoLogMsg>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<test_interface::msg::VideoLogMsg>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<test_interface::msg::VideoLogMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TEST_INTERFACE__MSG__DETAIL__VIDEO_LOG_MSG__TRAITS_HPP_
