# ManagedCustomerStatementShow200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**ManagedCustomerStatementShow200ResponseData**](ManagedCustomerStatementShow200ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.managed_customer_statement_show200_response import ManagedCustomerStatementShow200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedCustomerStatementShow200Response from a JSON string
managed_customer_statement_show200_response_instance = ManagedCustomerStatementShow200Response.from_json(json)
# print the JSON string representation of the object
print(ManagedCustomerStatementShow200Response.to_json())

# convert the object into a dict
managed_customer_statement_show200_response_dict = managed_customer_statement_show200_response_instance.to_dict()
# create an instance of ManagedCustomerStatementShow200Response from a dict
managed_customer_statement_show200_response_from_dict = ManagedCustomerStatementShow200Response.from_dict(managed_customer_statement_show200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


