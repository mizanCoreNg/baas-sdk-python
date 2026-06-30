# UsageAnalyticsRateLimitStatus200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** |  | [optional] 
**reads_per_minute** | **str** |  | [optional] 
**limit** | **str** |  | [optional] 
**used** | **str** |  | [optional] 
**remaining** | **str** |  | [optional] 
**writes_per_minute** | **str** |  | [optional] 
**overall_per_minute** | **str** |  | [optional] 
**reset_at** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.usage_analytics_rate_limit_status200_response_data import UsageAnalyticsRateLimitStatus200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UsageAnalyticsRateLimitStatus200ResponseData from a JSON string
usage_analytics_rate_limit_status200_response_data_instance = UsageAnalyticsRateLimitStatus200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UsageAnalyticsRateLimitStatus200ResponseData.to_json())

# convert the object into a dict
usage_analytics_rate_limit_status200_response_data_dict = usage_analytics_rate_limit_status200_response_data_instance.to_dict()
# create an instance of UsageAnalyticsRateLimitStatus200ResponseData from a dict
usage_analytics_rate_limit_status200_response_data_from_dict = UsageAnalyticsRateLimitStatus200ResponseData.from_dict(usage_analytics_rate_limit_status200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


