# ManagedCardReadTransactions200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**card_id** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**amount_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**fee_kobo** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**merchant_category_code** | **str** |  | [optional] 
**processor_reference** | **str** |  | [optional] 
**retrieval_reference** | **str** |  | [optional] 
**response_code** | **str** |  | [optional] 
**transaction_date** | **datetime** |  | [optional] 
**settlement_date** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.managed_card_read_transactions200_response_data import ManagedCardReadTransactions200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedCardReadTransactions200ResponseData from a JSON string
managed_card_read_transactions200_response_data_instance = ManagedCardReadTransactions200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ManagedCardReadTransactions200ResponseData.to_json())

# convert the object into a dict
managed_card_read_transactions200_response_data_dict = managed_card_read_transactions200_response_data_instance.to_dict()
# create an instance of ManagedCardReadTransactions200ResponseData from a dict
managed_card_read_transactions200_response_data_from_dict = ManagedCardReadTransactions200ResponseData.from_dict(managed_card_read_transactions200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


