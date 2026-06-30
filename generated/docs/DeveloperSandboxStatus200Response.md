# DeveloperSandboxStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**DeveloperSandboxStatus200ResponseData**](DeveloperSandboxStatus200ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.developer_sandbox_status200_response import DeveloperSandboxStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperSandboxStatus200Response from a JSON string
developer_sandbox_status200_response_instance = DeveloperSandboxStatus200Response.from_json(json)
# print the JSON string representation of the object
print(DeveloperSandboxStatus200Response.to_json())

# convert the object into a dict
developer_sandbox_status200_response_dict = developer_sandbox_status200_response_instance.to_dict()
# create an instance of DeveloperSandboxStatus200Response from a dict
developer_sandbox_status200_response_from_dict = DeveloperSandboxStatus200Response.from_dict(developer_sandbox_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


