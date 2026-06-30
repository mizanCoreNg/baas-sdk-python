# InitiateWithdrawalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 
**destination_account** | **str** |  | 
**destination_bank** | **str** |  | 
**narration** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.initiate_withdrawal_request import InitiateWithdrawalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateWithdrawalRequest from a JSON string
initiate_withdrawal_request_instance = InitiateWithdrawalRequest.from_json(json)
# print the JSON string representation of the object
print(InitiateWithdrawalRequest.to_json())

# convert the object into a dict
initiate_withdrawal_request_dict = initiate_withdrawal_request_instance.to_dict()
# create an instance of InitiateWithdrawalRequest from a dict
initiate_withdrawal_request_from_dict = InitiateWithdrawalRequest.from_dict(initiate_withdrawal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


