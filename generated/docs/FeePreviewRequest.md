# FeePreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 

## Example

```python
from mizancore_baas_generated.models.fee_preview_request import FeePreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeePreviewRequest from a JSON string
fee_preview_request_instance = FeePreviewRequest.from_json(json)
# print the JSON string representation of the object
print(FeePreviewRequest.to_json())

# convert the object into a dict
fee_preview_request_dict = fee_preview_request_instance.to_dict()
# create an instance of FeePreviewRequest from a dict
fee_preview_request_from_dict = FeePreviewRequest.from_dict(fee_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


