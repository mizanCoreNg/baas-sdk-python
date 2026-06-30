# VerifyDeveloperEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from mizancore_baas_generated.models.verify_developer_email_request import VerifyDeveloperEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyDeveloperEmailRequest from a JSON string
verify_developer_email_request_instance = VerifyDeveloperEmailRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyDeveloperEmailRequest.to_json())

# convert the object into a dict
verify_developer_email_request_dict = verify_developer_email_request_instance.to_dict()
# create an instance of VerifyDeveloperEmailRequest from a dict
verify_developer_email_request_from_dict = VerifyDeveloperEmailRequest.from_dict(verify_developer_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


