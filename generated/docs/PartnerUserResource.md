# PartnerUserResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**baas_partner_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**mfa_enabled** | **bool** |  | [optional] 
**email_verified_at** | **datetime** |  | [optional] 
**partner** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**settlement_mode** | **str** |  | [optional] 
**operating_model** | **str** |  | [optional] 
**kyb_status** | **str** |  | [optional] 
**go_live** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_user_resource import PartnerUserResource

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerUserResource from a JSON string
partner_user_resource_instance = PartnerUserResource.from_json(json)
# print the JSON string representation of the object
print(PartnerUserResource.to_json())

# convert the object into a dict
partner_user_resource_dict = partner_user_resource_instance.to_dict()
# create an instance of PartnerUserResource from a dict
partner_user_resource_from_dict = PartnerUserResource.from_dict(partner_user_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


