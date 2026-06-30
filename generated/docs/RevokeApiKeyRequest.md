# RevokeApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Optional field (included only when present in request) | [optional] 

## Example

```python
from mizancore_baas_generated.models.revoke_api_key_request import RevokeApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeApiKeyRequest from a JSON string
revoke_api_key_request_instance = RevokeApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeApiKeyRequest.to_json())

# convert the object into a dict
revoke_api_key_request_dict = revoke_api_key_request_instance.to_dict()
# create an instance of RevokeApiKeyRequest from a dict
revoke_api_key_request_from_dict = RevokeApiKeyRequest.from_dict(revoke_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


