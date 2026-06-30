# VirtualAccountQueryIndex200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**account_name** | **int** |  | [optional] 
**bank_code** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**max_uses** | **str** |  | [optional] 
**use_count** | **int** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**amount_validation** | **str** |  | [optional] 
**amount** | **str** | Conditional field — included when the relation is loaded. | [optional] 
**bvn** | **str** | Conditional field — included when the relation is loaded. | [optional] 
**nin** | **str** | Conditional field — included when the relation is loaded. | [optional] 
**verified_name** | **str** | Conditional field — included when the relation is loaded. | [optional] 
**verification_source** | **str** | Conditional field — included when the relation is loaded. | [optional] 
**is_verified** | **bool** |  | [optional] 
**company_name** | **str** | Conditional field — included when the relation is loaded. | [optional] 
**rc_number** | **str** | Conditional field — included when the relation is loaded. | [optional] 
**incorporation_date** | **datetime** |  | [optional] 
**director_bvn** | **str** | Conditional field — included when the relation is loaded. | [optional] 
**director_name** | **str** | Conditional field — included when the relation is loaded. | [optional] 
**customer_reference** | **str** |  | [optional] 
**customer_data** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**has_individual_balance** | **bool** |  | [optional] 
**balance** | **int** | Amount in kobo (minor currency units). | [optional] 
**available_balance** | **int** | Amount in kobo (minor currency units). | [optional] 
**ledger_account_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.virtual_account_query_index200_response_data import VirtualAccountQueryIndex200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountQueryIndex200ResponseData from a JSON string
virtual_account_query_index200_response_data_instance = VirtualAccountQueryIndex200ResponseData.from_json(json)
# print the JSON string representation of the object
print(VirtualAccountQueryIndex200ResponseData.to_json())

# convert the object into a dict
virtual_account_query_index200_response_data_dict = virtual_account_query_index200_response_data_instance.to_dict()
# create an instance of VirtualAccountQueryIndex200ResponseData from a dict
virtual_account_query_index200_response_data_from_dict = VirtualAccountQueryIndex200ResponseData.from_dict(virtual_account_query_index200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


