# DeveloperKybShow200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**registration_type** | **str** |  | [optional] 
**rc_number** | **int** |  | [optional] 
**legal_name** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**registered_address** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**allows_live_access** | **str** |  | [optional] 
**rejection_reason** | **str** |  | [optional] 
**submitted_at** | **datetime** |  | [optional] 
**reviewed_at** | **datetime** |  | [optional] 
**officers** | **str** |  | [optional] 
**documents** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.developer_kyb_show200_response_data import DeveloperKybShow200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperKybShow200ResponseData from a JSON string
developer_kyb_show200_response_data_instance = DeveloperKybShow200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeveloperKybShow200ResponseData.to_json())

# convert the object into a dict
developer_kyb_show200_response_data_dict = developer_kyb_show200_response_data_instance.to_dict()
# create an instance of DeveloperKybShow200ResponseData from a dict
developer_kyb_show200_response_data_from_dict = DeveloperKybShow200ResponseData.from_dict(developer_kyb_show200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


