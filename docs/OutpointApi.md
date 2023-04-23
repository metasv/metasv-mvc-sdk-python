# mvcapi-sdk.OutpointApi

All URIs are relative to *https://testnet.mvcapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outpoint_txid_index_get**](OutpointApi.md#outpoint_txid_index_get) | **GET** /outpoint/{txid}/{index} | Get tx output(outpoint for vin) spent status.


# **outpoint_txid_index_get**
> OutputInfo outpoint_txid_index_get(txid, index)

Get tx output(outpoint for vin) spent status.

Get detailed info for a utxo(or txo if spent), Only outputs spent no longer than one month are available. (Premium feature will support full history)

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import outpoint_api
from mvcapi-sdk.model.output_info import OutputInfo
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
    api_instance = outpoint_api.OutpointApi(api_client)
    txid = "txid_example" # str | The txid of the output
    index = 1 # int | The index of the output in the tx.

    # example passing only required values which don't have defaults set
    try:
        # Get tx output(outpoint for vin) spent status.
        api_response = api_instance.outpoint_txid_index_get(txid, index)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling OutpointApi->outpoint_txid_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| The txid of the output |
 **index** | **int**| The index of the output in the tx. |

### Return type

[**OutputInfo**](OutputInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get outpoint success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

