# UpdateKybBusinessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_type** | **str** |  | 
**rc_number** | **str** |  | 
**legal_name** | **str** |  | 
**tax_id** | **str** |  | [optional] 
**registered_address** | [**UpdateKybBusinessRequestRegisteredAddress**](UpdateKybBusinessRequestRegisteredAddress.md) |  | 

## Example

```python
from mizancore_baas_generated.models.update_kyb_business_request import UpdateKybBusinessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKybBusinessRequest from a JSON string
update_kyb_business_request_instance = UpdateKybBusinessRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateKybBusinessRequest.to_json())

# convert the object into a dict
update_kyb_business_request_dict = update_kyb_business_request_instance.to_dict()
# create an instance of UpdateKybBusinessRequest from a dict
update_kyb_business_request_from_dict = UpdateKybBusinessRequest.from_dict(update_kyb_business_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


