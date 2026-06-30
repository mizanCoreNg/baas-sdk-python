# ApiKeyResource


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
from mizancore_baas_generated.models.api_key_resource import ApiKeyResource

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyResource from a JSON string
api_key_resource_instance = ApiKeyResource.from_json(json)
# print the JSON string representation of the object
print(ApiKeyResource.to_json())

# convert the object into a dict
api_key_resource_dict = api_key_resource_instance.to_dict()
# create an instance of ApiKeyResource from a dict
api_key_resource_from_dict = ApiKeyResource.from_dict(api_key_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


