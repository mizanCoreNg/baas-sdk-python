# DeveloperApiKeyStore201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**key_prefix** | **str** |  | [optional] 
**scopes** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**ip_allowlist** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**last_used_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**revoked_at** | **datetime** |  | [optional] 
**in_grace_period** | **str** |  | [optional] 
**previous_key_expires_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.developer_api_key_store201_response_data import DeveloperApiKeyStore201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperApiKeyStore201ResponseData from a JSON string
developer_api_key_store201_response_data_instance = DeveloperApiKeyStore201ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeveloperApiKeyStore201ResponseData.to_json())

# convert the object into a dict
developer_api_key_store201_response_data_dict = developer_api_key_store201_response_data_instance.to_dict()
# create an instance of DeveloperApiKeyStore201ResponseData from a dict
developer_api_key_store201_response_data_from_dict = DeveloperApiKeyStore201ResponseData.from_dict(developer_api_key_store201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


