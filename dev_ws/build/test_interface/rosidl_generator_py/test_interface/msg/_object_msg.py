# generated from rosidl_generator_py/resource/_idl.py.em
# with input from test_interface:msg/ObjectMsg.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ObjectMsg(type):
    """Metaclass of message 'ObjectMsg'."""

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
                'test_interface.msg.ObjectMsg')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__object_msg
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__object_msg
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__object_msg
            cls._TYPE_SUPPORT = module.type_support_msg__msg__object_msg
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__object_msg

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ObjectMsg(metaclass=Metaclass_ObjectMsg):
    """Message class 'ObjectMsg'."""

    __slots__ = [
        '_obj_type',
        '_xl',
        '_xr',
        '_yu',
        '_yd',
        '_distance',
    ]

    _fields_and_field_types = {
        'obj_type': 'string',
        'xl': 'int32',
        'xr': 'int32',
        'yu': 'int32',
        'yd': 'int32',
        'distance': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.obj_type = kwargs.get('obj_type', str())
        self.xl = kwargs.get('xl', int())
        self.xr = kwargs.get('xr', int())
        self.yu = kwargs.get('yu', int())
        self.yd = kwargs.get('yd', int())
        self.distance = kwargs.get('distance', int())

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
        if self.obj_type != other.obj_type:
            return False
        if self.xl != other.xl:
            return False
        if self.xr != other.xr:
            return False
        if self.yu != other.yu:
            return False
        if self.yd != other.yd:
            return False
        if self.distance != other.distance:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def obj_type(self):
        """Message field 'obj_type'."""
        return self._obj_type

    @obj_type.setter
    def obj_type(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'obj_type' field must be of type 'str'"
        self._obj_type = value

    @builtins.property
    def xl(self):
        """Message field 'xl'."""
        return self._xl

    @xl.setter
    def xl(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'xl' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'xl' field must be an integer in [-2147483648, 2147483647]"
        self._xl = value

    @builtins.property
    def xr(self):
        """Message field 'xr'."""
        return self._xr

    @xr.setter
    def xr(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'xr' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'xr' field must be an integer in [-2147483648, 2147483647]"
        self._xr = value

    @builtins.property
    def yu(self):
        """Message field 'yu'."""
        return self._yu

    @yu.setter
    def yu(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'yu' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'yu' field must be an integer in [-2147483648, 2147483647]"
        self._yu = value

    @builtins.property
    def yd(self):
        """Message field 'yd'."""
        return self._yd

    @yd.setter
    def yd(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'yd' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'yd' field must be an integer in [-2147483648, 2147483647]"
        self._yd = value

    @builtins.property
    def distance(self):
        """Message field 'distance'."""
        return self._distance

    @distance.setter
    def distance(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'distance' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'distance' field must be an integer in [-2147483648, 2147483647]"
        self._distance = value
