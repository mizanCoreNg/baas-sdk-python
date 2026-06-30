# UsageAnalyticsSummary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**UsageAnalyticsSummary200ResponseData**](UsageAnalyticsSummary200ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.usage_analytics_summary200_response import UsageAnalyticsSummary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsageAnalyticsSummary200Response from a JSON string
usage_analytics_summary200_response_instance = UsageAnalyticsSummary200Response.from_json(json)
# print the JSON string representation of the object
print(UsageAnalyticsSummary200Response.to_json())

# convert the object into a dict
usage_analytics_summary200_response_dict = usage_analytics_summary200_response_instance.to_dict()
# create an instance of UsageAnalyticsSummary200Response from a dict
usage_analytics_summary200_response_from_dict = UsageAnalyticsSummary200Response.from_dict(usage_analytics_summary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


