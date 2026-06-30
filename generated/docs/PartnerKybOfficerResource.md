# PartnerKybOfficerResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**date_of_birth** | **datetime** |  | [optional] 
**role** | **str** |  | [optional] 
**ownership_percentage** | **str** |  | [optional] 
**bvn_masked** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_kyb_officer_resource import PartnerKybOfficerResource

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerKybOfficerResource from a JSON string
partner_kyb_officer_resource_instance = PartnerKybOfficerResource.from_json(json)
# print the JSON string representation of the object
print(PartnerKybOfficerResource.to_json())

# convert the object into a dict
partner_kyb_officer_resource_dict = partner_kyb_officer_resource_instance.to_dict()
# create an instance of PartnerKybOfficerResource from a dict
partner_kyb_officer_resource_from_dict = PartnerKybOfficerResource.from_dict(partner_kyb_officer_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


