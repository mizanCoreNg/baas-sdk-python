# OpenManagedAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**nickname** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.open_managed_account_request import OpenManagedAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenManagedAccountRequest from a JSON string
open_managed_account_request_instance = OpenManagedAccountRequest.from_json(json)
# print the JSON string representation of the object
print(OpenManagedAccountRequest.to_json())

# convert the object into a dict
open_managed_account_request_dict = open_managed_account_request_instance.to_dict()
# create an instance of OpenManagedAccountRequest from a dict
open_managed_account_request_from_dict = OpenManagedAccountRequest.from_dict(open_managed_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


