# XpubRequest

Request object to register(or delete) a new xpub
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xpub** | **str** | The xpub to register. | [optional] 
**skip_height** | **int** | Skip transactions before this height. Default is 0. Ignore this while deleting xpub. | [optional] 
**init_receive_index** | **int** | Set the init maxReceiveIndex to {initReceiveIndex}(less than 5000) before the initial crawl , default is 200. This could increase cost. | [optional] 
**init_change_index** | **int** | Set the init maxChangeIndex(less than 5000) before the initial crawl , default is 200. This could increase cost. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


