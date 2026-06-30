# WebhookDeliveryResource


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
from mizancore_baas_generated.models.webhook_delivery_resource import WebhookDeliveryResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryResource from a JSON string
webhook_delivery_resource_instance = WebhookDeliveryResource.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryResource.to_json())

# convert the object into a dict
webhook_delivery_resource_dict = webhook_delivery_resource_instance.to_dict()
# create an instance of WebhookDeliveryResource from a dict
webhook_delivery_resource_from_dict = WebhookDeliveryResource.from_dict(webhook_delivery_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


