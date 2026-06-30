# VirtualAccountQueryIndex200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**VirtualAccountQueryIndex200ResponseData**](VirtualAccountQueryIndex200ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.virtual_account_query_index200_response import VirtualAccountQueryIndex200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountQueryIndex200Response from a JSON string
virtual_account_query_index200_response_instance = VirtualAccountQueryIndex200Response.from_json(json)
# print the JSON string representation of the object
print(VirtualAccountQueryIndex200Response.to_json())

# convert the object into a dict
virtual_account_query_index200_response_dict = virtual_account_query_index200_response_instance.to_dict()
# create an instance of VirtualAccountQueryIndex200Response from a dict
virtual_account_query_index200_response_from_dict = VirtualAccountQueryIndex200Response.from_dict(virtual_account_query_index200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


