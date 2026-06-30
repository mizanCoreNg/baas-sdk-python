# PartnerFeeScheduleIndex200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | **str** |  | [optional] 
**charge_type** | **str** |  | [optional] 
**flat_amount** | **int** | Amount in kobo (minor currency units). | [optional] 
**flat_amount_naira** | **int** | Amount in kobo (minor currency units). | [optional] 
**percentage** | **str** |  | [optional] 
**min_fee** | **int** | Amount in kobo (minor currency units). | [optional] 
**min_fee_naira** | **str** |  | [optional] 
**max_fee** | **int** | Amount in kobo (minor currency units). | [optional] 
**max_fee_naira** | **str** |  | [optional] 
**tiers** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_fee_schedule_index200_response_data import PartnerFeeScheduleIndex200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerFeeScheduleIndex200ResponseData from a JSON string
partner_fee_schedule_index200_response_data_instance = PartnerFeeScheduleIndex200ResponseData.from_json(json)
# print the JSON string representation of the object
print(PartnerFeeScheduleIndex200ResponseData.to_json())

# convert the object into a dict
partner_fee_schedule_index200_response_data_dict = partner_fee_schedule_index200_response_data_instance.to_dict()
# create an instance of PartnerFeeScheduleIndex200ResponseData from a dict
partner_fee_schedule_index200_response_data_from_dict = PartnerFeeScheduleIndex200ResponseData.from_dict(partner_fee_schedule_index200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


