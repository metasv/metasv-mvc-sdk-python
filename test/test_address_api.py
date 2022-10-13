"""
    MetaSV API Spec

    API definition for MetaSV provided apis  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: heqiming@metasv.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import metasv_mvc_client
from metasv_mvc_client.api.address_api import AddressApi  # noqa: E501


class TestAddressApi(unittest.TestCase):
    """AddressApi unit test stubs"""

    def setUp(self):
        self.api = AddressApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_address_address_balance_get(self):
        """Test case for address_address_balance_get

        Get address balance by specific address.  # noqa: E501
        """
        pass

    def test_address_address_tx_get(self):
        """Test case for address_address_tx_get

        Get address history by specific address(recent 10 days available).  # noqa: E501
        """
        pass

    def test_address_address_utxo_get(self):
        """Test case for address_address_utxo_get

        Get address utxos by specific address(100 per page).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()