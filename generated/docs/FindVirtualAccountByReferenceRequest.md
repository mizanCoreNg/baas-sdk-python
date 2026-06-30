# FindVirtualAccountByReferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | **str** |  | 

## Example

```python
from mizancore_baas_generated.models.find_virtual_account_by_reference_request import FindVirtualAccountByReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FindVirtualAccountByReferenceRequest from a JSON string
find_virtual_account_by_reference_request_instance = FindVirtualAccountByReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(FindVirtualAccountByReferenceRequest.to_json())

# convert the object into a dict
find_virtual_account_by_reference_request_dict = find_virtual_account_by_reference_request_instance.to_dict()
# create an instance of FindVirtualAccountByReferenceRequest from a dict
find_virtual_account_by_reference_request_from_dict = FindVirtualAccountByReferenceRequest.from_dict(find_virtual_account_by_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


