# XPubTransaction

Xpub transaction history
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xpub** | **str** | query xpub | [optional] 
**txid** | **str** | Txid for this transaction. | [optional] 
**max_receive_index** | **int** | Max lookahead receive index when processing this transaction. | [optional] 
**max_change_index** | **int** | Max lookahead change index when processing this transaction. | [optional] 
**income** | **int** | Total received satoshis(Including all address) | [optional] 
**outcome** | **int** | Total spent satoshis(Including all address) | [optional] 
**height** | **int** | Height for this transaction. -1 for unconfirmed | [optional] 
**block_index** | **int** | Block index for this transaction, -1 for unconfirmed | [optional] 
**block_time** | **int** | Block timestamp for this transaction, if unconfirmed, the time is first seen time. | [optional] 
**flag** | **str** | Paging flag, format blockTimestamp_blockIndex | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


