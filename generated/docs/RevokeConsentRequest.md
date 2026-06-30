# RevokeConsentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.revoke_consent_request import RevokeConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeConsentRequest from a JSON string
revoke_consent_request_instance = RevokeConsentRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeConsentRequest.to_json())

# convert the object into a dict
revoke_consent_request_dict = revoke_consent_request_instance.to_dict()
# create an instance of RevokeConsentRequest from a dict
revoke_consent_request_from_dict = RevokeConsentRequest.from_dict(revoke_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


