# RegisterDeveloperRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | 
**contact_email** | **str** |  | 
**contact_name** | **str** |  | 
**use_case_description** | **str** |  | 
**website_url** | **str** | Optional field (included only when present in request) | [optional] 
**password** | **str** | Must match password_confirmation field | 

## Example

```python
from mizancore_baas_generated.models.register_developer_request import RegisterDeveloperRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterDeveloperRequest from a JSON string
register_developer_request_instance = RegisterDeveloperRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterDeveloperRequest.to_json())

# convert the object into a dict
register_developer_request_dict = register_developer_request_instance.to_dict()
# create an instance of RegisterDeveloperRequest from a dict
register_developer_request_from_dict = RegisterDeveloperRequest.from_dict(register_developer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


