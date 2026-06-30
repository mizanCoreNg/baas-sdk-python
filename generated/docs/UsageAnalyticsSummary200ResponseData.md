# UsageAnalyticsSummary200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** |  | [optional] 
**total_calls** | **str** |  | [optional] 
**success_count** | **int** |  | [optional] 
**error_4xx_count** | **int** |  | [optional] 
**error_5xx_count** | **int** |  | [optional] 
**success_rate** | **str** |  | [optional] 
**avg_latency_ms** | **str** |  | [optional] 
**p95_latency_ms** | **str** |  | [optional] 
**p99_latency_ms** | **str** |  | [optional] 
**breakdown** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.usage_analytics_summary200_response_data import UsageAnalyticsSummary200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UsageAnalyticsSummary200ResponseData from a JSON string
usage_analytics_summary200_response_data_instance = UsageAnalyticsSummary200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UsageAnalyticsSummary200ResponseData.to_json())

# convert the object into a dict
usage_analytics_summary200_response_data_dict = usage_analytics_summary200_response_data_instance.to_dict()
# create an instance of UsageAnalyticsSummary200ResponseData from a dict
usage_analytics_summary200_response_data_from_dict = UsageAnalyticsSummary200ResponseData.from_dict(usage_analytics_summary200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


