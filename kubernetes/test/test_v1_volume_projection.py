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
from kubernetes.client.models.v1_volume_projection import V1VolumeProjection


class TestV1VolumeProjection(unittest.TestCase):
    """ V1VolumeProjection unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1VolumeProjection(self):
        """
        Test V1VolumeProjection
        """
        model = kubernetes.client.models.v1_volume_projection.V1VolumeProjection()


if __name__ == '__main__':
    unittest.main()
