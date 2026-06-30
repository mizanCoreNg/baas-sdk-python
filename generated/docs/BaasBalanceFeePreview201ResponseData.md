# BaasBalanceFeePreview201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**fee_kobo** | **str** |  | [optional] 
**total_debit_kobo** | **str** |  | [optional] 
**current_balance_kobo** | **int** | Amount in kobo (minor currency units). | [optional] 
**sufficient_balance** | **int** | Amount in kobo (minor currency units). | [optional] 

## Example

```python
from mizancore_baas_generated.models.baas_balance_fee_preview201_response_data import BaasBalanceFeePreview201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BaasBalanceFeePreview201ResponseData from a JSON string
baas_balance_fee_preview201_response_data_instance = BaasBalanceFeePreview201ResponseData.from_json(json)
# print the JSON string representation of the object
print(BaasBalanceFeePreview201ResponseData.to_json())

# convert the object into a dict
baas_balance_fee_preview201_response_data_dict = baas_balance_fee_preview201_response_data_instance.to_dict()
# create an instance of BaasBalanceFeePreview201ResponseData from a dict
baas_balance_fee_preview201_response_data_from_dict = BaasBalanceFeePreview201ResponseData.from_dict(baas_balance_fee_preview201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


