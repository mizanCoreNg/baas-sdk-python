# PartnerFeeScheduleIndex200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**PartnerFeeScheduleIndex200ResponseData**](PartnerFeeScheduleIndex200ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_fee_schedule_index200_response import PartnerFeeScheduleIndex200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerFeeScheduleIndex200Response from a JSON string
partner_fee_schedule_index200_response_instance = PartnerFeeScheduleIndex200Response.from_json(json)
# print the JSON string representation of the object
print(PartnerFeeScheduleIndex200Response.to_json())

# convert the object into a dict
partner_fee_schedule_index200_response_dict = partner_fee_schedule_index200_response_instance.to_dict()
# create an instance of PartnerFeeScheduleIndex200Response from a dict
partner_fee_schedule_index200_response_from_dict = PartnerFeeScheduleIndex200Response.from_dict(partner_fee_schedule_index200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


