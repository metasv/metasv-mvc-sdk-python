# metasv_mvc_client.BlockApi

All URIs are relative to *https://api-mvc-testnet.metasv.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_block_id_get**](BlockApi.md#block_block_id_get) | **GET** /block/{blockId} | Get block request by height or hash
[**block_get**](BlockApi.md#block_get) | **GET** /block | Get recent block list by paging. 30 items per page.
[**block_info_get**](BlockApi.md#block_info_get) | **GET** /block/info | Get current blockchain info from full node.


# **block_block_id_get**
> BlockHeader block_block_id_get(block_id)

Get block request by height or hash

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import block_api
from metasv_mvc_client.model.block_header import BlockHeader
from pprint import pprint
# Defining the host is optional and defaults to https://api-mvc-testnet.metasv.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metasv_mvc_client.Configuration(
    host = "https://api-mvc-testnet.metasv.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = metasv_mvc_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with metasv_mvc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = block_api.BlockApi(api_client)
    block_id = "blockId_example" # str | The block id, height or hash acceptable.

    # example passing only required values which don't have defaults set
    try:
        # Get block request by height or hash
        api_response = api_instance.block_block_id_get(block_id)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling BlockApi->block_block_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| The block id, height or hash acceptable. |

### Return type

[**BlockHeader**](BlockHeader.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get block info success |  -  |
**404** | block info not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_get**
> [BlockHeader] block_get()

Get recent block list by paging. 30 items per page.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import block_api
from metasv_mvc_client.model.block_header import BlockHeader
from pprint import pprint
# Defining the host is optional and defaults to https://api-mvc-testnet.metasv.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metasv_mvc_client.Configuration(
    host = "https://api-mvc-testnet.metasv.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = metasv_mvc_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with metasv_mvc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = block_api.BlockApi(api_client)
    last = 1 # int | paging flag, height of last item in last page (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get recent block list by paging. 30 items per page.
        api_response = api_instance.block_get(last=last)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling BlockApi->block_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last** | **int**| paging flag, height of last item in last page | [optional]

### Return type

[**[BlockHeader]**](BlockHeader.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully get lists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_info_get**
> BlockchainInfo block_info_get()

Get current blockchain info from full node.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import block_api
from metasv_mvc_client.model.blockchain_info import BlockchainInfo
from pprint import pprint
# Defining the host is optional and defaults to https://api-mvc-testnet.metasv.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metasv_mvc_client.Configuration(
    host = "https://api-mvc-testnet.metasv.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = metasv_mvc_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with metasv_mvc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = block_api.BlockApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current blockchain info from full node.
        api_response = api_instance.block_info_get()
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling BlockApi->block_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlockchainInfo**](BlockchainInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get blockchain info success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

