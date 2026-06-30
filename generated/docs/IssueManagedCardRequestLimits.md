# IssueManagedCardRequestLimits

Optional field (included only when present in request)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily_pos** | **int** | Optional field (included only when present in request) | [optional] 
**daily_atm** | **int** | Optional field (included only when present in request) | [optional] 
**daily_web** | **int** | Optional field (included only when present in request) | [optional] 

## Example

```python
from mizancore_baas_generated.models.issue_managed_card_request_limits import IssueManagedCardRequestLimits

# TODO update the JSON string below
json = "{}"
# create an instance of IssueManagedCardRequestLimits from a JSON string
issue_managed_card_request_limits_instance = IssueManagedCardRequestLimits.from_json(json)
# print the JSON string representation of the object
print(IssueManagedCardRequestLimits.to_json())

# convert the object into a dict
issue_managed_card_request_limits_dict = issue_managed_card_request_limits_instance.to_dict()
# create an instance of IssueManagedCardRequestLimits from a dict
issue_managed_card_request_limits_from_dict = IssueManagedCardRequestLimits.from_dict(issue_managed_card_request_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


