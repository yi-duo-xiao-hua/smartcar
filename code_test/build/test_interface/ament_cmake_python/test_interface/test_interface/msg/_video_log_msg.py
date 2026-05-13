# generated from rosidl_generator_py/resource/_idl.py.em
# with input from test_interface:msg/VideoLogMsg.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_VideoLogMsg(type):
    """Metaclass of message 'VideoLogMsg'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('test_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'test_interface.msg.VideoLogMsg')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__video_log_msg
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__video_log_msg
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__video_log_msg
            cls._TYPE_SUPPORT = module.type_support_msg__msg__video_log_msg
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__video_log_msg

            from test_interface.msg import ObjectMsg
            if ObjectMsg.__class__._TYPE_SUPPORT is None:
                ObjectMsg.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class VideoLogMsg(metaclass=Metaclass_VideoLogMsg):
    """Message class 'VideoLogMsg'."""

    __slots__ = [
        '_isturning',
        '_refer',
        '_obj_list',
        '_linear',
        '_angular',
    ]

    _fields_and_field_types = {
        'isturning': 'boolean',
        'refer': 'float',
        'obj_list': 'sequence<test_interface/ObjectMsg>',
        'linear': 'float',
        'angular': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['test_interface', 'msg'], 'ObjectMsg')),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.isturning = kwargs.get('isturning', bool())
        self.refer = kwargs.get('refer', float())
        self.obj_list = kwargs.get('obj_list', [])
        self.linear = kwargs.get('linear', float())
        self.angular = kwargs.get('angular', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.isturning != other.isturning:
            return False
        if self.refer != other.refer:
            return False
        if self.obj_list != other.obj_list:
            return False
        if self.linear != other.linear:
            return False
        if self.angular != other.angular:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def isturning(self):
        """Message field 'isturning'."""
        return self._isturning

    @isturning.setter
    def isturning(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'isturning' field must be of type 'bool'"
        self._isturning = value

    @builtins.property
    def refer(self):
        """Message field 'refer'."""
        return self._refer

    @refer.setter
    def refer(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'refer' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'refer' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._refer = value

    @builtins.property
    def obj_list(self):
        """Message field 'obj_list'."""
        return self._obj_list

    @obj_list.setter
    def obj_list(self, value):
        if __debug__:
            from test_interface.msg import ObjectMsg
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, ObjectMsg) for v in value) and
                 True), \
                "The 'obj_list' field must be a set or sequence and each value of type 'ObjectMsg'"
        self._obj_list = value

    @builtins.property
    def linear(self):
        """Message field 'linear'."""
        return self._linear

    @linear.setter
    def linear(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'linear' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'linear' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._linear = value

    @builtins.property
    def angular(self):
        """Message field 'angular'."""
        return self._angular

    @angular.setter
    def angular(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angular' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'angular' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._angular = value
