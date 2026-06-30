# IndexPartnerTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Optional field (included only when present in request) | [optional] 
**status** | **str** | Optional field (included only when present in request) | [optional] 
**var_from** | **date** | Optional field (included only when present in request) | [optional] 
**to** | **date** | Optional field (included only when present in request) | [optional] 
**reference** | **str** | Optional field (included only when present in request) | [optional] 
**session_id** | **str** | Optional field (included only when present in request) | [optional] 
**virtual_account_id** | **str** | Optional field (included only when present in request) | [optional] 
**per_page** | **int** | Optional field (included only when present in request) | [optional] 

## Example

```python
from mizancore_baas_generated.models.index_partner_transaction_request import IndexPartnerTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IndexPartnerTransactionRequest from a JSON string
index_partner_transaction_request_instance = IndexPartnerTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(IndexPartnerTransactionRequest.to_json())

# convert the object into a dict
index_partner_transaction_request_dict = index_partner_transaction_request_instance.to_dict()
# create an instance of IndexPartnerTransactionRequest from a dict
index_partner_transaction_request_from_dict = IndexPartnerTransactionRequest.from_dict(index_partner_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


