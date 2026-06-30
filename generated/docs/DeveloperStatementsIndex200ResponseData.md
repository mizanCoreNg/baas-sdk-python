# DeveloperStatementsIndex200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**period** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**virtual_account_id** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**opening_balance_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**total_credit_kobo** | **str** |  | [optional] 
**total_debit_kobo** | **str** |  | [optional] 
**closing_balance_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**movement_count** | **int** |  | [optional] 
**movements** | **str** |  | [optional] 
**summaries** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.developer_statements_index200_response_data import DeveloperStatementsIndex200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperStatementsIndex200ResponseData from a JSON string
developer_statements_index200_response_data_instance = DeveloperStatementsIndex200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeveloperStatementsIndex200ResponseData.to_json())

# convert the object into a dict
developer_statements_index200_response_data_dict = developer_statements_index200_response_data_instance.to_dict()
# create an instance of DeveloperStatementsIndex200ResponseData from a dict
developer_statements_index200_response_data_from_dict = DeveloperStatementsIndex200ResponseData.from_dict(developer_statements_index200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


