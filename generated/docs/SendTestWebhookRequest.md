# SendTestWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** |  | 
**payload** | **List[str]** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.send_test_webhook_request import SendTestWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendTestWebhookRequest from a JSON string
send_test_webhook_request_instance = SendTestWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(SendTestWebhookRequest.to_json())

# convert the object into a dict
send_test_webhook_request_dict = send_test_webhook_request_instance.to_dict()
# create an instance of SendTestWebhookRequest from a dict
send_test_webhook_request_from_dict = SendTestWebhookRequest.from_dict(send_test_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


