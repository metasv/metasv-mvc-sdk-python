# mvcapi-sdk.TxApi

All URIs are relative to *https://testnet.mvcapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tx_broadcast_batch_post**](TxApi.md#tx_broadcast_batch_post) | **POST** /tx/broadcast/batch | Broadcast a batch of tx to MvcApi fullnode. This endpoint use rpc sendrawtransactions.
[**tx_broadcast_post**](TxApi.md#tx_broadcast_post) | **POST** /tx/broadcast | Broadcast tx to MvcApi fullnode.
[**tx_txid_get**](TxApi.md#tx_txid_get) | **GET** /tx/{txid} | Get transaction detail by specific txid.
[**tx_txid_raw_get**](TxApi.md#tx_txid_raw_get) | **GET** /tx/{txid}/raw | Get transaction raw hex by specific txid.
[**tx_txid_seen_get**](TxApi.md#tx_txid_seen_get) | **GET** /tx/{txid}/seen | Whether MvcApi have seen this tx before. This is a fast approach to know if the tx exist or not.
[**vin_txid_detail_get**](TxApi.md#vin_txid_detail_get) | **GET** /vin/{txid}/detail | Get all output point of vins in the tx with detailed output script.


# **tx_broadcast_batch_post**
> BatchBroadcastResult tx_broadcast_batch_post()

Broadcast a batch of tx to MvcApi fullnode. This endpoint use rpc sendrawtransactions.

This api will broadcast to MvcApi fullnode directly.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import tx_api
from mvcapi-sdk.model.batch_broadcast_result import BatchBroadcastResult
from mvcapi-sdk.model.tx_raw import TxRaw
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
    api_instance = tx_api.TxApi(api_client)
    tx_raw = [
        TxRaw(
            hex="hex_example",
        ),
    ] # [TxRaw] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Broadcast a batch of tx to MvcApi fullnode. This endpoint use rpc sendrawtransactions.
        api_response = api_instance.tx_broadcast_batch_post(tx_raw=tx_raw)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling TxApi->tx_broadcast_batch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_raw** | [**[TxRaw]**](TxRaw.md)|  | [optional]

### Return type

[**BatchBroadcastResult**](BatchBroadcastResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Broadcast result list, txid returned with the original order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tx_broadcast_post**
> BroadcastResult tx_broadcast_post()

Broadcast tx to MvcApi fullnode.

This api will broadcast to MvcApi fullnode directly. This endpoint use rpc sendrawtransaction.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import tx_api
from mvcapi-sdk.model.broadcast_result import BroadcastResult
from mvcapi-sdk.model.tx_raw import TxRaw
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
    api_instance = tx_api.TxApi(api_client)
    tx_raw = TxRaw(
        hex="hex_example",
    ) # TxRaw |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Broadcast tx to MvcApi fullnode.
        api_response = api_instance.tx_broadcast_post(tx_raw=tx_raw)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling TxApi->tx_broadcast_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_raw** | [**TxRaw**](TxRaw.md)|  | [optional]

### Return type

[**BroadcastResult**](BroadcastResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Broadcast success, txid returned |  -  |
**403** | Broadcast Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tx_txid_get**
> TxDetail tx_txid_get(txid)

Get transaction detail by specific txid.

This api is parsed from raw hex, you can use /tx/{txid}/raw to parse tx by yourself, If you want detail input info, use '/vin/{txid}' to get detailed input info including address and value.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import tx_api
from mvcapi-sdk.model.tx_detail import TxDetail
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
    api_instance = tx_api.TxApi(api_client)
    txid = "txid_example" # str | the request ID to search, txhash
    show_script = True # bool | Return source script code or not (default false). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get transaction detail by specific txid.
        api_response = api_instance.tx_txid_get(txid)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling TxApi->tx_txid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get transaction detail by specific txid.
        api_response = api_instance.tx_txid_get(txid, show_script=show_script)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling TxApi->tx_txid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| the request ID to search, txhash |
 **show_script** | **bool**| Return source script code or not (default false). | [optional]

### Return type

[**TxDetail**](TxDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get transaction detail success. |  -  |
**404** | Transaction not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tx_txid_raw_get**
> TxRaw tx_txid_raw_get(txid)

Get transaction raw hex by specific txid.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import tx_api
from mvcapi-sdk.model.tx_raw import TxRaw
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
    api_instance = tx_api.TxApi(api_client)
    txid = "txid_example" # str | the request ID to search, txhash

    # example passing only required values which don't have defaults set
    try:
        # Get transaction raw hex by specific txid.
        api_response = api_instance.tx_txid_raw_get(txid)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling TxApi->tx_txid_raw_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| the request ID to search, txhash |

### Return type

[**TxRaw**](TxRaw.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get transaction raw hex success. |  -  |
**404** | Transaction not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tx_txid_seen_get**
> bool tx_txid_seen_get(txid)

Whether MvcApi have seen this tx before. This is a fast approach to know if the tx exist or not.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import tx_api
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
    api_instance = tx_api.TxApi(api_client)
    txid = "txid_example" # str | the request ID to search, txhash

    # example passing only required values which don't have defaults set
    try:
        # Whether MvcApi have seen this tx before. This is a fast approach to know if the tx exist or not.
        api_response = api_instance.tx_txid_seen_get(txid)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling TxApi->tx_txid_seen_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| the request ID to search, txhash |

### Return type

**bool**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return true if the transaction is found. |  -  |
**404** | Transaction not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vin_txid_detail_get**
> [OutputInfoDetail] vin_txid_detail_get(txid)

Get all output point of vins in the tx with detailed output script.

Search output points by spent txid. Use this api to get detailed inputs for the tx.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import tx_api
from mvcapi-sdk.model.output_info_detail import OutputInfoDetail
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
    api_instance = tx_api.TxApi(api_client)
    txid = "txid_example" # str | The txid of the vins

    # example passing only required values which don't have defaults set
    try:
        # Get all output point of vins in the tx with detailed output script.
        api_response = api_instance.vin_txid_detail_get(txid)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling TxApi->vin_txid_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| The txid of the vins |

### Return type

[**[OutputInfoDetail]**](OutputInfoDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get vin list success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

