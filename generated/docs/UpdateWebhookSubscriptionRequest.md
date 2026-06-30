# UpdateWebhookSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Optional field (included only when present in request) | [optional] 
**events** | **List[str]** | Optional field (included only when present in request) | [optional] 
**is_active** | **bool** | Optional field (included only when present in request) | [optional] 

## Example

```python
from mizancore_baas_generated.models.update_webhook_subscription_request import UpdateWebhookSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookSubscriptionRequest from a JSON string
update_webhook_subscription_request_instance = UpdateWebhookSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookSubscriptionRequest.to_json())

# convert the object into a dict
update_webhook_subscription_request_dict = update_webhook_subscription_request_instance.to_dict()
# create an instance of UpdateWebhookSubscriptionRequest from a dict
update_webhook_subscription_request_from_dict = UpdateWebhookSubscriptionRequest.from_dict(update_webhook_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


