"""
    MicrovisionChain API Document

    API definition for MicrovisionChain provided apis  # noqa: E501

    The version of the OpenAPI document: 3.0.8
    Contact: heqiming@mvcapi.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mvcapi-sdk
from mvcapi-sdk.api.outpoint_api import OutpointApi  # noqa: E501


class TestOutpointApi(unittest.TestCase):
    """OutpointApi unit test stubs"""

    def setUp(self):
        self.api = OutpointApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_outpoint_txid_index_get(self):
        """Test case for outpoint_txid_index_get

        Get tx output(outpoint for vin) spent status.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
