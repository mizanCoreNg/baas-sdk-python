# mizancore_baas_generated.DeveloperPortalManagedCustomersApi

All URIs are relative to *https://api.mizancore.ng*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_customers_index**](DeveloperPortalManagedCustomersApi.md#developer_customers_index) | **GET** /api/v1/developer/customers | List managed customers
[**developer_customers_offboard**](DeveloperPortalManagedCustomersApi.md#developer_customers_offboard) | **POST** /api/v1/developer/customers/{customerId}/offboard | Offboard a managed customer
[**developer_customers_reactivate**](DeveloperPortalManagedCustomersApi.md#developer_customers_reactivate) | **POST** /api/v1/developer/customers/{customerId}/reactivate | Reactivate a managed customer
[**developer_customers_show**](DeveloperPortalManagedCustomersApi.md#developer_customers_show) | **GET** /api/v1/developer/customers/{id} | Show a managed customer
[**developer_customers_store**](DeveloperPortalManagedCustomersApi.md#developer_customers_store) | **POST** /api/v1/developer/customers | Onboard a managed customer
[**developer_customers_suspend**](DeveloperPortalManagedCustomersApi.md#developer_customers_suspend) | **POST** /api/v1/developer/customers/{customerId}/suspend | Suspend a managed customer
[**managed_customer_index**](DeveloperPortalManagedCustomersApi.md#managed_customer_index) | **GET** /api/v1/baas/customers | List managed customers
[**managed_customer_lifecycle_offboard**](DeveloperPortalManagedCustomersApi.md#managed_customer_lifecycle_offboard) | **POST** /api/v1/baas/customers/{customerId}/offboard | Offboard a managed customer
[**managed_customer_lifecycle_reactivate**](DeveloperPortalManagedCustomersApi.md#managed_customer_lifecycle_reactivate) | **POST** /api/v1/baas/customers/{customerId}/reactivate | Reactivate a managed customer
[**managed_customer_lifecycle_suspend**](DeveloperPortalManagedCustomersApi.md#managed_customer_lifecycle_suspend) | **POST** /api/v1/baas/customers/{customerId}/suspend | Suspend a managed customer
[**managed_customer_show**](DeveloperPortalManagedCustomersApi.md#managed_customer_show) | **GET** /api/v1/baas/customers/{id} | Show a managed customer
[**managed_customer_store**](DeveloperPortalManagedCustomersApi.md#managed_customer_store) | **POST** /api/v1/baas/customers | Onboard a managed customer


# **developer_customers_index**
> VirtualAccountQueryIndex200Response developer_customers_index(x_tenant_id, per_page=per_page)

List managed customers

Returns the managed customers linked to the authenticated partner. BVN/NIN/phone are masked (PII). Empty for a licensed partner (no links).

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    per_page = 20 # int | Page size (1-100, default 20). (optional)

    try:
        # List managed customers
        api_response = api_instance.developer_customers_index(x_tenant_id, per_page=per_page)
        print("The response of DeveloperPortalManagedCustomersApi->developer_customers_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->developer_customers_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **per_page** | **int**| Page size (1-100, default 20). | [optional] 

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

# **developer_customers_offboard**
> VirtualAccountQueryIndex200Response developer_customers_offboard(customer_id, x_tenant_id, managed_customer_lifecycle_request)

Offboard a managed customer

Severs the partner relationship with a managed customer (active|suspended → offboarded, terminal). Revokes the partner active consents (NDPA lawful-basis withdrawal) and ends all access. The shared customer identity is NOT deleted (other partners + MFB bank-of-record). Managed partners only. Owner/admin/developer only.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.managed_customer_lifecycle_request import ManagedCustomerLifecycleRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    managed_customer_lifecycle_request = {"reason":"example"} # ManagedCustomerLifecycleRequest | 

    try:
        # Offboard a managed customer
        api_response = api_instance.developer_customers_offboard(customer_id, x_tenant_id, managed_customer_lifecycle_request)
        print("The response of DeveloperPortalManagedCustomersApi->developer_customers_offboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->developer_customers_offboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **managed_customer_lifecycle_request** | [**ManagedCustomerLifecycleRequest**](ManagedCustomerLifecycleRequest.md)|  | 

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
**422** | Partner not managed, or already offboarded |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage customer lifecycle |  -  |
**404** | Customer not linked to this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_reactivate**
> VirtualAccountQueryIndex200Response developer_customers_reactivate(customer_id, x_tenant_id, managed_customer_lifecycle_request)

Reactivate a managed customer

Restores a suspended partner relationship (suspended → active). Only a suspended relationship may be reactivated; offboarded is terminal. Managed partners only. Owner/admin/developer only.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.managed_customer_lifecycle_request import ManagedCustomerLifecycleRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    managed_customer_lifecycle_request = {"reason":"example"} # ManagedCustomerLifecycleRequest | 

    try:
        # Reactivate a managed customer
        api_response = api_instance.developer_customers_reactivate(customer_id, x_tenant_id, managed_customer_lifecycle_request)
        print("The response of DeveloperPortalManagedCustomersApi->developer_customers_reactivate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->developer_customers_reactivate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **managed_customer_lifecycle_request** | [**ManagedCustomerLifecycleRequest**](ManagedCustomerLifecycleRequest.md)|  | 

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
**422** | Partner not managed, or illegal lifecycle transition |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage customer lifecycle |  -  |
**404** | Customer not linked to this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_show**
> VirtualAccountQueryIndex200Response developer_customers_show(id, x_tenant_id)

Show a managed customer

Returns a single managed customer linked to the authenticated partner. BOLA: a customer this partner has no link to resolves to 404, never 200. ACTIVE link: a managed partner additionally needs a granted, unexpired ACCOUNT_DETAILS consent for the PII block (403 BAAS_CONSENT_REQUIRED otherwise). NON-ACTIVE link (suspended/offboarded): the partner-owned relationship metadata is always readable (200, status reflects the lifecycle state) but the customer PII block is masked (customer:null, pii_access:false) — NDPA data-minimisation — so the partner can still view and reactivate the relationship.

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Show a managed customer
        api_response = api_instance.developer_customers_show(id, x_tenant_id)
        print("The response of DeveloperPortalManagedCustomersApi->developer_customers_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->developer_customers_show: %s\n" % e)
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
**200** | Successful operation. |  -  |
**401** | Unauthenticated |  -  |
**403** | Consent required — no valid consent for this customer (active link only) |  -  |
**404** | Customer not linked to this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_store**
> VirtualAccountQueryIndex200Response developer_customers_store(x_tenant_id, onboard_managed_customer_request)

Onboard a managed customer

Onboards an MFB-owned end-customer under the partner (find-or-link by BVN — an existing identity is reused with no re-KYC). Managed partners only. Owner/admin/developer only. Idempotent per (partner, BVN).

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.onboard_managed_customer_request import OnboardManagedCustomerRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    onboard_managed_customer_request = {"bvn":"12345678901","nin":"12345678901","first_name":"example","last_name":"example","phone":"+2348012345678","email":"alice@world.test","date_of_birth":"2026-04-21","gender":"male","address":"example","tier":1,"customer_reference":"example"} # OnboardManagedCustomerRequest | 

    try:
        # Onboard a managed customer
        api_response = api_instance.developer_customers_store(x_tenant_id, onboard_managed_customer_request)
        print("The response of DeveloperPortalManagedCustomersApi->developer_customers_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->developer_customers_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **onboard_managed_customer_request** | [**OnboardManagedCustomerRequest**](OnboardManagedCustomerRequest.md)|  | 

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
**422** | Validation error, partner not managed, or insufficient KYC documentation for the requested tier |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot onboard customers |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_suspend**
> VirtualAccountQueryIndex200Response developer_customers_suspend(customer_id, x_tenant_id, managed_customer_lifecycle_request)

Suspend a managed customer

Freezes the partner relationship with a managed customer (active → suspended). The partner can no longer act on the customer (subsequent access 404s) until reactivated. Managed partners only. Owner/admin/developer only.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.managed_customer_lifecycle_request import ManagedCustomerLifecycleRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    managed_customer_lifecycle_request = {"reason":"example"} # ManagedCustomerLifecycleRequest | 

    try:
        # Suspend a managed customer
        api_response = api_instance.developer_customers_suspend(customer_id, x_tenant_id, managed_customer_lifecycle_request)
        print("The response of DeveloperPortalManagedCustomersApi->developer_customers_suspend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->developer_customers_suspend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **managed_customer_lifecycle_request** | [**ManagedCustomerLifecycleRequest**](ManagedCustomerLifecycleRequest.md)|  | 

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
**422** | Partner not managed, or illegal lifecycle transition |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage customer lifecycle |  -  |
**404** | Customer not linked to this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_customer_index**
> VirtualAccountQueryIndex200Response managed_customer_index(x_tenant_id, per_page=per_page)

List managed customers

Returns the managed customers linked to the authenticated partner. BVN/NIN/phone are masked (PII). Empty for a licensed partner (no links).

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    per_page = 20 # int | Page size (1-100, default 20). (optional)

    try:
        # List managed customers
        api_response = api_instance.managed_customer_index(x_tenant_id, per_page=per_page)
        print("The response of DeveloperPortalManagedCustomersApi->managed_customer_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->managed_customer_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **per_page** | **int**| Page size (1-100, default 20). | [optional] 

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

# **managed_customer_lifecycle_offboard**
> VirtualAccountQueryIndex200Response managed_customer_lifecycle_offboard(customer_id, x_tenant_id, idempotency_key, managed_customer_lifecycle_request)

Offboard a managed customer

Severs the partner relationship with a managed customer (active|suspended → offboarded, terminal). Revokes the partner active consents (NDPA lawful-basis withdrawal) and ends all access. The shared customer identity is NOT deleted (other partners + MFB bank-of-record). Managed partners only. Owner/admin/developer only.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.managed_customer_lifecycle_request import ManagedCustomerLifecycleRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    managed_customer_lifecycle_request = {"reason":"CI18 offboard"} # ManagedCustomerLifecycleRequest | 

    try:
        # Offboard a managed customer
        api_response = api_instance.managed_customer_lifecycle_offboard(customer_id, x_tenant_id, idempotency_key, managed_customer_lifecycle_request)
        print("The response of DeveloperPortalManagedCustomersApi->managed_customer_lifecycle_offboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->managed_customer_lifecycle_offboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **managed_customer_lifecycle_request** | [**ManagedCustomerLifecycleRequest**](ManagedCustomerLifecycleRequest.md)|  | 

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
**422** | Partner not managed, or already offboarded |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage customer lifecycle |  -  |
**404** | Customer not linked to this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_customer_lifecycle_reactivate**
> VirtualAccountQueryIndex200Response managed_customer_lifecycle_reactivate(customer_id, x_tenant_id, idempotency_key, managed_customer_lifecycle_request)

Reactivate a managed customer

Restores a suspended partner relationship (suspended → active). Only a suspended relationship may be reactivated; offboarded is terminal. Managed partners only. Owner/admin/developer only.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.managed_customer_lifecycle_request import ManagedCustomerLifecycleRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    managed_customer_lifecycle_request = {"reason":"example"} # ManagedCustomerLifecycleRequest | 

    try:
        # Reactivate a managed customer
        api_response = api_instance.managed_customer_lifecycle_reactivate(customer_id, x_tenant_id, idempotency_key, managed_customer_lifecycle_request)
        print("The response of DeveloperPortalManagedCustomersApi->managed_customer_lifecycle_reactivate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->managed_customer_lifecycle_reactivate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **managed_customer_lifecycle_request** | [**ManagedCustomerLifecycleRequest**](ManagedCustomerLifecycleRequest.md)|  | 

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
**422** | Partner not managed, or illegal lifecycle transition |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage customer lifecycle |  -  |
**404** | Customer not linked to this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_customer_lifecycle_suspend**
> VirtualAccountQueryIndex200Response managed_customer_lifecycle_suspend(customer_id, x_tenant_id, idempotency_key, managed_customer_lifecycle_request)

Suspend a managed customer

Freezes the partner relationship with a managed customer (active → suspended). The partner can no longer act on the customer (subsequent access 404s) until reactivated. Managed partners only. Owner/admin/developer only.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.managed_customer_lifecycle_request import ManagedCustomerLifecycleRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    managed_customer_lifecycle_request = {"reason":"CI18 lifecycle test"} # ManagedCustomerLifecycleRequest | 

    try:
        # Suspend a managed customer
        api_response = api_instance.managed_customer_lifecycle_suspend(customer_id, x_tenant_id, idempotency_key, managed_customer_lifecycle_request)
        print("The response of DeveloperPortalManagedCustomersApi->managed_customer_lifecycle_suspend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->managed_customer_lifecycle_suspend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **managed_customer_lifecycle_request** | [**ManagedCustomerLifecycleRequest**](ManagedCustomerLifecycleRequest.md)|  | 

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
**422** | Partner not managed, or illegal lifecycle transition |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage customer lifecycle |  -  |
**404** | Customer not linked to this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_customer_show**
> VirtualAccountQueryIndex200Response managed_customer_show(id, x_tenant_id)

Show a managed customer

Returns a single managed customer linked to the authenticated partner. BOLA: a customer this partner has no link to resolves to 404, never 200. ACTIVE link: a managed partner additionally needs a granted, unexpired ACCOUNT_DETAILS consent for the PII block (403 BAAS_CONSENT_REQUIRED otherwise). NON-ACTIVE link (suspended/offboarded): the partner-owned relationship metadata is always readable (200, status reflects the lifecycle state) but the customer PII block is masked (customer:null, pii_access:false) — NDPA data-minimisation — so the partner can still view and reactivate the relationship.

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Show a managed customer
        api_response = api_instance.managed_customer_show(id, x_tenant_id)
        print("The response of DeveloperPortalManagedCustomersApi->managed_customer_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->managed_customer_show: %s\n" % e)
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
**200** | Successful operation. |  -  |
**401** | Unauthenticated |  -  |
**403** | Consent required — no valid consent for this customer (active link only) |  -  |
**404** | Customer not linked to this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_customer_store**
> VirtualAccountQueryIndex200Response managed_customer_store(x_tenant_id, idempotency_key, onboard_managed_customer_request)

Onboard a managed customer

Onboards an MFB-owned end-customer under the partner (find-or-link by BVN — an existing identity is reused with no re-KYC). Managed partners only. Owner/admin/developer only. Idempotent per (partner, BVN).

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.onboard_managed_customer_request import OnboardManagedCustomerRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCustomersApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    onboard_managed_customer_request = {"bvn":"22281800001","first_name":"Ngozi","last_name":"Eze","phone":"08031800001","date_of_birth":"1991-03-12","tier":1,"customer_reference":"ci18-user-001"} # OnboardManagedCustomerRequest | 

    try:
        # Onboard a managed customer
        api_response = api_instance.managed_customer_store(x_tenant_id, idempotency_key, onboard_managed_customer_request)
        print("The response of DeveloperPortalManagedCustomersApi->managed_customer_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCustomersApi->managed_customer_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **onboard_managed_customer_request** | [**OnboardManagedCustomerRequest**](OnboardManagedCustomerRequest.md)|  | 

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
**422** | Validation error, partner not managed, or insufficient KYC documentation for the requested tier |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot onboard customers |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

