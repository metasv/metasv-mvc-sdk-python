# metasv_mvc_client.ContractApi

All URIs are relative to *https://api-mvc-testnet.metasv.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contract_ft_address_address_balance_confirmed_get**](ContractApi.md#contract_ft_address_address_balance_confirmed_get) | **GET** /contract/ft/address/{address}/balance/confirmed | Get all contract token balances for specific address ignoring all unconfirmed txs.
[**contract_ft_address_address_balance_get**](ContractApi.md#contract_ft_address_address_balance_get) | **GET** /contract/ft/address/{address}/balance | Get all contract token balances for specific address.
[**contract_ft_address_address_utxo_get**](ContractApi.md#contract_ft_address_address_utxo_get) | **GET** /contract/ft/address/{address}/utxo | Get all contract token utxos for specific address.
[**contract_nft_address_address_count_confirmed_get**](ContractApi.md#contract_nft_address_address_count_confirmed_get) | **GET** /contract/nft/address/{address}/count/confirmed | Get confirmed utxo count for specific nft(ignore all unconfirmed txs).
[**contract_nft_address_address_summary_get**](ContractApi.md#contract_nft_address_address_summary_get) | **GET** /contract/nft/address/{address}/summary | Get nft summary(NFT count group by genesis) for address.
[**contract_nft_address_address_utxo_get**](ContractApi.md#contract_nft_address_address_utxo_get) | **GET** /contract/nft/address/{address}/utxo | Get all contract nft token utxos for specific address.
[**contract_nft_auction_code_hash_code_hash_nft_id_nft_id_utxo_get**](ContractApi.md#contract_nft_auction_code_hash_code_hash_nft_id_nft_id_utxo_get) | **GET** /contract/nft/auction/codeHash/{codeHash}/nftId/{nftId}/utxo | Get all contract nft token utxos by codeHash and genesisId.
[**contract_nft_genesis_code_hash_genesis_summary_get**](ContractApi.md#contract_nft_genesis_code_hash_genesis_summary_get) | **GET** /contract/nft/genesis/{codeHash}/{genesis}/summary | Get nft summary(count group by address) for specific codeHash and genesisId(result cached for 60s).
[**contract_nft_genesis_code_hash_genesis_utxo_get**](ContractApi.md#contract_nft_genesis_code_hash_genesis_utxo_get) | **GET** /contract/nft/genesis/{codeHash}/{genesis}/utxo | Get all contract nft token utxos by codeHash and genesisId.
[**contract_nft_sell_address_address_utxo_get**](ContractApi.md#contract_nft_sell_address_address_utxo_get) | **GET** /contract/nft/sell/address/{address}/utxo | Get all contract sell sell utxos for specific address.
[**contract_nft_sell_genesis_code_hash_genesis_utxo_get**](ContractApi.md#contract_nft_sell_genesis_code_hash_genesis_utxo_get) | **GET** /contract/nft/sell/genesis/{codeHash}/{genesis}/utxo | Get all contract nft token utxos by codeHash and genesisId.
[**contract_nft_sell_v2_address_address_utxo_get**](ContractApi.md#contract_nft_sell_v2_address_address_utxo_get) | **GET** /contract/nft/sellV2/address/{address}/utxo | Get all contract sell sell utxos for specific address.
[**contract_nft_sell_v2_genesis_code_hash_genesis_utxo_get**](ContractApi.md#contract_nft_sell_v2_genesis_code_hash_genesis_utxo_get) | **GET** /contract/nft/sellV2/genesis/{codeHash}/{genesis}/utxo | Get all contract nft token utxos by codeHash and genesisId.
[**contract_unique_genesis_code_hash_genesis_utxo_get**](ContractApi.md#contract_unique_genesis_code_hash_genesis_utxo_get) | **GET** /contract/unique/genesis/{codeHash}/{genesis}/utxo | Get contract unique utxos by codeHash and genesisId.


# **contract_ft_address_address_balance_confirmed_get**
> int contract_ft_address_address_balance_confirmed_get(address, code_hash, genesis)

Get all contract token balances for specific address ignoring all unconfirmed txs.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address
    code_hash = "codeHash_example" # str | Filter by contract code hash
    genesis = "genesis_example" # str | Filter by contract genesis

    # example passing only required values which don't have defaults set
    try:
        # Get all contract token balances for specific address ignoring all unconfirmed txs.
        api_response = api_instance.contract_ft_address_address_balance_confirmed_get(address, code_hash, genesis)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_ft_address_address_balance_get**
> [ContractFtBalance] contract_ft_address_address_balance_get(address)

Get all contract token balances for specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_ft_balance import ContractFtBalance
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address
    code_hash = "codeHash_example" # str | Filter by contract code hash (optional)
    genesis = "genesis_example" # str | Filter by contract genesis (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all contract token balances for specific address.
        api_response = api_instance.contract_ft_address_address_balance_get(address)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_ft_address_address_balance_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract token balances for specific address.
        api_response = api_instance.contract_ft_address_address_balance_get(address, code_hash=code_hash, genesis=genesis)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_ft_address_address_utxo_get**
> [ContractFtUtxo] contract_ft_address_address_utxo_get(address)

Get all contract token utxos for specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_ft_utxo import ContractFtUtxo
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
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_ft_address_address_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract token utxos for specific address.
        api_response = api_instance.contract_ft_address_address_utxo_get(address, code_hash=code_hash, genesis=genesis, flag=flag)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_address_address_count_confirmed_get**
> int contract_nft_address_address_count_confirmed_get(address, code_hash, genesis)

Get confirmed utxo count for specific nft(ignore all unconfirmed txs).

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address
    code_hash = "codeHash_example" # str | Filter by contract code hash
    genesis = "genesis_example" # str | Filter by contract genesis

    # example passing only required values which don't have defaults set
    try:
        # Get confirmed utxo count for specific nft(ignore all unconfirmed txs).
        api_response = api_instance.contract_nft_address_address_count_confirmed_get(address, code_hash, genesis)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_address_address_summary_get**
> [ContractNftAddressSummary] contract_nft_address_address_summary_get(address)

Get nft summary(NFT count group by genesis) for address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_nft_address_summary import ContractNftAddressSummary
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | the requested address

    # example passing only required values which don't have defaults set
    try:
        # Get nft summary(NFT count group by genesis) for address.
        api_response = api_instance.contract_nft_address_address_summary_get(address)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_address_address_utxo_get**
> [ContractNftUtxo] contract_nft_address_address_utxo_get(address)

Get all contract nft token utxos for specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_nft_utxo import ContractNftUtxo
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
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_address_address_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract nft token utxos for specific address.
        api_response = api_instance.contract_nft_address_address_utxo_get(address, code_hash=code_hash, genesis=genesis, limit=limit, flag=flag)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_auction_code_hash_code_hash_nft_id_nft_id_utxo_get**
> [ContractNftAuctionUtxo] contract_nft_auction_code_hash_code_hash_nft_id_nft_id_utxo_get(code_hash, nft_id)

Get all contract nft token utxos by codeHash and genesisId.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_nft_auction_utxo import ContractNftAuctionUtxo
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
    api_instance = contract_api.ContractApi(api_client)
    code_hash = "codeHash_example" # str | Code hash of the token.
    nft_id = "nftId_example" # str | Nft id of this auction.

    # example passing only required values which don't have defaults set
    try:
        # Get all contract nft token utxos by codeHash and genesisId.
        api_response = api_instance.contract_nft_auction_code_hash_code_hash_nft_id_nft_id_utxo_get(code_hash, nft_id)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_auction_code_hash_code_hash_nft_id_nft_id_utxo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_hash** | **str**| Code hash of the token. |
 **nft_id** | **str**| Nft id of this auction. |

### Return type

[**[ContractNftAuctionUtxo]**](ContractNftAuctionUtxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract nft sell utxo success. |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_genesis_code_hash_genesis_summary_get**
> [ContractNftGenesisSummary] contract_nft_genesis_code_hash_genesis_summary_get(code_hash, genesis)

Get nft summary(count group by address) for specific codeHash and genesisId(result cached for 60s).

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_nft_genesis_summary import ContractNftGenesisSummary
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
    api_instance = contract_api.ContractApi(api_client)
    code_hash = "codeHash_example" # str | Code hash of the token.
    genesis = "genesis_example" # str | Contract genesis

    # example passing only required values which don't have defaults set
    try:
        # Get nft summary(count group by address) for specific codeHash and genesisId(result cached for 60s).
        api_response = api_instance.contract_nft_genesis_code_hash_genesis_summary_get(code_hash, genesis)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_genesis_code_hash_genesis_utxo_get**
> [ContractNftUtxo] contract_nft_genesis_code_hash_genesis_utxo_get(code_hash, genesis)

Get all contract nft token utxos by codeHash and genesisId.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_nft_utxo import ContractNftUtxo
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
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_genesis_code_hash_genesis_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract nft token utxos by codeHash and genesisId.
        api_response = api_instance.contract_nft_genesis_code_hash_genesis_utxo_get(code_hash, genesis, token_index=token_index, max=max, min=min)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_sell_address_address_utxo_get**
> [ContractNftSellUtxo] contract_nft_sell_address_address_utxo_get(address)

Get all contract sell sell utxos for specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_nft_sell_utxo import ContractNftSellUtxo
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
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_sell_address_address_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract sell sell utxos for specific address.
        api_response = api_instance.contract_nft_sell_address_address_utxo_get(address, code_hash=code_hash, genesis=genesis, flag=flag)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_sell_genesis_code_hash_genesis_utxo_get**
> [ContractNftSellUtxo] contract_nft_sell_genesis_code_hash_genesis_utxo_get(code_hash, genesis)

Get all contract nft token utxos by codeHash and genesisId.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_nft_sell_utxo import ContractNftSellUtxo
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
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_sell_genesis_code_hash_genesis_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract nft token utxos by codeHash and genesisId.
        api_response = api_instance.contract_nft_sell_genesis_code_hash_genesis_utxo_get(code_hash, genesis, token_index=token_index, max=max, min=min)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_sell_v2_address_address_utxo_get**
> [ContractNftSellV2Utxo] contract_nft_sell_v2_address_address_utxo_get(address)

Get all contract sell sell utxos for specific address.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_nft_sell_v2_utxo import ContractNftSellV2Utxo
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
    api_instance = contract_api.ContractApi(api_client)
    address = "address_example" # str | Owner address.
    code_hash = "codeHash_example" # str | Filter by contract code hash (optional)
    genesis = "genesis_example" # str | Filter by contract genesis (optional)
    flag = "flag_example" # str | The flag of the last query Item(Paging flag) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all contract sell sell utxos for specific address.
        api_response = api_instance.contract_nft_sell_v2_address_address_utxo_get(address)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_sell_v2_address_address_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract sell sell utxos for specific address.
        api_response = api_instance.contract_nft_sell_v2_address_address_utxo_get(address, code_hash=code_hash, genesis=genesis, flag=flag)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_sell_v2_address_address_utxo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Owner address. |
 **code_hash** | **str**| Filter by contract code hash | [optional]
 **genesis** | **str**| Filter by contract genesis | [optional]
 **flag** | **str**| The flag of the last query Item(Paging flag) | [optional]

### Return type

[**[ContractNftSellV2Utxo]**](ContractNftSellV2Utxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract nft sell utxo success. |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_nft_sell_v2_genesis_code_hash_genesis_utxo_get**
> [ContractNftSellV2Utxo] contract_nft_sell_v2_genesis_code_hash_genesis_utxo_get(code_hash, genesis)

Get all contract nft token utxos by codeHash and genesisId.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_nft_sell_v2_utxo import ContractNftSellV2Utxo
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
    api_instance = contract_api.ContractApi(api_client)
    code_hash = "codeHash_example" # str | Code hash of the token.
    genesis = "genesis_example" # str | Contract genesis
    token_index = 1 # int | Find exact token Index. (optional)
    max = 1 # int | Token index not bigger than this(include this). (optional)
    min = 1 # int | Token index not less than this(include this). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all contract nft token utxos by codeHash and genesisId.
        api_response = api_instance.contract_nft_sell_v2_genesis_code_hash_genesis_utxo_get(code_hash, genesis)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_sell_v2_genesis_code_hash_genesis_utxo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all contract nft token utxos by codeHash and genesisId.
        api_response = api_instance.contract_nft_sell_v2_genesis_code_hash_genesis_utxo_get(code_hash, genesis, token_index=token_index, max=max, min=min)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
        print("Exception when calling ContractApi->contract_nft_sell_v2_genesis_code_hash_genesis_utxo_get: %s\n" % e)
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

[**[ContractNftSellV2Utxo]**](ContractNftSellV2Utxo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get contract nft sell utxo success. |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_unique_genesis_code_hash_genesis_utxo_get**
> [ContractUniqueUtxo] contract_unique_genesis_code_hash_genesis_utxo_get(code_hash, genesis)

Get contract unique utxos by codeHash and genesisId.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import metasv_mvc_client
from metasv_mvc_client.api import contract_api
from metasv_mvc_client.model.contract_unique_utxo import ContractUniqueUtxo
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
    api_instance = contract_api.ContractApi(api_client)
    code_hash = "codeHash_example" # str | Code hash of the token.
    genesis = "genesis_example" # str | Contract genesis

    # example passing only required values which don't have defaults set
    try:
        # Get contract unique utxos by codeHash and genesisId.
        api_response = api_instance.contract_unique_genesis_code_hash_genesis_utxo_get(code_hash, genesis)
        pprint(api_response)
    except metasv_mvc_client.ApiException as e:
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
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

