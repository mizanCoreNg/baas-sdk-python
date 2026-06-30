# UsageAnalyticsRateLimitStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**UsageAnalyticsRateLimitStatus200ResponseData**](UsageAnalyticsRateLimitStatus200ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.usage_analytics_rate_limit_status200_response import UsageAnalyticsRateLimitStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsageAnalyticsRateLimitStatus200Response from a JSON string
usage_analytics_rate_limit_status200_response_instance = UsageAnalyticsRateLimitStatus200Response.from_json(json)
# print the JSON string representation of the object
print(UsageAnalyticsRateLimitStatus200Response.to_json())

# convert the object into a dict
usage_analytics_rate_limit_status200_response_dict = usage_analytics_rate_limit_status200_response_instance.to_dict()
# create an instance of UsageAnalyticsRateLimitStatus200Response from a dict
usage_analytics_rate_limit_status200_response_from_dict = UsageAnalyticsRateLimitStatus200Response.from_dict(usage_analytics_rate_limit_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


