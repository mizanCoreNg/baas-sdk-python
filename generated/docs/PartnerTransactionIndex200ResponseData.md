# PartnerTransactionIndex200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**transaction_type_label** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**amount** | **int** | Amount in kobo (minor currency units). | [optional] 
**amount_naira** | **int** | Amount in kobo (minor currency units). | [optional] 
**fee_amount** | **int** | Amount in kobo (minor currency units). | [optional] 
**fee_amount_naira** | **int** | Amount in kobo (minor currency units). | [optional] 
**net_amount** | **int** | Amount in kobo (minor currency units). | [optional] 
**net_amount_naira** | **int** | Amount in kobo (minor currency units). | [optional] 
**currency** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**narration** | **str** |  | [optional] 
**sender_name** | **str** |  | [optional] 
**sender_account** | **str** |  | [optional] 
**sender_bank** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.partner_transaction_index200_response_data import PartnerTransactionIndex200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerTransactionIndex200ResponseData from a JSON string
partner_transaction_index200_response_data_instance = PartnerTransactionIndex200ResponseData.from_json(json)
# print the JSON string representation of the object
print(PartnerTransactionIndex200ResponseData.to_json())

# convert the object into a dict
partner_transaction_index200_response_data_dict = partner_transaction_index200_response_data_instance.to_dict()
# create an instance of PartnerTransactionIndex200ResponseData from a dict
partner_transaction_index200_response_data_from_dict = PartnerTransactionIndex200ResponseData.from_dict(partner_transaction_index200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


