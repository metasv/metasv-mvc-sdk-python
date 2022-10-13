# ContractFtUtxo

Contract fungible token Utxo belongs to the specified address
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address string of this utxo | [optional] 
**code_hash** | **str** | Codehash of this utxo. | [optional] 
**genesis** | **str** | Genesis of this utxo. | [optional] 
**name** | **str** | Name of the token. | [optional] 
**symbol** | **str** | Symbol of the token. | [optional] 
**sensible_id** | **str** | SensibleId of the token | [optional] 
**decimal** | **int** | The decimal position. | [optional] 
**txid** | **str** | Txid for this utxo. | [optional] 
**tx_index** | **int** | Output index for the Utxo. | [optional] 
**value** | **int** | Token value of the utxo(Irrelavant to satoshi value). | [optional] 
**value_string** | **str** | Token value of the utxo(In string format) | [optional] 
**satoshi** | **int** | Mvc value of the utxo(Irrelavant to token value) | [optional] 
**satoshi_string** | **str** | Mvc value of the utxo(In string format) | [optional] 
**height** | **int** | The height of this utxo, -1 for unconfirmed utxo. | [optional] 
**flag** | **str** | Flag used for paging | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


