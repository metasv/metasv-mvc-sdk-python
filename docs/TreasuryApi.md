# mvcapi-sdk.TreasuryApi

All URIs are relative to *https://testnet.mvcapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**treasury_get**](TreasuryApi.md#treasury_get) | **GET** /treasury | Get current treasury info.
[**treasury_history_get**](TreasuryApi.md#treasury_history_get) | **GET** /treasury/history | Get all treasury history.


# **treasury_get**
> TreasuryInfo treasury_get()

Get current treasury info.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import treasury_api
from mvcapi-sdk.model.treasury_info import TreasuryInfo
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
    api_instance = treasury_api.TreasuryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current treasury info.
        api_response = api_instance.treasury_get()
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling TreasuryApi->treasury_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TreasuryInfo**](TreasuryInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get treasury info success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **treasury_history_get**
> [TreasuryHistory] treasury_history_get()

Get all treasury history.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import treasury_api
from mvcapi-sdk.model.treasury_history import TreasuryHistory
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
    api_instance = treasury_api.TreasuryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all treasury history.
        api_response = api_instance.treasury_history_get()
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling TreasuryApi->treasury_history_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[TreasuryHistory]**](TreasuryHistory.md)

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

