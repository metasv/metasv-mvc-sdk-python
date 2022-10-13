# ContractUniqueUtxo

Contract unique Utxo indexed by codeHash and genesis.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txid** | **str** | Txid for this utxo. | [optional] 
**tx_index** | **int** | Output index for the Utxo. | [optional] 
**code_hash** | **str** | Codehash of this utxo. | [optional] 
**genesis** | **str** | Genesis of this utxo. | [optional] 
**sensible_id** | **str** | SensibleId of the token | [optional] 
**height** | **int** | The height of this utxo, -1 for unconfirmed utxo. | [optional] 
**custom_data** | **str** | The hex encoded customData | [optional] 
**satoshi** | **int** | Mvc value of the utxo(Irrelavant to token value) | [optional] 
**satoshi_string** | **str** | Mvc value of the utxo(In string format) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


