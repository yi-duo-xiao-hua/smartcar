// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from test_interface:msg/ObjPosition.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__TRAITS_HPP_
#define TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "test_interface/msg/detail/obj_position__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace test_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const ObjPosition & msg,
  std::ostream & out)
{
  out << "{";
  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: x_left
  {
    out << "x_left: ";
    rosidl_generator_traits::value_to_yaml(msg.x_left, out);
    out << ", ";
  }

  // member: x_right
  {
    out << "x_right: ";
    rosidl_generator_traits::value_to_yaml(msg.x_right, out);
    out << ", ";
  }

  // member: area
  {
    out << "area: ";
    rosidl_generator_traits::value_to_yaml(msg.area, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << ", ";
  }

  // member: y_up
  {
    out << "y_up: ";
    rosidl_generator_traits::value_to_yaml(msg.y_up, out);
    out << ", ";
  }

  // member: y_down
  {
    out << "y_down: ";
    rosidl_generator_traits::value_to_yaml(msg.y_down, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ObjPosition & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: x_left
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_left: ";
    rosidl_generator_traits::value_to_yaml(msg.x_left, out);
    out << "\n";
  }

  // member: x_right
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_right: ";
    rosidl_generator_traits::value_to_yaml(msg.x_right, out);
    out << "\n";
  }

  // member: area
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "area: ";
    rosidl_generator_traits::value_to_yaml(msg.area, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }

  // member: y_up
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_up: ";
    rosidl_generator_traits::value_to_yaml(msg.y_up, out);
    out << "\n";
  }

  // member: y_down
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_down: ";
    rosidl_generator_traits::value_to_yaml(msg.y_down, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ObjPosition & msg, bool use_flow_style = false)
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
  const test_interface::msg::ObjPosition & msg,
  std::ostream & out, size_t indentation = 0)
{
  test_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use test_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const test_interface::msg::ObjPosition & msg)
{
  return test_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<test_interface::msg::ObjPosition>()
{
  return "test_interface::msg::ObjPosition";
}

template<>
inline const char * name<test_interface::msg::ObjPosition>()
{
  return "test_interface/msg/ObjPosition";
}

template<>
struct has_fixed_size<test_interface::msg::ObjPosition>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<test_interface::msg::ObjPosition>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<test_interface::msg::ObjPosition>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TEST_INTERFACE__MSG__DETAIL__OBJ_POSITION__TRAITS_HPP_
