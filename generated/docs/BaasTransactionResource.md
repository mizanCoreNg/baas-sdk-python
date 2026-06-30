# BaasTransactionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**transaction_type_label** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**amount** | **int** | Amount in kobo (minor currency units). | [optional] 
**amount_naira** | **int** | Amount in kobo (minor currency units). | [optional] 
**fee_amount** | **int** | Amount in kobo (minor currency units). | [optional] 
**fee_amount_naira** | **int** | Amount in kobo (minor currency units). | [optional] 
**net_amount** | **int** | Amount in kobo (minor currency units). | [optional] 
**net_amount_naira** | **int** | Amount in kobo (minor currency units). | [optional] 
**currency** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**narration** | **str** |  | [optional] 
**sender_name** | **str** |  | [optional] 
**sender_account** | **str** |  | [optional] 
**sender_bank** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.baas_transaction_resource import BaasTransactionResource

# TODO update the JSON string below
json = "{}"
# create an instance of BaasTransactionResource from a JSON string
baas_transaction_resource_instance = BaasTransactionResource.from_json(json)
# print the JSON string representation of the object
print(BaasTransactionResource.to_json())

# convert the object into a dict
baas_transaction_resource_dict = baas_transaction_resource_instance.to_dict()
# create an instance of BaasTransactionResource from a dict
baas_transaction_resource_from_dict = BaasTransactionResource.from_dict(baas_transaction_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


