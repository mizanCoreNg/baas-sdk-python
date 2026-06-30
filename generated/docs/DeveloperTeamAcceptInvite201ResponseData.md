# DeveloperTeamAcceptInvite201ResponseData


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
from mizancore_baas_generated.models.developer_team_accept_invite201_response_data import DeveloperTeamAcceptInvite201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperTeamAcceptInvite201ResponseData from a JSON string
developer_team_accept_invite201_response_data_instance = DeveloperTeamAcceptInvite201ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeveloperTeamAcceptInvite201ResponseData.to_json())

# convert the object into a dict
developer_team_accept_invite201_response_data_dict = developer_team_accept_invite201_response_data_instance.to_dict()
# create an instance of DeveloperTeamAcceptInvite201ResponseData from a dict
developer_team_accept_invite201_response_data_from_dict = DeveloperTeamAcceptInvite201ResponseData.from_dict(developer_team_accept_invite201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


