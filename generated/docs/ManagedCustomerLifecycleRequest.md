# ManagedCustomerLifecycleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.managed_customer_lifecycle_request import ManagedCustomerLifecycleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedCustomerLifecycleRequest from a JSON string
managed_customer_lifecycle_request_instance = ManagedCustomerLifecycleRequest.from_json(json)
# print the JSON string representation of the object
print(ManagedCustomerLifecycleRequest.to_json())

# convert the object into a dict
managed_customer_lifecycle_request_dict = managed_customer_lifecycle_request_instance.to_dict()
# create an instance of ManagedCustomerLifecycleRequest from a dict
managed_customer_lifecycle_request_from_dict = ManagedCustomerLifecycleRequest.from_dict(managed_customer_lifecycle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


