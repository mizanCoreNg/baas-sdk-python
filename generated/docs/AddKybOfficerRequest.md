# AddKybOfficerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**date_of_birth** | **date** |  | [optional] 
**bvn** | **str** |  | [optional] 
**role** | **str** |  | 
**ownership_percentage** | **int** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.add_kyb_officer_request import AddKybOfficerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddKybOfficerRequest from a JSON string
add_kyb_officer_request_instance = AddKybOfficerRequest.from_json(json)
# print the JSON string representation of the object
print(AddKybOfficerRequest.to_json())

# convert the object into a dict
add_kyb_officer_request_dict = add_kyb_officer_request_instance.to_dict()
# create an instance of AddKybOfficerRequest from a dict
add_kyb_officer_request_from_dict = AddKybOfficerRequest.from_dict(add_kyb_officer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


