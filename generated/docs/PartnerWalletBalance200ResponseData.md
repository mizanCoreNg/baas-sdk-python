# PartnerWalletBalance200ResponseData


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
from mizancore_baas_generated.models.partner_wallet_balance200_response_data import PartnerWalletBalance200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerWalletBalance200ResponseData from a JSON string
partner_wallet_balance200_response_data_instance = PartnerWalletBalance200ResponseData.from_json(json)
# print the JSON string representation of the object
print(PartnerWalletBalance200ResponseData.to_json())

# convert the object into a dict
partner_wallet_balance200_response_data_dict = partner_wallet_balance200_response_data_instance.to_dict()
# create an instance of PartnerWalletBalance200ResponseData from a dict
partner_wallet_balance200_response_data_from_dict = PartnerWalletBalance200ResponseData.from_dict(partner_wallet_balance200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


