# coding: utf-8

"""
    WebScraping.AI

    A client for https://webscraping.ai API. It provides a web scaping automation API with Chrome JS rendering, rotating proxies and builtin HTML parsing.  # noqa: E501

    The version of the OpenAPI document: 2.0.2
    Contact: support@webscraping.ai
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from webscraping_ai.configuration import Configuration


class PageError(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status_code': 'int',
        'status_message': 'str'
    }

    attribute_map = {
        'status_code': 'status_code',
        'status_message': 'status_message'
    }

    def __init__(self, status_code=None, status_message=None, local_vars_configuration=None):  # noqa: E501
        """PageError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status_code = None
        self._status_message = None
        self.discriminator = None

        if status_code is not None:
            self.status_code = status_code
        if status_message is not None:
            self.status_message = status_message

    @property
    def status_code(self):
        """Gets the status_code of this PageError.  # noqa: E501

        Response HTTP status code (403, 500, etc)  # noqa: E501

        :return: The status_code of this PageError.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this PageError.

        Response HTTP status code (403, 500, etc)  # noqa: E501

        :param status_code: The status_code of this PageError.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def status_message(self):
        """Gets the status_message of this PageError.  # noqa: E501

        Response HTTP status message  # noqa: E501

        :return: The status_message of this PageError.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this PageError.

        Response HTTP status message  # noqa: E501

        :param status_message: The status_message of this PageError.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PageError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageError):
            return True

        return self.to_dict() != other.to_dict()
