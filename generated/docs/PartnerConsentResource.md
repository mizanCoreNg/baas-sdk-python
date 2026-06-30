# PartnerConsentResource


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
from mizancore_baas_generated.models.partner_consent_resource import PartnerConsentResource

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerConsentResource from a JSON string
partner_consent_resource_instance = PartnerConsentResource.from_json(json)
# print the JSON string representation of the object
print(PartnerConsentResource.to_json())

# convert the object into a dict
partner_consent_resource_dict = partner_consent_resource_instance.to_dict()
# create an instance of PartnerConsentResource from a dict
partner_consent_resource_from_dict = PartnerConsentResource.from_dict(partner_consent_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


