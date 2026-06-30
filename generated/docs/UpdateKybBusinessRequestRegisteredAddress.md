# UpdateKybBusinessRequestRegisteredAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.update_kyb_business_request_registered_address import UpdateKybBusinessRequestRegisteredAddress

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKybBusinessRequestRegisteredAddress from a JSON string
update_kyb_business_request_registered_address_instance = UpdateKybBusinessRequestRegisteredAddress.from_json(json)
# print the JSON string representation of the object
print(UpdateKybBusinessRequestRegisteredAddress.to_json())

# convert the object into a dict
update_kyb_business_request_registered_address_dict = update_kyb_business_request_registered_address_instance.to_dict()
# create an instance of UpdateKybBusinessRequestRegisteredAddress from a dict
update_kyb_business_request_registered_address_from_dict = UpdateKybBusinessRequestRegisteredAddress.from_dict(update_kyb_business_request_registered_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


