# GenerateStatementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **date** |  | 
**to** | **date** |  | 
**virtual_account_id** | **str** | Optional field (included only when present in request) | [optional] 

## Example

```python
from mizancore_baas_generated.models.generate_statement_request import GenerateStatementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateStatementRequest from a JSON string
generate_statement_request_instance = GenerateStatementRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateStatementRequest.to_json())

# convert the object into a dict
generate_statement_request_dict = generate_statement_request_instance.to_dict()
# create an instance of GenerateStatementRequest from a dict
generate_statement_request_from_dict = GenerateStatementRequest.from_dict(generate_statement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


