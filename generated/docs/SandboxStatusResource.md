# SandboxStatusResource


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
from mizancore_baas_generated.models.sandbox_status_resource import SandboxStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of SandboxStatusResource from a JSON string
sandbox_status_resource_instance = SandboxStatusResource.from_json(json)
# print the JSON string representation of the object
print(SandboxStatusResource.to_json())

# convert the object into a dict
sandbox_status_resource_dict = sandbox_status_resource_instance.to_dict()
# create an instance of SandboxStatusResource from a dict
sandbox_status_resource_from_dict = SandboxStatusResource.from_dict(sandbox_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


