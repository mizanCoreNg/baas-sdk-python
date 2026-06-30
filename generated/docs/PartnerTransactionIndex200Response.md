# PartnerTransactionIndex200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**PartnerTransactionIndex200ResponseData**](PartnerTransactionIndex200ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_transaction_index200_response import PartnerTransactionIndex200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerTransactionIndex200Response from a JSON string
partner_transaction_index200_response_instance = PartnerTransactionIndex200Response.from_json(json)
# print the JSON string representation of the object
print(PartnerTransactionIndex200Response.to_json())

# convert the object into a dict
partner_transaction_index200_response_dict = partner_transaction_index200_response_instance.to_dict()
# create an instance of PartnerTransactionIndex200Response from a dict
partner_transaction_index200_response_from_dict = PartnerTransactionIndex200Response.from_dict(partner_transaction_index200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


