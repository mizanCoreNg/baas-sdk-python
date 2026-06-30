# IssueManagedCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** | Optional field (included only when present in request) | [optional] 
**limits** | [**IssueManagedCardRequestLimits**](IssueManagedCardRequestLimits.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.issue_managed_card_request import IssueManagedCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssueManagedCardRequest from a JSON string
issue_managed_card_request_instance = IssueManagedCardRequest.from_json(json)
# print the JSON string representation of the object
print(IssueManagedCardRequest.to_json())

# convert the object into a dict
issue_managed_card_request_dict = issue_managed_card_request_instance.to_dict()
# create an instance of IssueManagedCardRequest from a dict
issue_managed_card_request_from_dict = IssueManagedCardRequest.from_dict(issue_managed_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


