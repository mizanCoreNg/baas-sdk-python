# WebhookSubscriptionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**events** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**webhook_rate_limit** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.webhook_subscription_resource import WebhookSubscriptionResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionResource from a JSON string
webhook_subscription_resource_instance = WebhookSubscriptionResource.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionResource.to_json())

# convert the object into a dict
webhook_subscription_resource_dict = webhook_subscription_resource_instance.to_dict()
# create an instance of WebhookSubscriptionResource from a dict
webhook_subscription_resource_from_dict = WebhookSubscriptionResource.from_dict(webhook_subscription_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


