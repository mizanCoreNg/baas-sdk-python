# DeveloperStatementsIndex200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**DeveloperStatementsIndex200ResponseData**](DeveloperStatementsIndex200ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.developer_statements_index200_response import DeveloperStatementsIndex200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperStatementsIndex200Response from a JSON string
developer_statements_index200_response_instance = DeveloperStatementsIndex200Response.from_json(json)
# print the JSON string representation of the object
print(DeveloperStatementsIndex200Response.to_json())

# convert the object into a dict
developer_statements_index200_response_dict = developer_statements_index200_response_instance.to_dict()
# create an instance of DeveloperStatementsIndex200Response from a dict
developer_statements_index200_response_from_dict = DeveloperStatementsIndex200Response.from_dict(developer_statements_index200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


