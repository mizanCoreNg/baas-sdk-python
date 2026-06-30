# WebhookSubscriptionDestroy204Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**WebhookSubscriptionDestroy204ResponseData**](WebhookSubscriptionDestroy204ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.webhook_subscription_destroy204_response import WebhookSubscriptionDestroy204Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionDestroy204Response from a JSON string
webhook_subscription_destroy204_response_instance = WebhookSubscriptionDestroy204Response.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionDestroy204Response.to_json())

# convert the object into a dict
webhook_subscription_destroy204_response_dict = webhook_subscription_destroy204_response_instance.to_dict()
# create an instance of WebhookSubscriptionDestroy204Response from a dict
webhook_subscription_destroy204_response_from_dict = WebhookSubscriptionDestroy204Response.from_dict(webhook_subscription_destroy204_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


