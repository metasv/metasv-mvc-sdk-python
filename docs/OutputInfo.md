# OutputInfo

spent status and value info of the output.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txid** | **str** | txid that this output is in. | [optional] 
**index** | **int** | index of this output in the tx. | [optional] 
**address** | **str** | parsed address of this output, empty for non standard. | [optional] 
**value** | **int** | value of this output | [optional] 
**spent** | **bool** | this output is spent or not, true if spent | [optional] 
**spent_txid** | **str** | txid that spent this output | [optional] 
**spent_index** | **int** | vin index of the spent tx | [optional] 
**spent_height** | **int** | height of the spent tx(-1 if unconfirmed, 0 if unspent) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


