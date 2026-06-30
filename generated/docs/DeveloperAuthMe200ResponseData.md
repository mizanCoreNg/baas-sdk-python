# DeveloperAuthMe200ResponseData


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
from mizancore_baas_generated.models.developer_auth_me200_response_data import DeveloperAuthMe200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperAuthMe200ResponseData from a JSON string
developer_auth_me200_response_data_instance = DeveloperAuthMe200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeveloperAuthMe200ResponseData.to_json())

# convert the object into a dict
developer_auth_me200_response_data_dict = developer_auth_me200_response_data_instance.to_dict()
# create an instance of DeveloperAuthMe200ResponseData from a dict
developer_auth_me200_response_data_from_dict = DeveloperAuthMe200ResponseData.from_dict(developer_auth_me200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


