# ContractNftSellV2Utxo

Contract nft sell v2 Utxo belongs to the specified address
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address string of this utxo | [optional] 
**contract_address** | **str** | Address calculated from contract hash(p2ch). | [optional] 
**txid** | **str** | Txid for this utxo. | [optional] 
**tx_index** | **int** | Output index for the Utxo. | [optional] 
**code_hash** | **str** | Codehash of this utxo. | [optional] 
**genesis** | **str** | Genesis of this utxo. | [optional] 
**token_index** | **int** | The index of this NFT. | [optional] 
**price** | **int** | the price of nft. | [optional] 
**fee_address_pkh** | **str** | The address to receive fees. | [optional] 
**fee_rate** | **int** | feeRate | [optional] 
**nft_id** | **str** | nftId | [optional] 
**seller_address_pkh** | **str** | The address pkh of seller | [optional] 
**satoshi** | **int** | Mvc value of the utxo(Irrelavant to token value) | [optional] 
**satoshi_string** | **str** | Mvc value of the utxo(In string format) | [optional] 
**height** | **int** | The height of this utxo, -1 for unconfirmed utxo. | [optional] 
**is_ready** | **bool** | Is current nft transfered into sell contract, If not ready, the following fields will be null | [optional] 
**sensible_id** | **str** | SensibleId of the token | [optional] 
**meta_txid** | **str** | The metanet tx describing the nft. | [optional] 
**meta_output_index** | **int** | Symbol of the token. | [optional] 
**token_supply** | **int** | The total supply of this NFT. | [optional] 
**flag** | **str** | Flag used for paging | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


