# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_third_party_resource import V1beta1ThirdPartyResource


class TestV1beta1ThirdPartyResource(unittest.TestCase):
    """ V1beta1ThirdPartyResource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1ThirdPartyResource(self):
        """
        Test V1beta1ThirdPartyResource
        """
        model = kubernetes.client.models.v1beta1_third_party_resource.V1beta1ThirdPartyResource()


if __name__ == '__main__':
    unittest.main()
