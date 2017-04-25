# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1VolumeMount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, mount_path=None, name=None, read_only=None, sub_path=None):
        """
        V1VolumeMount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'mount_path': 'str',
            'name': 'str',
            'read_only': 'bool',
            'sub_path': 'str'
        }

        self.attribute_map = {
            'mount_path': 'mountPath',
            'name': 'name',
            'read_only': 'readOnly',
            'sub_path': 'subPath'
        }

        self._mount_path = mount_path
        self._name = name
        self._read_only = read_only
        self._sub_path = sub_path

    @property
    def mount_path(self):
        """
        Gets the mount_path of this V1VolumeMount.
        Path within the container at which the volume should be mounted.  Must not contain ':'.

        :return: The mount_path of this V1VolumeMount.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """
        Sets the mount_path of this V1VolumeMount.
        Path within the container at which the volume should be mounted.  Must not contain ':'.

        :param mount_path: The mount_path of this V1VolumeMount.
        :type: str
        """
        if mount_path is None:
            raise ValueError("Invalid value for `mount_path`, must not be `None`")

        self._mount_path = mount_path

    @property
    def name(self):
        """
        Gets the name of this V1VolumeMount.
        This must match the Name of a Volume.

        :return: The name of this V1VolumeMount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1VolumeMount.
        This must match the Name of a Volume.

        :param name: The name of this V1VolumeMount.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def read_only(self):
        """
        Gets the read_only of this V1VolumeMount.
        Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.

        :return: The read_only of this V1VolumeMount.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1VolumeMount.
        Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.

        :param read_only: The read_only of this V1VolumeMount.
        :type: bool
        """

        self._read_only = read_only

    @property
    def sub_path(self):
        """
        Gets the sub_path of this V1VolumeMount.
        Path within the volume from which the container's volume should be mounted. Defaults to \"\" (volume's root).

        :return: The sub_path of this V1VolumeMount.
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """
        Sets the sub_path of this V1VolumeMount.
        Path within the volume from which the container's volume should be mounted. Defaults to \"\" (volume's root).

        :param sub_path: The sub_path of this V1VolumeMount.
        :type: str
        """

        self._sub_path = sub_path

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
