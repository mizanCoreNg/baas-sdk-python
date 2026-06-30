# mizancore_baas_generated.DeveloperPortalKYBApi

All URIs are relative to *https://api.mizancore.ng*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_kyb_business**](DeveloperPortalKYBApi.md#developer_kyb_business) | **PUT** /api/v1/developer/kyb/business | Update KYB business info
[**developer_kyb_documents_upload**](DeveloperPortalKYBApi.md#developer_kyb_documents_upload) | **POST** /api/v1/developer/kyb/documents | Upload a KYB document
[**developer_kyb_officers_add**](DeveloperPortalKYBApi.md#developer_kyb_officers_add) | **POST** /api/v1/developer/kyb/officers | Add a KYB officer
[**developer_kyb_officers_remove**](DeveloperPortalKYBApi.md#developer_kyb_officers_remove) | **DELETE** /api/v1/developer/kyb/officers/{id} | Remove a KYB officer
[**developer_kyb_officers_update**](DeveloperPortalKYBApi.md#developer_kyb_officers_update) | **PATCH** /api/v1/developer/kyb/officers/{id} | Update a KYB officer
[**developer_kyb_show**](DeveloperPortalKYBApi.md#developer_kyb_show) | **GET** /api/v1/developer/kyb | Get KYB submission
[**developer_kyb_submit**](DeveloperPortalKYBApi.md#developer_kyb_submit) | **POST** /api/v1/developer/kyb/submit | Submit KYB for review


# **developer_kyb_business**
> VirtualAccountQueryIndex200Response developer_kyb_business(x_tenant_id, update_kyb_business_request)

Update KYB business info

Sets registration type, RC number, legal name, tax id and registered address. Owner/admin only. Editable while draft or needs_more_info.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.update_kyb_business_request import UpdateKybBusinessRequest
from mizancore_baas_generated.models.virtual_account_query_index200_response import VirtualAccountQueryIndex200Response
from mizancore_baas_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mizancore.ng
# See configuration.py for a list of all supported configuration parameters.
configuration = mizancore_baas_generated.Configuration(
    host = "https://api.mizancore.ng"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tenantHeader
configuration.api_key['tenantHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantHeader'] = 'Bearer'

# Configure API key authorization: hmacAuth
configuration.api_key['hmacAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacAuth'] = 'Bearer'

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mizancore_baas_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mizancore_baas_generated.DeveloperPortalKYBApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    update_kyb_business_request = {"registration_type":"private_incorporated","rc_number":"example","legal_name":"example","tax_id":"11111111-0000-0000-0000-000000000001","registered_address":{}} # UpdateKybBusinessRequest | 

    try:
        # Update KYB business info
        api_response = api_instance.developer_kyb_business(x_tenant_id, update_kyb_business_request)
        print("The response of DeveloperPortalKYBApi->developer_kyb_business:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalKYBApi->developer_kyb_business: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **update_kyb_business_request** | [**UpdateKybBusinessRequest**](UpdateKybBusinessRequest.md)|  | 

### Return type

[**VirtualAccountQueryIndex200Response**](VirtualAccountQueryIndex200Response.md)

### Authorization

[tenantHeader](../README.md#tenantHeader), [hmacAuth](../README.md#hmacAuth), [apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**422** | Validation error or submission locked |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — not a KYB manager |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_kyb_documents_upload**
> VirtualAccountQueryIndex200Response developer_kyb_documents_upload(x_tenant_id, upload_kyb_document_request)

Upload a KYB document

Multipart upload of a supporting document. Stored via the document storage abstraction. Owner/admin only.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.upload_kyb_document_request import UploadKybDocumentRequest
from mizancore_baas_generated.models.virtual_account_query_index200_response import VirtualAccountQueryIndex200Response
from mizancore_baas_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mizancore.ng
# See configuration.py for a list of all supported configuration parameters.
configuration = mizancore_baas_generated.Configuration(
    host = "https://api.mizancore.ng"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tenantHeader
configuration.api_key['tenantHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantHeader'] = 'Bearer'

# Configure API key authorization: hmacAuth
configuration.api_key['hmacAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacAuth'] = 'Bearer'

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mizancore_baas_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mizancore_baas_generated.DeveloperPortalKYBApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    upload_kyb_document_request = {"document_type":"certificate_of_incorporation","file":"example"} # UploadKybDocumentRequest | 

    try:
        # Upload a KYB document
        api_response = api_instance.developer_kyb_documents_upload(x_tenant_id, upload_kyb_document_request)
        print("The response of DeveloperPortalKYBApi->developer_kyb_documents_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalKYBApi->developer_kyb_documents_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **upload_kyb_document_request** | [**UploadKybDocumentRequest**](UploadKybDocumentRequest.md)|  | 

### Return type

[**VirtualAccountQueryIndex200Response**](VirtualAccountQueryIndex200Response.md)

### Authorization

[tenantHeader](../README.md#tenantHeader), [hmacAuth](../README.md#hmacAuth), [apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully. |  -  |
**200** | Successful operation. |  -  |
**422** | Validation error or submission locked |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — not a KYB manager |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_kyb_officers_add**
> VirtualAccountQueryIndex200Response developer_kyb_officers_add(x_tenant_id, add_kyb_officer_request)

Add a KYB officer

Attaches a director or beneficial owner. Owner/admin only. BVN is stored hidden and returned masked.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.add_kyb_officer_request import AddKybOfficerRequest
from mizancore_baas_generated.models.virtual_account_query_index200_response import VirtualAccountQueryIndex200Response
from mizancore_baas_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mizancore.ng
# See configuration.py for a list of all supported configuration parameters.
configuration = mizancore_baas_generated.Configuration(
    host = "https://api.mizancore.ng"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tenantHeader
configuration.api_key['tenantHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantHeader'] = 'Bearer'

# Configure API key authorization: hmacAuth
configuration.api_key['hmacAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacAuth'] = 'Bearer'

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mizancore_baas_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mizancore_baas_generated.DeveloperPortalKYBApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    add_kyb_officer_request = {"full_name":"example","date_of_birth":"2026-04-21","bvn":"12345678901","role":"owner","ownership_percentage":1} # AddKybOfficerRequest | 

    try:
        # Add a KYB officer
        api_response = api_instance.developer_kyb_officers_add(x_tenant_id, add_kyb_officer_request)
        print("The response of DeveloperPortalKYBApi->developer_kyb_officers_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalKYBApi->developer_kyb_officers_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **add_kyb_officer_request** | [**AddKybOfficerRequest**](AddKybOfficerRequest.md)|  | 

### Return type

[**VirtualAccountQueryIndex200Response**](VirtualAccountQueryIndex200Response.md)

### Authorization

[tenantHeader](../README.md#tenantHeader), [hmacAuth](../README.md#hmacAuth), [apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully. |  -  |
**200** | Successful operation. |  -  |
**422** | Validation error or submission locked |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — not a KYB manager |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_kyb_officers_remove**
> VirtualAccountQueryIndex200Response developer_kyb_officers_remove(id, x_tenant_id)

Remove a KYB officer

Removes a director/owner. Owner/admin only. BOLA-scoped.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.virtual_account_query_index200_response import VirtualAccountQueryIndex200Response
from mizancore_baas_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mizancore.ng
# See configuration.py for a list of all supported configuration parameters.
configuration = mizancore_baas_generated.Configuration(
    host = "https://api.mizancore.ng"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tenantHeader
configuration.api_key['tenantHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantHeader'] = 'Bearer'

# Configure API key authorization: hmacAuth
configuration.api_key['hmacAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacAuth'] = 'Bearer'

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mizancore_baas_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mizancore_baas_generated.DeveloperPortalKYBApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Remove a KYB officer
        api_response = api_instance.developer_kyb_officers_remove(id, x_tenant_id)
        print("The response of DeveloperPortalKYBApi->developer_kyb_officers_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalKYBApi->developer_kyb_officers_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 

### Return type

[**VirtualAccountQueryIndex200Response**](VirtualAccountQueryIndex200Response.md)

### Authorization

[tenantHeader](../README.md#tenantHeader), [hmacAuth](../README.md#hmacAuth), [apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully. |  -  |
**200** | Successful operation. |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — not a KYB manager |  -  |
**404** | Officer not found in this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**422** | Submission locked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_kyb_officers_update**
> VirtualAccountQueryIndex200Response developer_kyb_officers_update(id, x_tenant_id, update_kyb_officer_request)

Update a KYB officer

Updates a director/owner. Owner/admin only. BOLA: a cross-partner officer id resolves to 404.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.update_kyb_officer_request import UpdateKybOfficerRequest
from mizancore_baas_generated.models.virtual_account_query_index200_response import VirtualAccountQueryIndex200Response
from mizancore_baas_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mizancore.ng
# See configuration.py for a list of all supported configuration parameters.
configuration = mizancore_baas_generated.Configuration(
    host = "https://api.mizancore.ng"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tenantHeader
configuration.api_key['tenantHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantHeader'] = 'Bearer'

# Configure API key authorization: hmacAuth
configuration.api_key['hmacAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacAuth'] = 'Bearer'

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mizancore_baas_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mizancore_baas_generated.DeveloperPortalKYBApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    update_kyb_officer_request = {"full_name":"example","date_of_birth":"2026-04-21","bvn":"12345678901","role":"owner","ownership_percentage":1} # UpdateKybOfficerRequest | 

    try:
        # Update a KYB officer
        api_response = api_instance.developer_kyb_officers_update(id, x_tenant_id, update_kyb_officer_request)
        print("The response of DeveloperPortalKYBApi->developer_kyb_officers_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalKYBApi->developer_kyb_officers_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **update_kyb_officer_request** | [**UpdateKybOfficerRequest**](UpdateKybOfficerRequest.md)|  | 

### Return type

[**VirtualAccountQueryIndex200Response**](VirtualAccountQueryIndex200Response.md)

### Authorization

[tenantHeader](../README.md#tenantHeader), [hmacAuth](../README.md#hmacAuth), [apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**422** | Validation error or submission locked |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — not a KYB manager |  -  |
**404** | Officer not found in this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_kyb_show**
> VirtualAccountQueryIndex200Response developer_kyb_show(x_tenant_id)

Get KYB submission

Returns the authenticated partner KYB submission with officers and documents, creating a draft if none exists.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.virtual_account_query_index200_response import VirtualAccountQueryIndex200Response
from mizancore_baas_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mizancore.ng
# See configuration.py for a list of all supported configuration parameters.
configuration = mizancore_baas_generated.Configuration(
    host = "https://api.mizancore.ng"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tenantHeader
configuration.api_key['tenantHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantHeader'] = 'Bearer'

# Configure API key authorization: hmacAuth
configuration.api_key['hmacAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacAuth'] = 'Bearer'

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mizancore_baas_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mizancore_baas_generated.DeveloperPortalKYBApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Get KYB submission
        api_response = api_instance.developer_kyb_show(x_tenant_id)
        print("The response of DeveloperPortalKYBApi->developer_kyb_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalKYBApi->developer_kyb_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 

### Return type

[**VirtualAccountQueryIndex200Response**](VirtualAccountQueryIndex200Response.md)

### Authorization

[tenantHeader](../README.md#tenantHeader), [hmacAuth](../README.md#hmacAuth), [apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized (insufficient permissions). |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_kyb_submit**
> VirtualAccountQueryIndex200Response developer_kyb_submit(x_tenant_id)

Submit KYB for review

Validates completeness and submits the KYB. Owner/admin only. Returns 422 if incomplete.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.virtual_account_query_index200_response import VirtualAccountQueryIndex200Response
from mizancore_baas_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mizancore.ng
# See configuration.py for a list of all supported configuration parameters.
configuration = mizancore_baas_generated.Configuration(
    host = "https://api.mizancore.ng"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tenantHeader
configuration.api_key['tenantHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantHeader'] = 'Bearer'

# Configure API key authorization: hmacAuth
configuration.api_key['hmacAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['hmacAuth'] = 'Bearer'

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with mizancore_baas_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mizancore_baas_generated.DeveloperPortalKYBApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Submit KYB for review
        api_response = api_instance.developer_kyb_submit(x_tenant_id)
        print("The response of DeveloperPortalKYBApi->developer_kyb_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalKYBApi->developer_kyb_submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 

### Return type

[**VirtualAccountQueryIndex200Response**](VirtualAccountQueryIndex200Response.md)

### Authorization

[tenantHeader](../README.md#tenantHeader), [hmacAuth](../README.md#hmacAuth), [apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully. |  -  |
**200** | Successful operation. |  -  |
**422** | Submission incomplete or illegal transition |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — not a KYB manager |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

