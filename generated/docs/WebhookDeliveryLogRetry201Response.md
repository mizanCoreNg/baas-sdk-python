# WebhookDeliveryLogRetry201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**WebhookDeliveryLogRetry201ResponseData**](WebhookDeliveryLogRetry201ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.webhook_delivery_log_retry201_response import WebhookDeliveryLogRetry201Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryLogRetry201Response from a JSON string
webhook_delivery_log_retry201_response_instance = WebhookDeliveryLogRetry201Response.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryLogRetry201Response.to_json())

# convert the object into a dict
webhook_delivery_log_retry201_response_dict = webhook_delivery_log_retry201_response_instance.to_dict()
# create an instance of WebhookDeliveryLogRetry201Response from a dict
webhook_delivery_log_retry201_response_from_dict = WebhookDeliveryLogRetry201Response.from_dict(webhook_delivery_log_retry201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


