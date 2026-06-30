# DeveloperKybOfficersAdd201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**date_of_birth** | **datetime** |  | [optional] 
**role** | **str** |  | [optional] 
**ownership_percentage** | **str** |  | [optional] 
**bvn_masked** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.developer_kyb_officers_add201_response_data import DeveloperKybOfficersAdd201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperKybOfficersAdd201ResponseData from a JSON string
developer_kyb_officers_add201_response_data_instance = DeveloperKybOfficersAdd201ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeveloperKybOfficersAdd201ResponseData.to_json())

# convert the object into a dict
developer_kyb_officers_add201_response_data_dict = developer_kyb_officers_add201_response_data_instance.to_dict()
# create an instance of DeveloperKybOfficersAdd201ResponseData from a dict
developer_kyb_officers_add201_response_data_from_dict = DeveloperKybOfficersAdd201ResponseData.from_dict(developer_kyb_officers_add201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


