# DeveloperRegistrationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.developer_registration_resource import DeveloperRegistrationResource

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperRegistrationResource from a JSON string
developer_registration_resource_instance = DeveloperRegistrationResource.from_json(json)
# print the JSON string representation of the object
print(DeveloperRegistrationResource.to_json())

# convert the object into a dict
developer_registration_resource_dict = developer_registration_resource_instance.to_dict()
# create an instance of DeveloperRegistrationResource from a dict
developer_registration_resource_from_dict = DeveloperRegistrationResource.from_dict(developer_registration_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


