# BaasBalanceFeePreview201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**BaasBalanceFeePreview201ResponseData**](BaasBalanceFeePreview201ResponseData.md) |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.baas_balance_fee_preview201_response import BaasBalanceFeePreview201Response

# TODO update the JSON string below
json = "{}"
# create an instance of BaasBalanceFeePreview201Response from a JSON string
baas_balance_fee_preview201_response_instance = BaasBalanceFeePreview201Response.from_json(json)
# print the JSON string representation of the object
print(BaasBalanceFeePreview201Response.to_json())

# convert the object into a dict
baas_balance_fee_preview201_response_dict = baas_balance_fee_preview201_response_instance.to_dict()
# create an instance of BaasBalanceFeePreview201Response from a dict
baas_balance_fee_preview201_response_from_dict = BaasBalanceFeePreview201Response.from_dict(baas_balance_fee_preview201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


