# WebhookSubscriptionOperationsDeliveries200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**event_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**attempts** | **str** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**delivered_at** | **datetime** |  | [optional] 
**last_attempt_at** | **datetime** |  | [optional] 
**next_retry_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.webhook_subscription_operations_deliveries200_response_data import WebhookSubscriptionOperationsDeliveries200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionOperationsDeliveries200ResponseData from a JSON string
webhook_subscription_operations_deliveries200_response_data_instance = WebhookSubscriptionOperationsDeliveries200ResponseData.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionOperationsDeliveries200ResponseData.to_json())

# convert the object into a dict
webhook_subscription_operations_deliveries200_response_data_dict = webhook_subscription_operations_deliveries200_response_data_instance.to_dict()
# create an instance of WebhookSubscriptionOperationsDeliveries200ResponseData from a dict
webhook_subscription_operations_deliveries200_response_data_from_dict = WebhookSubscriptionOperationsDeliveries200ResponseData.from_dict(webhook_subscription_operations_deliveries200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


