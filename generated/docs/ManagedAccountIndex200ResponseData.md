# ManagedAccountIndex200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**balance_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**nickname** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.managed_account_index200_response_data import ManagedAccountIndex200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedAccountIndex200ResponseData from a JSON string
managed_account_index200_response_data_instance = ManagedAccountIndex200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ManagedAccountIndex200ResponseData.to_json())

# convert the object into a dict
managed_account_index200_response_data_dict = managed_account_index200_response_data_instance.to_dict()
# create an instance of ManagedAccountIndex200ResponseData from a dict
managed_account_index200_response_data_from_dict = ManagedAccountIndex200ResponseData.from_dict(managed_account_index200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


