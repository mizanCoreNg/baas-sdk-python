# DeveloperLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from mizancore_baas_generated.models.developer_login_request import DeveloperLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperLoginRequest from a JSON string
developer_login_request_instance = DeveloperLoginRequest.from_json(json)
# print the JSON string representation of the object
print(DeveloperLoginRequest.to_json())

# convert the object into a dict
developer_login_request_dict = developer_login_request_instance.to_dict()
# create an instance of DeveloperLoginRequest from a dict
developer_login_request_from_dict = DeveloperLoginRequest.from_dict(developer_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


