# TerminateManagedCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 

## Example

```python
from mizancore_baas_generated.models.terminate_managed_card_request import TerminateManagedCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateManagedCardRequest from a JSON string
terminate_managed_card_request_instance = TerminateManagedCardRequest.from_json(json)
# print the JSON string representation of the object
print(TerminateManagedCardRequest.to_json())

# convert the object into a dict
terminate_managed_card_request_dict = terminate_managed_card_request_instance.to_dict()
# create an instance of TerminateManagedCardRequest from a dict
terminate_managed_card_request_from_dict = TerminateManagedCardRequest.from_dict(terminate_managed_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


