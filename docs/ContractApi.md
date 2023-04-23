# mvcapi-sdk.ContractApi

All URIs are relative to *https://testnet.mvcapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contract_ft_address_address_balance_confirmed_get**](ContractApi.md#contract_ft_address_address_balance_confirmed_get) | **GET** /contract/ft/address/{address}/balance/confirmed | Get all contract token balances for specific address ignoring all unconfirmed txs.
[**contract_ft_address_address_balance_get**](ContractApi.md#contract_ft_address_address_balance_get) | **GET** /contract/ft/address/{address}/balance | Get all contract token balances for specific address.
[**contract_ft_address_address_code_hash_genesis_tx_get**](ContractApi.md#contract_ft_address_address_code_hash_genesis_tx_get) | **GET** /contract/ft/address/{address}/{codeHash}/{genesis}/tx | Get all contract token balances for specific address.
[**contract_ft_address_address_utxo_get**](ContractApi.md#contract_ft_address_address_utxo_get) | **GET** /contract/ft/address/{address}/utxo | Get all contract token utxos for specific address.
[**contract_nft_address_address_count_confirmed_get**](ContractApi.md#contract_nft_address_address_count_confirmed_get) | **GET** /contract/nft/address/{address}/count/confirmed | Get confirmed utxo count for specific nft(ignore all unconfirmed txs).
[**contract_nft_address_address_summary_get**](ContractApi.md#contract_nft_address_address_summary_get) | **GET** /contract/nft/address/{address}/summary | Get nft summary(NFT count group by genesis) for address.
[**contract_nft_address_address_utxo_get**](ContractApi.md#contract_nft_address_address_utxo_get) | **GET** /contract/nft/address/{address}/utxo | Get all contract nft token utxos for specific address.
[**contract_nft_genesis_code_hash_genesis_summary_get**](ContractApi.md#contract_nft_genesis_code_hash_genesis_summary_get) | **GET** /contract/nft/genesis/{codeHash}/{genesis}/summary | Get nft summary(count group by address) for specific codeHash and genesisId(result cached for 60s).
[**contract_nft_genesis_code_hash_genesis_utxo_get**](ContractApi.md#contract_nft_genesis_code_hash_genesis_utxo_get) | **GET** /contract/nft/genesis/{codeHash}/{genesis}/utxo | Get all contract nft token utxos by codeHash and genesisId.
[**contract_nft_sell_address_address_utxo_get**](ContractApi.md#contract_nft_sell_address_address_utxo_get) | **GET** /contract/nft/sell/address/{address}/utxo | Get all contract sell sell utxos for specific address.
[**contract_nft_sell_genesis_code_hash_genesis_utxo_get**](ContractApi.md#contract_nft_sell_genesis_code_hash_genesis_utxo_get) | **GET** /contract/nft/sell/genesis/{codeHash}/{genesis}/utxo | Get all contract nft token utxos by codeHash and genesisId.
[**contract_unique_genesis_code_hash_genesis_utxo_get**](ContractApi.md#contract_unique_genesis_code_hash_genesis_utxo_get) | **GET** /contract/unique/genesis/{codeHash}/{genesis}/utxo | Get contract unique utxos by codeHash and genesisId.


# **contract_ft_address_address_balance_confirmed_get**
> int contract_ft_address_address_balance_confirmed_get(address, code_hash, genesis)

Get all contract token balances for specific address ignoring all unconfirmed txs.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address
    code_hash = "codeHash_example" # str | Filter by contract code hash
    genesis = "genesis_example" # str | Filter by contract genesis

    # example passing only required values which don't have defaults set
    try:
        # Get all contract token balances for specific address ignoring all unconfirmed txs.
        api_response = api_instance.contract_ft_address_address_balance_confirmed_get(address, code_hash, genesis)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_ft_address_address_balance_confirmed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| the requested address |
 **code_hash** | **str**| Filter by contract code hash |
 **genesis** | **str**| Filter by contract genesis |

### Return type

**int**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract ft balances succes（ingore unconfirmed txs）. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_ft_address_address_balance_get**
> [ContractFtBalance] contract_ft_address_address_balance_get(address)

Get all contract token balances for specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
from mvcapi-sdk.model.contract_ft_balance import ContractFtBalance
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address
    code_hash = "codeHash_example" # str | Filter by contract code hash (optional)
    genesis = "genesis_example" # str | Filter by contract genesis (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all contract token balances for specific address.
        api_response = api_instance.contract_ft_address_address_balance_get(address)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_ft_address_address_balance_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract token balances for specific address.
        api_response = api_instance.contract_ft_address_address_balance_get(address, code_hash=code_hash, genesis=genesis)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_ft_address_address_balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| the requested address |
 **code_hash** | **str**| Filter by contract code hash | [optional]
 **genesis** | **str**| Filter by contract genesis | [optional]

### Return type

[**[ContractFtBalance]**](ContractFtBalance.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract ft balances success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_ft_address_address_code_hash_genesis_tx_get**
> [ContractFtAddressTx] contract_ft_address_address_code_hash_genesis_tx_get(address, code_hash, genesis)

Get all contract token balances for specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
from mvcapi-sdk.model.contract_ft_address_tx import ContractFtAddressTx
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address
    code_hash = "codeHash_example" # str | Filter by contract code hash
    genesis = "genesis_example" # str | Filter by contract genesis
    flag = "flag_example" # str | The last id of the last query(Paging flag) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all contract token balances for specific address.
        api_response = api_instance.contract_ft_address_address_code_hash_genesis_tx_get(address, code_hash, genesis)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_ft_address_address_code_hash_genesis_tx_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract token balances for specific address.
        api_response = api_instance.contract_ft_address_address_code_hash_genesis_tx_get(address, code_hash, genesis, flag=flag)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_ft_address_address_code_hash_genesis_tx_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| the requested address |
 **code_hash** | **str**| Filter by contract code hash |
 **genesis** | **str**| Filter by contract genesis |
 **flag** | **str**| The last id of the last query(Paging flag) | [optional]

### Return type

[**[ContractFtAddressTx]**](ContractFtAddressTx.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract ft history success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_ft_address_address_utxo_get**
> [ContractFtUtxo] contract_ft_address_address_utxo_get(address)

Get all contract token utxos for specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
from mvcapi-sdk.model.contract_ft_utxo import ContractFtUtxo
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address
    code_hash = "codeHash_example" # str | Filter by contract code hash (optional)
    genesis = "genesis_example" # str | Filter by contract genesis (optional)
    flag = "flag_example" # str | The flag of the last query Item(Paging flag) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all contract token utxos for specific address.
        api_response = api_instance.contract_ft_address_address_utxo_get(address)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_ft_address_address_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract token utxos for specific address.
        api_response = api_instance.contract_ft_address_address_utxo_get(address, code_hash=code_hash, genesis=genesis, flag=flag)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_ft_address_address_utxo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| the requested address |
 **code_hash** | **str**| Filter by contract code hash | [optional]
 **genesis** | **str**| Filter by contract genesis | [optional]
 **flag** | **str**| The flag of the last query Item(Paging flag) | [optional]

### Return type

[**[ContractFtUtxo]**](ContractFtUtxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract ft utxo success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_address_address_count_confirmed_get**
> int contract_nft_address_address_count_confirmed_get(address, code_hash, genesis)

Get confirmed utxo count for specific nft(ignore all unconfirmed txs).

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address
    code_hash = "codeHash_example" # str | Filter by contract code hash
    genesis = "genesis_example" # str | Filter by contract genesis

    # example passing only required values which don't have defaults set
    try:
        # Get confirmed utxo count for specific nft(ignore all unconfirmed txs).
        api_response = api_instance.contract_nft_address_address_count_confirmed_get(address, code_hash, genesis)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_address_address_count_confirmed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| the requested address |
 **code_hash** | **str**| Filter by contract code hash |
 **genesis** | **str**| Filter by contract genesis |

### Return type

**int**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract nft utxo success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_address_address_summary_get**
> [ContractNftAddressSummary] contract_nft_address_address_summary_get(address)

Get nft summary(NFT count group by genesis) for address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
from mvcapi-sdk.model.contract_nft_address_summary import ContractNftAddressSummary
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address

    # example passing only required values which don't have defaults set
    try:
        # Get nft summary(NFT count group by genesis) for address.
        api_response = api_instance.contract_nft_address_address_summary_get(address)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_address_address_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| the requested address |

### Return type

[**[ContractNftAddressSummary]**](ContractNftAddressSummary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract nft utxo success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_address_address_utxo_get**
> [ContractNftUtxo] contract_nft_address_address_utxo_get(address)

Get all contract nft token utxos for specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
from mvcapi-sdk.model.contract_nft_utxo import ContractNftUtxo
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address
    code_hash = "codeHash_example" # str | Filter by contract code hash (optional)
    genesis = "genesis_example" # str | Filter by contract genesis (optional)
    limit = 1 # int | Limit the return count(no more than 300) (optional)
    flag = "flag_example" # str | The flag of the last query Item(Paging flag) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all contract nft token utxos for specific address.
        api_response = api_instance.contract_nft_address_address_utxo_get(address)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_address_address_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract nft token utxos for specific address.
        api_response = api_instance.contract_nft_address_address_utxo_get(address, code_hash=code_hash, genesis=genesis, limit=limit, flag=flag)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_address_address_utxo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| the requested address |
 **code_hash** | **str**| Filter by contract code hash | [optional]
 **genesis** | **str**| Filter by contract genesis | [optional]
 **limit** | **int**| Limit the return count(no more than 300) | [optional]
 **flag** | **str**| The flag of the last query Item(Paging flag) | [optional]

### Return type

[**[ContractNftUtxo]**](ContractNftUtxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract nft utxo success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_genesis_code_hash_genesis_summary_get**
> [ContractNftGenesisSummary] contract_nft_genesis_code_hash_genesis_summary_get(code_hash, genesis)

Get nft summary(count group by address) for specific codeHash and genesisId(result cached for 60s).

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
from mvcapi-sdk.model.contract_nft_genesis_summary import ContractNftGenesisSummary
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
    api_instance = contract_api.ContractApi(api_client)
    code_hash = "codeHash_example" # str | Code hash of the token.
    genesis = "genesis_example" # str | Contract genesis

    # example passing only required values which don't have defaults set
    try:
        # Get nft summary(count group by address) for specific codeHash and genesisId(result cached for 60s).
        api_response = api_instance.contract_nft_genesis_code_hash_genesis_summary_get(code_hash, genesis)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_genesis_code_hash_genesis_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_hash** | **str**| Code hash of the token. |
 **genesis** | **str**| Contract genesis |

### Return type

[**[ContractNftGenesisSummary]**](ContractNftGenesisSummary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract nft utxo success(result cached for 60s).. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_genesis_code_hash_genesis_utxo_get**
> [ContractNftUtxo] contract_nft_genesis_code_hash_genesis_utxo_get(code_hash, genesis)

Get all contract nft token utxos by codeHash and genesisId.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
from mvcapi-sdk.model.contract_nft_utxo import ContractNftUtxo
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
    api_instance = contract_api.ContractApi(api_client)
    code_hash = "codeHash_example" # str | Code hash of the token.
    genesis = "genesis_example" # str | Contract genesis
    token_index = 1 # int | Find exact token Index. (optional)
    max = 1 # int | Token index not bigger than this(include this). (optional)
    min = 1 # int | Token index not less than this(include this). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all contract nft token utxos by codeHash and genesisId.
        api_response = api_instance.contract_nft_genesis_code_hash_genesis_utxo_get(code_hash, genesis)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_genesis_code_hash_genesis_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract nft token utxos by codeHash and genesisId.
        api_response = api_instance.contract_nft_genesis_code_hash_genesis_utxo_get(code_hash, genesis, token_index=token_index, max=max, min=min)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_genesis_code_hash_genesis_utxo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_hash** | **str**| Code hash of the token. |
 **genesis** | **str**| Contract genesis |
 **token_index** | **int**| Find exact token Index. | [optional]
 **max** | **int**| Token index not bigger than this(include this). | [optional]
 **min** | **int**| Token index not less than this(include this). | [optional]

### Return type

[**[ContractNftUtxo]**](ContractNftUtxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract nft utxo success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_sell_address_address_utxo_get**
> [ContractNftSellUtxo] contract_nft_sell_address_address_utxo_get(address)

Get all contract sell sell utxos for specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
from mvcapi-sdk.model.contract_nft_sell_utxo import ContractNftSellUtxo
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | Owner address.
    code_hash = "codeHash_example" # str | Filter by contract code hash (optional)
    genesis = "genesis_example" # str | Filter by contract genesis (optional)
    flag = "flag_example" # str | The flag of the last query Item(Paging flag) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all contract sell sell utxos for specific address.
        api_response = api_instance.contract_nft_sell_address_address_utxo_get(address)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_sell_address_address_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract sell sell utxos for specific address.
        api_response = api_instance.contract_nft_sell_address_address_utxo_get(address, code_hash=code_hash, genesis=genesis, flag=flag)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_sell_address_address_utxo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Owner address. |
 **code_hash** | **str**| Filter by contract code hash | [optional]
 **genesis** | **str**| Filter by contract genesis | [optional]
 **flag** | **str**| The flag of the last query Item(Paging flag) | [optional]

### Return type

[**[ContractNftSellUtxo]**](ContractNftSellUtxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract nft sell utxo success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_sell_genesis_code_hash_genesis_utxo_get**
> [ContractNftSellUtxo] contract_nft_sell_genesis_code_hash_genesis_utxo_get(code_hash, genesis)

Get all contract nft token utxos by codeHash and genesisId.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
from mvcapi-sdk.model.contract_nft_sell_utxo import ContractNftSellUtxo
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
    api_instance = contract_api.ContractApi(api_client)
    code_hash = "codeHash_example" # str | Code hash of the token.
    genesis = "genesis_example" # str | Contract genesis
    token_index = 1 # int | Find exact token Index. (optional)
    max = 1 # int | Token index not bigger than this(include this). (optional)
    min = 1 # int | Token index not less than this(include this). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all contract nft token utxos by codeHash and genesisId.
        api_response = api_instance.contract_nft_sell_genesis_code_hash_genesis_utxo_get(code_hash, genesis)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_sell_genesis_code_hash_genesis_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract nft token utxos by codeHash and genesisId.
        api_response = api_instance.contract_nft_sell_genesis_code_hash_genesis_utxo_get(code_hash, genesis, token_index=token_index, max=max, min=min)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_sell_genesis_code_hash_genesis_utxo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_hash** | **str**| Code hash of the token. |
 **genesis** | **str**| Contract genesis |
 **token_index** | **int**| Find exact token Index. | [optional]
 **max** | **int**| Token index not bigger than this(include this). | [optional]
 **min** | **int**| Token index not less than this(include this). | [optional]

### Return type

[**[ContractNftSellUtxo]**](ContractNftSellUtxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract nft sell utxo success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_unique_genesis_code_hash_genesis_utxo_get**
> [ContractUniqueUtxo] contract_unique_genesis_code_hash_genesis_utxo_get(code_hash, genesis)

Get contract unique utxos by codeHash and genesisId.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import mvcapi-sdk
from mvcapi-sdk.api import contract_api
from mvcapi-sdk.model.contract_unique_utxo import ContractUniqueUtxo
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
    api_instance = contract_api.ContractApi(api_client)
    code_hash = "codeHash_example" # str | Code hash of the token.
    genesis = "genesis_example" # str | Contract genesis

    # example passing only required values which don't have defaults set
    try:
        # Get contract unique utxos by codeHash and genesisId.
        api_response = api_instance.contract_unique_genesis_code_hash_genesis_utxo_get(code_hash, genesis)
        pprint(api_response)
    except mvcapi-sdk.ApiException as e:
        print("Exception when calling ContractApi->contract_unique_genesis_code_hash_genesis_utxo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_hash** | **str**| Code hash of the token. |
 **genesis** | **str**| Contract genesis |

### Return type

[**[ContractUniqueUtxo]**](ContractUniqueUtxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract unique utxo success. |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

