# ContractNftUtxo

Contract non fungible token Utxo belongs to the specified address
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address string of this utxo | [optional] 
**txid** | **str** | Txid for this utxo. | [optional] 
**tx_index** | **int** | Output index for the Utxo. | [optional] 
**code_hash** | **str** | Codehash of this utxo. | [optional] 
**genesis** | **str** | Genesis of this utxo. | [optional] 
**sensible_id** | **str** | SensibleId of the token | [optional] 
**height** | **int** | The height of this utxo, -1 for unconfirmed utxo. | [optional] 
**meta_txid** | **str** | The metanet tx describing the nft. | [optional] 
**meta_output_index** | **int** | Symbol of the token. | [optional] 
**token_supply** | **int** | The total supply of this NFT. | [optional] 
**token_index** | **int** | The index of this NFT. | [optional] 
**satoshi** | **int** | Mvc value of the utxo(Irrelavant to token value) | [optional] 
**satoshi_string** | **str** | Mvc value of the utxo(In string format) | [optional] 
**flag** | **str** | Flag used for paging | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


