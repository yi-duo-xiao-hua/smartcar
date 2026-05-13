// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from test_interface:msg/ObjPosition.idl
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
#include "test_interface/msg/detail/obj_position__struct.h"
#include "test_interface/msg/detail/obj_position__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool test_interface__msg__obj_position__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[45];
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
    assert(strncmp("test_interface.msg._obj_position.ObjPosition", full_classname_dest, 44) == 0);
  }
  test_interface__msg__ObjPosition * ros_message = _ros_message;
  {  // x
    PyObject * field = PyObject_GetAttrString(_pymsg, "x");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->x = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // x_left
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_left");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->x_left = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // x_right
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_right");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->x_right = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // area
    PyObject * field = PyObject_GetAttrString(_pymsg, "area");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->area = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // y
    PyObject * field = PyObject_GetAttrString(_pymsg, "y");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->y = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // y_up
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_up");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->y_up = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // y_down
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_down");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->y_down = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * test_interface__msg__obj_position__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ObjPosition */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("test_interface.msg._obj_position");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ObjPosition");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  test_interface__msg__ObjPosition * ros_message = (test_interface__msg__ObjPosition *)raw_ros_message;
  {  // x
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x_left
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->x_left);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_left", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x_right
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->x_right);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_right", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // area
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->area);
    {
      int rc = PyObject_SetAttrString(_pymessage, "area", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_up
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->y_up);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_up", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_down
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->y_down);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_down", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
