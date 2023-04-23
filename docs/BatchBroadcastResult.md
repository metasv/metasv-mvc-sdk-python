# BatchBroadcastResult

Batch broadcast result
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**known** | **[str]** | Already known transactions detected during processing (if there are any) | [optional] 
**evicted** | **[str]** | Transactions accepted by the mempool and then evicted due to insufficient fee (if there are any) | [optional] 
**invalid** | [**[InvalidBroadCast]**](InvalidBroadCast.md) | Transactions that failed to be accepted by the mempool (if there are any) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


