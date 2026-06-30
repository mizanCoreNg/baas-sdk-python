# WebhookDeliveryLogRetry201ResponseData


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
from mizancore_baas_generated.models.webhook_delivery_log_retry201_response_data import WebhookDeliveryLogRetry201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryLogRetry201ResponseData from a JSON string
webhook_delivery_log_retry201_response_data_instance = WebhookDeliveryLogRetry201ResponseData.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryLogRetry201ResponseData.to_json())

# convert the object into a dict
webhook_delivery_log_retry201_response_data_dict = webhook_delivery_log_retry201_response_data_instance.to_dict()
# create an instance of WebhookDeliveryLogRetry201ResponseData from a dict
webhook_delivery_log_retry201_response_data_from_dict = WebhookDeliveryLogRetry201ResponseData.from_dict(webhook_delivery_log_retry201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


