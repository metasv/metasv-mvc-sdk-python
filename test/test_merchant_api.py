"""
    MicrovisionChain API Document

    API definition for MicrovisionChain provided apis  # noqa: E501

    The version of the OpenAPI document: 3.0.8
    Contact: heqiming@mvcapi.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mvcapi-sdk
from mvcapi-sdk.api.merchant_api import MerchantApi  # noqa: E501


class TestMerchantApi(unittest.TestCase):
    """MerchantApi unit test stubs"""

    def setUp(self):
        self.api = MerchantApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_merchant_utxo_post(self):
        """Test case for merchant_utxo_post

        Pick utxos by addresses and amount.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
