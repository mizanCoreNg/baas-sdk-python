# SetManagedCardPinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin** | **str** |  | 
**current_pin** | **str** | Optional field (included only when present in request) | [optional] 

## Example

```python
from mizancore_baas_generated.models.set_managed_card_pin_request import SetManagedCardPinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetManagedCardPinRequest from a JSON string
set_managed_card_pin_request_instance = SetManagedCardPinRequest.from_json(json)
# print the JSON string representation of the object
print(SetManagedCardPinRequest.to_json())

# convert the object into a dict
set_managed_card_pin_request_dict = set_managed_card_pin_request_instance.to_dict()
# create an instance of SetManagedCardPinRequest from a dict
set_managed_card_pin_request_from_dict = SetManagedCardPinRequest.from_dict(set_managed_card_pin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


