# WebhookDeliveryLogResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**event_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**attempt_count** | **int** |  | [optional] 
**max_attempts** | **str** |  | [optional] 
**last_status_code** | **str** |  | [optional] 
**last_error** | **str** |  | [optional] 
**response_time_ms** | **str** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**delivered_at** | **datetime** |  | [optional] 
**failed_at** | **datetime** |  | [optional] 
**next_retry_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.webhook_delivery_log_resource import WebhookDeliveryLogResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryLogResource from a JSON string
webhook_delivery_log_resource_instance = WebhookDeliveryLogResource.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryLogResource.to_json())

# convert the object into a dict
webhook_delivery_log_resource_dict = webhook_delivery_log_resource_instance.to_dict()
# create an instance of WebhookDeliveryLogResource from a dict
webhook_delivery_log_resource_from_dict = WebhookDeliveryLogResource.from_dict(webhook_delivery_log_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


