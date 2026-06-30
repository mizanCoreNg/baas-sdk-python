# SetManagedCardLimitsRequestLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily_atm** | **int** | Optional field (included only when present in request) | [optional] 
**daily_pos** | **int** | Optional field (included only when present in request) | [optional] 
**daily_web** | **int** | Optional field (included only when present in request) | [optional] 
**per_transaction** | **int** | Optional field (included only when present in request) | [optional] 

## Example

```python
from mizancore_baas_generated.models.set_managed_card_limits_request_limits import SetManagedCardLimitsRequestLimits

# TODO update the JSON string below
json = "{}"
# create an instance of SetManagedCardLimitsRequestLimits from a JSON string
set_managed_card_limits_request_limits_instance = SetManagedCardLimitsRequestLimits.from_json(json)
# print the JSON string representation of the object
print(SetManagedCardLimitsRequestLimits.to_json())

# convert the object into a dict
set_managed_card_limits_request_limits_dict = set_managed_card_limits_request_limits_instance.to_dict()
# create an instance of SetManagedCardLimitsRequestLimits from a dict
set_managed_card_limits_request_limits_from_dict = SetManagedCardLimitsRequestLimits.from_dict(set_managed_card_limits_request_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


