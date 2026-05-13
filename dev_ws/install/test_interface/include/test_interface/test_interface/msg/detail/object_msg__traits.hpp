// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from test_interface:msg/ObjectMsg.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__TRAITS_HPP_
#define TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "test_interface/msg/detail/object_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace test_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const ObjectMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: obj_type
  {
    out << "obj_type: ";
    rosidl_generator_traits::value_to_yaml(msg.obj_type, out);
    out << ", ";
  }

  // member: xl
  {
    out << "xl: ";
    rosidl_generator_traits::value_to_yaml(msg.xl, out);
    out << ", ";
  }

  // member: xr
  {
    out << "xr: ";
    rosidl_generator_traits::value_to_yaml(msg.xr, out);
    out << ", ";
  }

  // member: yu
  {
    out << "yu: ";
    rosidl_generator_traits::value_to_yaml(msg.yu, out);
    out << ", ";
  }

  // member: yd
  {
    out << "yd: ";
    rosidl_generator_traits::value_to_yaml(msg.yd, out);
    out << ", ";
  }

  // member: distance
  {
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ObjectMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: obj_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "obj_type: ";
    rosidl_generator_traits::value_to_yaml(msg.obj_type, out);
    out << "\n";
  }

  // member: xl
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "xl: ";
    rosidl_generator_traits::value_to_yaml(msg.xl, out);
    out << "\n";
  }

  // member: xr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "xr: ";
    rosidl_generator_traits::value_to_yaml(msg.xr, out);
    out << "\n";
  }

  // member: yu
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yu: ";
    rosidl_generator_traits::value_to_yaml(msg.yu, out);
    out << "\n";
  }

  // member: yd
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yd: ";
    rosidl_generator_traits::value_to_yaml(msg.yd, out);
    out << "\n";
  }

  // member: distance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ObjectMsg & msg, bool use_flow_style = false)
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
  const test_interface::msg::ObjectMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  test_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use test_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const test_interface::msg::ObjectMsg & msg)
{
  return test_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<test_interface::msg::ObjectMsg>()
{
  return "test_interface::msg::ObjectMsg";
}

template<>
inline const char * name<test_interface::msg::ObjectMsg>()
{
  return "test_interface/msg/ObjectMsg";
}

template<>
struct has_fixed_size<test_interface::msg::ObjectMsg>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<test_interface::msg::ObjectMsg>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<test_interface::msg::ObjectMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TEST_INTERFACE__MSG__DETAIL__OBJECT_MSG__TRAITS_HPP_
