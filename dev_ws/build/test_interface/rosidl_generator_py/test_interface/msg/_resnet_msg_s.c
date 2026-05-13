// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from test_interface:msg/ResnetMsg.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "test_interface/msg/detail/resnet_msg__struct.h"
#include "test_interface/msg/detail/resnet_msg__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool test_interface__msg__resnet_msg__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[41];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("test_interface.msg._resnet_msg.ResnetMsg", full_classname_dest, 40) == 0);
  }
  test_interface__msg__ResnetMsg * ros_message = _ros_message;
  {  // line_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "line_x");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->line_x = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // line_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "line_y");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->line_y = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * test_interface__msg__resnet_msg__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ResnetMsg */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("test_interface.msg._resnet_msg");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ResnetMsg");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  test_interface__msg__ResnetMsg * ros_message = (test_interface__msg__ResnetMsg *)raw_ros_message;
  {  // line_x
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->line_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "line_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // line_y
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->line_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "line_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
