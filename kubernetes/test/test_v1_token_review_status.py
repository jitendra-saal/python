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
from kubernetes.client.models.v1_token_review_status import V1TokenReviewStatus


class TestV1TokenReviewStatus(unittest.TestCase):
    """ V1TokenReviewStatus unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1TokenReviewStatus(self):
        """
        Test V1TokenReviewStatus
        """
        model = kubernetes.client.models.v1_token_review_status.V1TokenReviewStatus()


if __name__ == '__main__':
    unittest.main()
