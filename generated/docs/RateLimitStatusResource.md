# RateLimitStatusResource


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
from mizancore_baas_generated.models.rate_limit_status_resource import RateLimitStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitStatusResource from a JSON string
rate_limit_status_resource_instance = RateLimitStatusResource.from_json(json)
# print the JSON string representation of the object
print(RateLimitStatusResource.to_json())

# convert the object into a dict
rate_limit_status_resource_dict = rate_limit_status_resource_instance.to_dict()
# create an instance of RateLimitStatusResource from a dict
rate_limit_status_resource_from_dict = RateLimitStatusResource.from_dict(rate_limit_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


