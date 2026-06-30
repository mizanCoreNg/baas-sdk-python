# StoreWebhookSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**events** | **List[str]** |  | [optional] 
**is_active** | **bool** | Optional field (included only when present in request) | [optional] 

## Example

```python
from mizancore_baas_generated.models.store_webhook_subscription_request import StoreWebhookSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoreWebhookSubscriptionRequest from a JSON string
store_webhook_subscription_request_instance = StoreWebhookSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(StoreWebhookSubscriptionRequest.to_json())

# convert the object into a dict
store_webhook_subscription_request_dict = store_webhook_subscription_request_instance.to_dict()
# create an instance of StoreWebhookSubscriptionRequest from a dict
store_webhook_subscription_request_from_dict = StoreWebhookSubscriptionRequest.from_dict(store_webhook_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


