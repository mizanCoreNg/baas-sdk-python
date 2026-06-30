# SetManagedCardLimitsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**SetManagedCardLimitsRequestLimits**](SetManagedCardLimitsRequestLimits.md) |  | 

## Example

```python
from mizancore_baas_generated.models.set_managed_card_limits_request import SetManagedCardLimitsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetManagedCardLimitsRequest from a JSON string
set_managed_card_limits_request_instance = SetManagedCardLimitsRequest.from_json(json)
# print the JSON string representation of the object
print(SetManagedCardLimitsRequest.to_json())

# convert the object into a dict
set_managed_card_limits_request_dict = set_managed_card_limits_request_instance.to_dict()
# create an instance of SetManagedCardLimitsRequest from a dict
set_managed_card_limits_request_from_dict = SetManagedCardLimitsRequest.from_dict(set_managed_card_limits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


