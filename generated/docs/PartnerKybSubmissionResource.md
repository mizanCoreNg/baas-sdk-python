# PartnerKybSubmissionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**registration_type** | **str** |  | [optional] 
**rc_number** | **int** |  | [optional] 
**legal_name** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**registered_address** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**allows_live_access** | **str** |  | [optional] 
**rejection_reason** | **str** |  | [optional] 
**submitted_at** | **datetime** |  | [optional] 
**reviewed_at** | **datetime** |  | [optional] 
**officers** | **str** |  | [optional] 
**documents** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_kyb_submission_resource import PartnerKybSubmissionResource

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerKybSubmissionResource from a JSON string
partner_kyb_submission_resource_instance = PartnerKybSubmissionResource.from_json(json)
# print the JSON string representation of the object
print(PartnerKybSubmissionResource.to_json())

# convert the object into a dict
partner_kyb_submission_resource_dict = partner_kyb_submission_resource_instance.to_dict()
# create an instance of PartnerKybSubmissionResource from a dict
partner_kyb_submission_resource_from_dict = PartnerKybSubmissionResource.from_dict(partner_kyb_submission_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


