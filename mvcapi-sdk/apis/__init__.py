
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
from mvcapi-sdk.api.address_api import AddressApi
from mvcapi-sdk.api.block_api import BlockApi
from mvcapi-sdk.api.contract_api import ContractApi
from mvcapi-sdk.api.merchant_api import MerchantApi
from mvcapi-sdk.api.outpoint_api import OutpointApi
from mvcapi-sdk.api.treasury_api import TreasuryApi
from mvcapi-sdk.api.tx_api import TxApi
from mvcapi-sdk.api.xpub_api import XpubApi
