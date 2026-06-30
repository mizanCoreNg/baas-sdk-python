# WebhookSubscriptionIndex200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**WebhookSubscriptionIndex200ResponseData**](WebhookSubscriptionIndex200ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.webhook_subscription_index200_response import WebhookSubscriptionIndex200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionIndex200Response from a JSON string
webhook_subscription_index200_response_instance = WebhookSubscriptionIndex200Response.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionIndex200Response.to_json())

# convert the object into a dict
webhook_subscription_index200_response_dict = webhook_subscription_index200_response_instance.to_dict()
# create an instance of WebhookSubscriptionIndex200Response from a dict
webhook_subscription_index200_response_from_dict = WebhookSubscriptionIndex200Response.from_dict(webhook_subscription_index200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


