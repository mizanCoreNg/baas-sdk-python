# OnboardManagedCustomerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bvn** | **str** |  | 
**nin** | **str** | Required when: tier,2,3 | [optional] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**phone** | **str** |  | 
**email** | **str** |  | [optional] 
**date_of_birth** | **date** |  | 
**gender** | **str** |  | [optional] 
**address** | **str** | Required when: tier,3 | [optional] 
**tier** | **int** |  | 
**customer_reference** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.onboard_managed_customer_request import OnboardManagedCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardManagedCustomerRequest from a JSON string
onboard_managed_customer_request_instance = OnboardManagedCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(OnboardManagedCustomerRequest.to_json())

# convert the object into a dict
onboard_managed_customer_request_dict = onboard_managed_customer_request_instance.to_dict()
# create an instance of OnboardManagedCustomerRequest from a dict
onboard_managed_customer_request_from_dict = OnboardManagedCustomerRequest.from_dict(onboard_managed_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


