# WithdrawalFeePreviewResource


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
from mizancore_baas_generated.models.withdrawal_fee_preview_resource import WithdrawalFeePreviewResource

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalFeePreviewResource from a JSON string
withdrawal_fee_preview_resource_instance = WithdrawalFeePreviewResource.from_json(json)
# print the JSON string representation of the object
print(WithdrawalFeePreviewResource.to_json())

# convert the object into a dict
withdrawal_fee_preview_resource_dict = withdrawal_fee_preview_resource_instance.to_dict()
# create an instance of WithdrawalFeePreviewResource from a dict
withdrawal_fee_preview_resource_from_dict = WithdrawalFeePreviewResource.from_dict(withdrawal_fee_preview_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


