# PartnerStatementResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**period** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**virtual_account_id** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**opening_balance_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**total_credit_kobo** | **str** |  | [optional] 
**total_debit_kobo** | **str** |  | [optional] 
**closing_balance_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**movement_count** | **int** |  | [optional] 
**movements** | **str** |  | [optional] 
**summaries** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_statement_resource import PartnerStatementResource

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerStatementResource from a JSON string
partner_statement_resource_instance = PartnerStatementResource.from_json(json)
# print the JSON string representation of the object
print(PartnerStatementResource.to_json())

# convert the object into a dict
partner_statement_resource_dict = partner_statement_resource_instance.to_dict()
# create an instance of PartnerStatementResource from a dict
partner_statement_resource_from_dict = PartnerStatementResource.from_dict(partner_statement_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


