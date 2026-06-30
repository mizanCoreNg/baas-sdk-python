# ListManagedCardTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_page** | **int** | Optional field (included only when present in request) | [optional] 
**page** | **int** | Optional field (included only when present in request) | [optional] 

## Example

```python
from mizancore_baas_generated.models.list_managed_card_transactions_request import ListManagedCardTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListManagedCardTransactionsRequest from a JSON string
list_managed_card_transactions_request_instance = ListManagedCardTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListManagedCardTransactionsRequest.to_json())

# convert the object into a dict
list_managed_card_transactions_request_dict = list_managed_card_transactions_request_instance.to_dict()
# create an instance of ListManagedCardTransactionsRequest from a dict
list_managed_card_transactions_request_from_dict = ListManagedCardTransactionsRequest.from_dict(list_managed_card_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


