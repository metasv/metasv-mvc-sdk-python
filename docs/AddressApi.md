# mvcapi-sdk.AddressApi

All URIs are relative to *https://testnet.mvcapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**address_address_balance_get**](AddressApi.md#address_address_balance_get) | **GET** /address/{address}/balance | Get address balance by specific address.
[**address_address_tx_get**](AddressApi.md#address_address_tx_get) | **GET** /address/{address}/tx | Get address history by specific address(recent 10 days available).
[**address_address_utxo_get**](AddressApi.md#address_address_utxo_get) | **GET** /address/{address}/utxo | Get address utxos by specific address(100 per page).


# **address_address_balance_get**
> AddressBalance address_address_balance_get(address)

Get address balance by specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import address_api
from mvcapi-sdk.model.address_balance import AddressBalance
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
    api_instance = address_api.AddressApi(api_client)
    address = "address_example" # str | the requested address

    # example passing only required values which don't have defaults set
    try:
        # Get address balance by specific address.
        api_response = api_instance.address_address_balance_get(address)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling AddressApi->address_address_balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| the requested address |

### Return type

[**AddressBalance**](AddressBalance.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get address detail success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_address_tx_get**
> [AddressTx] address_address_tx_get(address)

Get address history by specific address(recent 10 days available).

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import address_api
from mvcapi-sdk.model.address_tx import AddressTx
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
    api_instance = address_api.AddressApi(api_client)
    address = "address_example" # str | the requested address
    flag = "flag_example" # str | The last id of the last query(Paging flag) (optional)
    confirmed = True # bool | (default true) fetch confirmed tx, fetch unconfirmed tx if false (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get address history by specific address(recent 10 days available).
        api_response = api_instance.address_address_tx_get(address)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling AddressApi->address_address_tx_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get address history by specific address(recent 10 days available).
        api_response = api_instance.address_address_tx_get(address, flag=flag, confirmed=confirmed)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling AddressApi->address_address_tx_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| the requested address |
 **flag** | **str**| The last id of the last query(Paging flag) | [optional]
 **confirmed** | **bool**| (default true) fetch confirmed tx, fetch unconfirmed tx if false | [optional]

### Return type

[**[AddressTx]**](AddressTx.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get address transaction history success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_address_utxo_get**
> [AddressUtxo] address_address_utxo_get(address)

Get address utxos by specific address(100 per page).

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import address_api
from mvcapi-sdk.model.address_utxo import AddressUtxo
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
    api_instance = address_api.AddressApi(api_client)
    address = "address_example" # str | the requested address
    flag = "flag_example" # str | The last id of the last query(Paging flag) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get address utxos by specific address(100 per page).
        api_response = api_instance.address_address_utxo_get(address)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling AddressApi->address_address_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get address utxos by specific address(100 per page).
        api_response = api_instance.address_address_utxo_get(address, flag=flag)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling AddressApi->address_address_utxo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| the requested address |
 **flag** | **str**| The last id of the last query(Paging flag) | [optional]

### Return type

[**[AddressUtxo]**](AddressUtxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get address utxos success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

