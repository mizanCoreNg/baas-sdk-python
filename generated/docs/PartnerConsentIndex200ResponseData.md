# PartnerConsentIndex200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**customer_reference** | **str** |  | [optional] 
**consent_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**granted_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**revoked_at** | **datetime** |  | [optional] 
**recorded_by_id** | **str** |  | [optional] 
**source_reference** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_consent_index200_response_data import PartnerConsentIndex200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerConsentIndex200ResponseData from a JSON string
partner_consent_index200_response_data_instance = PartnerConsentIndex200ResponseData.from_json(json)
# print the JSON string representation of the object
print(PartnerConsentIndex200ResponseData.to_json())

# convert the object into a dict
partner_consent_index200_response_data_dict = partner_consent_index200_response_data_instance.to_dict()
# create an instance of PartnerConsentIndex200ResponseData from a dict
partner_consent_index200_response_data_from_dict = PartnerConsentIndex200ResponseData.from_dict(partner_consent_index200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


