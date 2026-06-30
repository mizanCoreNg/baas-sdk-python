# GenerateManagedStatementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **date** |  | 
**to** | **date** |  | 

## Example

```python
from mizancore_baas_generated.models.generate_managed_statement_request import GenerateManagedStatementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateManagedStatementRequest from a JSON string
generate_managed_statement_request_instance = GenerateManagedStatementRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateManagedStatementRequest.to_json())

# convert the object into a dict
generate_managed_statement_request_dict = generate_managed_statement_request_instance.to_dict()
# create an instance of GenerateManagedStatementRequest from a dict
generate_managed_statement_request_from_dict = GenerateManagedStatementRequest.from_dict(generate_managed_statement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


