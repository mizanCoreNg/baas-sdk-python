# UpdateKybOfficerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** | Optional field (included only when present in request) | [optional] 
**date_of_birth** | **date** | Optional field (included only when present in request) | [optional] 
**bvn** | **str** | Optional field (included only when present in request) | [optional] 
**role** | **str** | Optional field (included only when present in request) | [optional] 
**ownership_percentage** | **int** | Optional field (included only when present in request) | [optional] 

## Example

```python
from mizancore_baas_generated.models.update_kyb_officer_request import UpdateKybOfficerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKybOfficerRequest from a JSON string
update_kyb_officer_request_instance = UpdateKybOfficerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateKybOfficerRequest.to_json())

# convert the object into a dict
update_kyb_officer_request_dict = update_kyb_officer_request_instance.to_dict()
# create an instance of UpdateKybOfficerRequest from a dict
update_kyb_officer_request_from_dict = UpdateKybOfficerRequest.from_dict(update_kyb_officer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


