# DeveloperApiKeyStore201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**DeveloperApiKeyStore201ResponseData**](DeveloperApiKeyStore201ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.developer_api_key_store201_response import DeveloperApiKeyStore201Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperApiKeyStore201Response from a JSON string
developer_api_key_store201_response_instance = DeveloperApiKeyStore201Response.from_json(json)
# print the JSON string representation of the object
print(DeveloperApiKeyStore201Response.to_json())

# convert the object into a dict
developer_api_key_store201_response_dict = developer_api_key_store201_response_instance.to_dict()
# create an instance of DeveloperApiKeyStore201Response from a dict
developer_api_key_store201_response_from_dict = DeveloperApiKeyStore201Response.from_dict(developer_api_key_store201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


