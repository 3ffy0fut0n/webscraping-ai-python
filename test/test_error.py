# coding: utf-8

"""
    WebScraping.AI

    A client for https://webscraping.ai API. It provides a web scaping automation API with Chrome JS rendering, rotating proxies and builtin HTML parsing.  # noqa: E501

    The version of the OpenAPI document: 2.0.2
    Contact: support@webscraping.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import webscraping_ai
from webscraping_ai.models.error import Error  # noqa: E501
from webscraping_ai.rest import ApiException

class TestError(unittest.TestCase):
    """Error unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Error
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = webscraping_ai.models.error.Error()  # noqa: E501
        if include_optional :
            return Error(
                message = '0'
            )
        else :
            return Error(
        )

    def testError(self):
        """Test Error"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
