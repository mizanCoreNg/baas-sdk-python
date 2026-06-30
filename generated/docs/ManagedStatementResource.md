# ManagedStatementResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**current_balance_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**period** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**total_credits_kobo** | **str** |  | [optional] 
**total_debits_kobo** | **str** |  | [optional] 
**net_change_kobo** | **str** |  | [optional] 
**transaction_count** | **int** |  | [optional] 
**transactions** | **str** |  | [optional] 
**transaction_number** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**amount_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**fee_kobo** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**narration** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**value_date** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.managed_statement_resource import ManagedStatementResource

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedStatementResource from a JSON string
managed_statement_resource_instance = ManagedStatementResource.from_json(json)
# print the JSON string representation of the object
print(ManagedStatementResource.to_json())

# convert the object into a dict
managed_statement_resource_dict = managed_statement_resource_instance.to_dict()
# create an instance of ManagedStatementResource from a dict
managed_statement_resource_from_dict = ManagedStatementResource.from_dict(managed_statement_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


