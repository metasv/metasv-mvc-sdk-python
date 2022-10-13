# metasv_mvc_client.MerchantApi

All URIs are relative to *https://api-mvc-testnet.metasv.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchant_utxo_post**](MerchantApi.md#merchant_utxo_post) | **POST** /merchant/utxo | Pick utxos by addresses and amount.


# **merchant_utxo_post**
> [AddressUtxo] merchant_utxo_post()

Pick utxos by addresses and amount.

Selects a set of Utxos with total value higher than the given amount from a given address list . In case of HD wallets, multiple addresses can be specified.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import merchant_api
from metasv_mvc_client.model.utxo_pick_request import UtxoPickRequest
from metasv_mvc_client.model.address_utxo import AddressUtxo
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
    api_instance = merchant_api.MerchantApi(api_client)
    utxo_pick_request = UtxoPickRequest(
        addresses=[
            "addresses_example",
        ],
        amount=1,
    ) # UtxoPickRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Pick utxos by addresses and amount.
        api_response = api_instance.merchant_utxo_post(utxo_pick_request=utxo_pick_request)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling MerchantApi->merchant_utxo_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **utxo_pick_request** | [**UtxoPickRequest**](UtxoPickRequest.md)|  | [optional]

### Return type

[**[AddressUtxo]**](AddressUtxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | utxo pick success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

