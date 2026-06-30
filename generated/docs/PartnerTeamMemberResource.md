# PartnerTeamMemberResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**last_login_at** | **datetime** |  | [optional] 
**invited_at** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_team_member_resource import PartnerTeamMemberResource

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerTeamMemberResource from a JSON string
partner_team_member_resource_instance = PartnerTeamMemberResource.from_json(json)
# print the JSON string representation of the object
print(PartnerTeamMemberResource.to_json())

# convert the object into a dict
partner_team_member_resource_dict = partner_team_member_resource_instance.to_dict()
# create an instance of PartnerTeamMemberResource from a dict
partner_team_member_resource_from_dict = PartnerTeamMemberResource.from_dict(partner_team_member_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


