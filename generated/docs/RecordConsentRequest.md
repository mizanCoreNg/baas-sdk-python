# RecordConsentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | **str** |  | 
**consent_type** | **str** |  | 
**scope** | **List[str]** |  | [optional] 
**expires_at** | **date** |  | [optional] 
**source_reference** | **str** |  | [optional] 

## Example

```python
from mizancore_baas_generated.models.record_consent_request import RecordConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordConsentRequest from a JSON string
record_consent_request_instance = RecordConsentRequest.from_json(json)
# print the JSON string representation of the object
print(RecordConsentRequest.to_json())

# convert the object into a dict
record_consent_request_dict = record_consent_request_instance.to_dict()
# create an instance of RecordConsentRequest from a dict
record_consent_request_from_dict = RecordConsentRequest.from_dict(record_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


