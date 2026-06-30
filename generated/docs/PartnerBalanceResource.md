# PartnerBalanceResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**balance_naira** | **int** | Amount in kobo (minor currency units). | [optional] 
**currency** | **str** |  | [optional] 
**total_credited** | **str** |  | [optional] 
**total_debited** | **str** |  | [optional] 
**settlement_account** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_balance_resource import PartnerBalanceResource

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerBalanceResource from a JSON string
partner_balance_resource_instance = PartnerBalanceResource.from_json(json)
# print the JSON string representation of the object
print(PartnerBalanceResource.to_json())

# convert the object into a dict
partner_balance_resource_dict = partner_balance_resource_instance.to_dict()
# create an instance of PartnerBalanceResource from a dict
partner_balance_resource_from_dict = PartnerBalanceResource.from_dict(partner_balance_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


