# XpubDetail

Registered Xpub detail
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xpub** | **str** | String encoded extended pubkey (xpub) | [optional] 
**receive_index** | **int** | Next unused receive index, path /0/index | [optional] 
**max_receive_index** | **int** | Max lookahead receive index. | [optional] 
**change_index** | **int** | Next unused change index, path /1/index | [optional] 
**max_change_index** | **int** | Max lookahead change index. | [optional] 
**mode** | **int** | Current xpub process mode, 0 means preparing(not ready), 1 means synchronizing(ready) | [optional] 
**skip_height** | **int** | Skip blocks before skipHeight while searching transactions. This will speed up sync time. | [optional] 
**process_height** | **int** | Xpub current processed height. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


