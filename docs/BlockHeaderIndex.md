# BlockHeaderIndex

Detailed block header info.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_hash** | **str** | Block hash. | [optional] 
**height** | **int** | Block height. | [optional] 
**version** | **int** | Block version. | [optional] 
**prev_block_hash** | **str** | The block hash of the previous block. | [optional] 
**merkle_root** | **str** | Hex formatted block merkle root. | [optional] 
**timestamp** | **int** | Block timestamp. | [optional] 
**median_time** | **int** | Block median timestamp. | [optional] 
**reward** | **int** | Miner total rewards, including miner fee. | [optional] 
**miner** | **str** | Guessed miner name. | [optional] 
**miner_address** | **str** | Miner address that received rewards. | [optional] 
**tx_count** | **int** | Total txs count included in the block. | [optional] 
**input_count** | **int** | Total input count in the block. | [optional] 
**output_count** | **int** | Total output count in the block | [optional] 
**size** | **int** | Size of the block | [optional] 
**bits** | **int** | Target bits. | [optional] 
**nonce** | **int** | Block nonce | [optional] 
**coinbase** | **str** | Hex formated coinbase info. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


