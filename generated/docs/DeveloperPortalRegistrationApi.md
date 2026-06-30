# mizancore_baas_generated.DeveloperPortalRegistrationApi

All URIs are relative to *https://api.mizancore.ng*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_registration_register**](DeveloperPortalRegistrationApi.md#developer_registration_register) | **POST** /api/v1/developer/register | Register as a developer partner
[**developer_registration_verify_email**](DeveloperPortalRegistrationApi.md#developer_registration_verify_email) | **POST** /api/v1/developer/verify-email | Verify developer email address


# **developer_registration_register**
> DeveloperRegistrationRegister201Response developer_registration_register(x_tenant_id, register_developer_request)

Register as a developer partner

Self-service registration for developers wanting to integrate with the BaaS platform. Creates a partner with pending_approval status.

### Example


```python
import mizancore_baas_generated
from mizancore_baas_generated.models.developer_registration_register201_response import DeveloperRegistrationRegister201Response
from mizancore_baas_generated.models.register_developer_request import RegisterDeveloperRequest
from mizancore_baas_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mizancore.ng
# See configuration.py for a list of all supported configuration parameters.
configuration = mizancore_baas_generated.Configuration(
    host = "https://api.mizancore.ng"
)


# Enter a context with an instance of the API client
with mizancore_baas_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mizancore_baas_generated.DeveloperPortalRegistrationApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    register_developer_request = {"company_name":"DC02 Test Partner Ltd","contact_email":"dc02-register-11111111-0000-0000-0000-000000000001@world.test","contact_name":"DC02 Contact","use_case_description":"Slice 8 coverage happy-path registration probe.","website_url":"https://dc02.example.test"} # RegisterDeveloperRequest | 

    try:
        # Register as a developer partner
        api_response = api_instance.developer_registration_register(x_tenant_id, register_developer_request)
        print("The response of DeveloperPortalRegistrationApi->developer_registration_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalRegistrationApi->developer_registration_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **register_developer_request** | [**RegisterDeveloperRequest**](RegisterDeveloperRequest.md)|  | 

### Return type

[**DeveloperRegistrationRegister201Response**](DeveloperRegistrationRegister201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully. |  -  |
**200** | Successful operation. |  -  |
**422** | Validation error |  -  |
**401** | Unauthenticated. |  -  |
**403** | Unauthorized (insufficient permissions). |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Email already registered |  -  |
**429** | Rate limit exceeded — max 5 registrations per hour |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_registration_verify_email**
> DeveloperRegistrationRegister201Response developer_registration_verify_email(x_tenant_id, verify_developer_email_request)

Verify developer email address

Verifies the developer email address using the token sent during registration.

### Example


```python
import mizancore_baas_generated
from mizancore_baas_generated.models.developer_registration_register201_response import DeveloperRegistrationRegister201Response
from mizancore_baas_generated.models.verify_developer_email_request import VerifyDeveloperEmailRequest
from mizancore_baas_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mizancore.ng
# See configuration.py for a list of all supported configuration parameters.
configuration = mizancore_baas_generated.Configuration(
    host = "https://api.mizancore.ng"
)


# Enter a context with an instance of the API client
with mizancore_baas_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mizancore_baas_generated.DeveloperPortalRegistrationApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    verify_developer_email_request = {"token":"0000000000000000000000000000000000000000000000000000000000000001","email":"cq01-probe@example.com"} # VerifyDeveloperEmailRequest | 

    try:
        # Verify developer email address
        api_response = api_instance.developer_registration_verify_email(x_tenant_id, verify_developer_email_request)
        print("The response of DeveloperPortalRegistrationApi->developer_registration_verify_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalRegistrationApi->developer_registration_verify_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **verify_developer_email_request** | [**VerifyDeveloperEmailRequest**](VerifyDeveloperEmailRequest.md)|  | 

### Return type

[**DeveloperRegistrationRegister201Response**](DeveloperRegistrationRegister201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully. |  -  |
**200** | Successful operation. |  -  |
**422** | Validation error |  -  |
**401** | Invalid or expired verification token |  -  |
**403** | Unauthorized (insufficient permissions). |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

