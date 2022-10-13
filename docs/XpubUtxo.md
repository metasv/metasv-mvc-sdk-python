# XpubUtxo

Utxo belongs to the specified xpub
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xpub** | **str** | xpub of the utxo | [optional] 
**address** | **str** | Address string of this utxo | [optional] 
**address_type** | **int** | Address type, 0 for receive address, 1 for change address. path is {{addressType}}/{{addressIndex}} | [optional] 
**address_index** | **int** | Address index. Address path in the xpub is {{addressType}}/{{addressIndex}} | [optional] 
**txid** | **str** | Txid for this utxo. | [optional] 
**tx_index** | **int** | Output index for the Utxo. | [optional] 
**value** | **int** | Satoshi value of the utxo. | [optional] 
**height** | **int** | The height of this utxo, -1 for unconfirmed utxo. | [optional] 
**flag** | **int** | The paging flag of utxo | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


