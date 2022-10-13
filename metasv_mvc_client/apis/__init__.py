
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.address_api import AddressApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from metasv_mvc_client.api.address_api import AddressApi
from metasv_mvc_client.api.block_api import BlockApi
from metasv_mvc_client.api.contract_api import ContractApi
from metasv_mvc_client.api.merchant_api import MerchantApi
from metasv_mvc_client.api.outpoint_api import OutpointApi
from metasv_mvc_client.api.tx_api import TxApi
from metasv_mvc_client.api.xpub_api import XpubApi
