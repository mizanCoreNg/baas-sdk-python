# ManagedCardReadIndex200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**masked_pan** | **str** |  | [optional] 
**card_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**expiry_month** | **str** |  | [optional] 
**expiry_year** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**processor_ref** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.managed_card_read_index200_response_data import ManagedCardReadIndex200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedCardReadIndex200ResponseData from a JSON string
managed_card_read_index200_response_data_instance = ManagedCardReadIndex200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ManagedCardReadIndex200ResponseData.to_json())

# convert the object into a dict
managed_card_read_index200_response_data_dict = managed_card_read_index200_response_data_instance.to_dict()
# create an instance of ManagedCardReadIndex200ResponseData from a dict
managed_card_read_index200_response_data_from_dict = ManagedCardReadIndex200ResponseData.from_dict(managed_card_read_index200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


