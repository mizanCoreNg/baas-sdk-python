# SandboxTestDataResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_patterns** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.sandbox_test_data_resource import SandboxTestDataResource

# TODO update the JSON string below
json = "{}"
# create an instance of SandboxTestDataResource from a JSON string
sandbox_test_data_resource_instance = SandboxTestDataResource.from_json(json)
# print the JSON string representation of the object
print(SandboxTestDataResource.to_json())

# convert the object into a dict
sandbox_test_data_resource_dict = sandbox_test_data_resource_instance.to_dict()
# create an instance of SandboxTestDataResource from a dict
sandbox_test_data_resource_from_dict = SandboxTestDataResource.from_dict(sandbox_test_data_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


