# ManagedCustomerLinkResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**customer_reference** | **str** |  | [optional] 
**onboarded_at** | **datetime** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**pii_access** | **str** |  | [optional] 
**customer** | **str** |  | [optional] 
**customer_number** | **int** |  | [optional] 
**kyc_tier** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**phone_masked** | **str** |  | [optional] 
**bvn_masked** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.managed_customer_link_resource import ManagedCustomerLinkResource

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedCustomerLinkResource from a JSON string
managed_customer_link_resource_instance = ManagedCustomerLinkResource.from_json(json)
# print the JSON string representation of the object
print(ManagedCustomerLinkResource.to_json())

# convert the object into a dict
managed_customer_link_resource_dict = managed_customer_link_resource_instance.to_dict()
# create an instance of ManagedCustomerLinkResource from a dict
managed_customer_link_resource_from_dict = ManagedCustomerLinkResource.from_dict(managed_customer_link_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


