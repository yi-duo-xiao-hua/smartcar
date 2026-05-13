// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from test_interface:msg/ResnetMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__TRAITS_HPP_
#define TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "test_interface/msg/detail/resnet_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace test_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const ResnetMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: line_x
  {
    out << "line_x: ";
    rosidl_generator_traits::value_to_yaml(msg.line_x, out);
    out << ", ";
  }

  // member: line_y
  {
    out << "line_y: ";
    rosidl_generator_traits::value_to_yaml(msg.line_y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ResnetMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: line_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "line_x: ";
    rosidl_generator_traits::value_to_yaml(msg.line_x, out);
    out << "\n";
  }

  // member: line_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "line_y: ";
    rosidl_generator_traits::value_to_yaml(msg.line_y, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ResnetMsg & msg, bool use_flow_style = false)
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
  const test_interface::msg::ResnetMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  test_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use test_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const test_interface::msg::ResnetMsg & msg)
{
  return test_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<test_interface::msg::ResnetMsg>()
{
  return "test_interface::msg::ResnetMsg";
}

template<>
inline const char * name<test_interface::msg::ResnetMsg>()
{
  return "test_interface/msg/ResnetMsg";
}

template<>
struct has_fixed_size<test_interface::msg::ResnetMsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<test_interface::msg::ResnetMsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<test_interface::msg::ResnetMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TEST_INTERFACE__MSG__DETAIL__RESNET_MSG__TRAITS_HPP_
