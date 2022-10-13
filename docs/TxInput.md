# TxInput

Parsed inputs from raw tx. Use output api to get value and spent info.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Input index of the tx. | [optional] 
**utxo_txid** | **str** | The outpoint utxo txid that this input spent | [optional] 
**utxo_index** | **int** | The outpoint utxo index that this input spent | [optional] 
**address** | **str** | Parsed address from pubkey(P2PKH input only). | [optional] 
**value** | **int** | satoshi value of this input. | [optional] 
**unlock_script** | **str** | The hex of the input script. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


