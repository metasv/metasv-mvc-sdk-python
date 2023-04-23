# mvcapi-sdk.XpubApi

All URIs are relative to *https://testnet.mvcapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**xpub_lite_xpub_address_address_get**](XpubApi.md#xpub_lite_xpub_address_address_get) | **GET** /xpubLite/{xpub}/address/{address} | Get xpub address type and index. Only index under /0/70 /1/30 is valid. Otherwise not found.
[**xpub_lite_xpub_balance_get**](XpubApi.md#xpub_lite_xpub_balance_get) | **GET** /xpubLite/{xpub}/balance | Get xpub balances including confirmed and unconfirmed.
[**xpub_lite_xpub_utxo_get**](XpubApi.md#xpub_lite_xpub_utxo_get) | **GET** /xpubLite/{xpub}/utxo | Get xpub utxos by specific xpub(300 per page).


# **xpub_lite_xpub_address_address_get**
> XpubAddress xpub_lite_xpub_address_address_get(xpub, address)

Get xpub address type and index. Only index under /0/70 /1/30 is valid. Otherwise not found.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import xpub_api
from mvcapi-sdk.model.xpub_address import XpubAddress
from mvcapi-sdk.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://testnet.mvcapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mvcapi-sdk.Configuration(
    host = "https://testnet.mvcapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = mvcapi-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with mvcapi-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xpub_api.XpubApi(api_client)
    xpub = "xpub_example" # str | the requested xpub
    address = "address_example" # str | the requested address

    # example passing only required values which don't have defaults set
    try:
        # Get xpub address type and index. Only index under /0/70 /1/30 is valid. Otherwise not found.
        api_response = api_instance.xpub_lite_xpub_address_address_get(xpub, address)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling XpubApi->xpub_lite_xpub_address_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xpub** | **str**| the requested xpub |
 **address** | **str**| the requested address |

### Return type

[**XpubAddress**](XpubAddress.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get xpub address success. |  -  |
**401** | Access token is missing or invalid |  -  |
**404** | Address not found in the xpub. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpub_lite_xpub_balance_get**
> XpubLiteBalance xpub_lite_xpub_balance_get(xpub)

Get xpub balances including confirmed and unconfirmed.

This api returns confirmed balance(same as address balance), not sumed utxos.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import xpub_api
from mvcapi-sdk.model.xpub_lite_balance import XpubLiteBalance
from mvcapi-sdk.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://testnet.mvcapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mvcapi-sdk.Configuration(
    host = "https://testnet.mvcapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = mvcapi-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with mvcapi-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xpub_api.XpubApi(api_client)
    xpub = "xpub_example" # str | the xpub to search

    # example passing only required values which don't have defaults set
    try:
        # Get xpub balances including confirmed and unconfirmed.
        api_response = api_instance.xpub_lite_xpub_balance_get(xpub)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling XpubApi->xpub_lite_xpub_balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xpub** | **str**| the xpub to search |

### Return type

[**XpubLiteBalance**](XpubLiteBalance.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get xpub balance success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpub_lite_xpub_utxo_get**
> [XpubUtxo] xpub_lite_xpub_utxo_get(xpub)

Get xpub utxos by specific xpub(300 per page).

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import xpub_api
from mvcapi-sdk.model.xpub_utxo import XpubUtxo
from mvcapi-sdk.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://testnet.mvcapi.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mvcapi-sdk.Configuration(
    host = "https://testnet.mvcapi.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = mvcapi-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with mvcapi-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xpub_api.XpubApi(api_client)
    xpub = "xpub_example" # str | the requested xpub
    limit = 1 # int | The max items returned in this query(default 300), not bigger than 5000. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get xpub utxos by specific xpub(300 per page).
        api_response = api_instance.xpub_lite_xpub_utxo_get(xpub)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling XpubApi->xpub_lite_xpub_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get xpub utxos by specific xpub(300 per page).
        api_response = api_instance.xpub_lite_xpub_utxo_get(xpub, limit=limit)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling XpubApi->xpub_lite_xpub_utxo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xpub** | **str**| the requested xpub |
 **limit** | **int**| The max items returned in this query(default 300), not bigger than 5000. | [optional]

### Return type

[**[XpubUtxo]**](XpubUtxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get xpub utxos success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

