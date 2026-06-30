# DeveloperSandboxStatus200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_sandbox** | **bool** |  | [optional] 
**environment** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**sandbox_enabled** | **str** |  | [optional] 
**mock_providers_available** | **str** |  | [optional] 
**test_data_available** | **str** |  | [optional] 
**last_reset_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.developer_sandbox_status200_response_data import DeveloperSandboxStatus200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperSandboxStatus200ResponseData from a JSON string
developer_sandbox_status200_response_data_instance = DeveloperSandboxStatus200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeveloperSandboxStatus200ResponseData.to_json())

# convert the object into a dict
developer_sandbox_status200_response_data_dict = developer_sandbox_status200_response_data_instance.to_dict()
# create an instance of DeveloperSandboxStatus200ResponseData from a dict
developer_sandbox_status200_response_data_from_dict = DeveloperSandboxStatus200ResponseData.from_dict(developer_sandbox_status200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


