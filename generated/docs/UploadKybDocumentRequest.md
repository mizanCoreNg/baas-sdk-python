# UploadKybDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** |  | 
**file** | **str** |  | 

## Example

```python
from mizancore_baas_generated.models.upload_kyb_document_request import UploadKybDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadKybDocumentRequest from a JSON string
upload_kyb_document_request_instance = UploadKybDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(UploadKybDocumentRequest.to_json())

# convert the object into a dict
upload_kyb_document_request_dict = upload_kyb_document_request_instance.to_dict()
# create an instance of UploadKybDocumentRequest from a dict
upload_kyb_document_request_from_dict = UploadKybDocumentRequest.from_dict(upload_kyb_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


