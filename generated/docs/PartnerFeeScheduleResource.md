# PartnerFeeScheduleResource


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
from mizancore_baas_generated.models.partner_fee_schedule_resource import PartnerFeeScheduleResource

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerFeeScheduleResource from a JSON string
partner_fee_schedule_resource_instance = PartnerFeeScheduleResource.from_json(json)
# print the JSON string representation of the object
print(PartnerFeeScheduleResource.to_json())

# convert the object into a dict
partner_fee_schedule_resource_dict = partner_fee_schedule_resource_instance.to_dict()
# create an instance of PartnerFeeScheduleResource from a dict
partner_fee_schedule_resource_from_dict = PartnerFeeScheduleResource.from_dict(partner_fee_schedule_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


