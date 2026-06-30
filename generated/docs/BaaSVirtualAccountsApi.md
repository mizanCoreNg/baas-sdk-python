# mizancore_baas_generated.BaaSVirtualAccountsApi

All URIs are relative to *https://api.mizancore.ng*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_virtual_accounts_close**](BaaSVirtualAccountsApi.md#developer_virtual_accounts_close) | **POST** /api/v1/developer/virtual-accounts/{id}/close | Close a virtual account
[**developer_virtual_accounts_create**](BaaSVirtualAccountsApi.md#developer_virtual_accounts_create) | **POST** /api/v1/developer/virtual-accounts | Create a virtual account
[**developer_virtual_accounts_index**](BaaSVirtualAccountsApi.md#developer_virtual_accounts_index) | **GET** /api/v1/developer/virtual-accounts | List virtual accounts
[**developer_virtual_accounts_lookup**](BaaSVirtualAccountsApi.md#developer_virtual_accounts_lookup) | **GET** /api/v1/developer/virtual-accounts/lookup | Find virtual account by customer reference
[**developer_virtual_accounts_show**](BaaSVirtualAccountsApi.md#developer_virtual_accounts_show) | **GET** /api/v1/developer/virtual-accounts/{id} | Get virtual account details
[**virtual_account_close**](BaaSVirtualAccountsApi.md#virtual_account_close) | **POST** /api/v1/baas/virtual-accounts/{id}/close | Close a virtual account
[**virtual_account_create**](BaaSVirtualAccountsApi.md#virtual_account_create) | **POST** /api/v1/baas/virtual-accounts | Create a virtual account
[**virtual_account_query_find_by_reference**](BaaSVirtualAccountsApi.md#virtual_account_query_find_by_reference) | **GET** /api/v1/baas/virtual-accounts/lookup | Find virtual account by customer reference
[**virtual_account_query_index**](BaaSVirtualAccountsApi.md#virtual_account_query_index) | **GET** /api/v1/baas/virtual-accounts | List virtual accounts
[**virtual_account_query_show**](BaaSVirtualAccountsApi.md#virtual_account_query_show) | **GET** /api/v1/baas/virtual-accounts/{id} | Get virtual account details


# **developer_virtual_accounts_close**
> VirtualAccountQueryIndex200Response developer_virtual_accounts_close(id, x_tenant_id, idempotency_key)

Close a virtual account

Closes a virtual account, preventing further deposits. The account number will no longer accept inbound transfers.

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
    api_instance = mizancore_baas_generated.BaaSVirtualAccountsApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.

    try:
        # Close a virtual account
        api_response = api_instance.developer_virtual_accounts_close(id, x_tenant_id, idempotency_key)
        print("The response of BaaSVirtualAccountsApi->developer_virtual_accounts_close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaaSVirtualAccountsApi->developer_virtual_accounts_close: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 

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
**422** | Validation failed. |  -  |
**401** | Invalid or missing API key |  -  |
**403** | Partner account is not active |  -  |
**404** | Virtual account not found |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_virtual_accounts_create**
> VirtualAccountQueryIndex200Response developer_virtual_accounts_create(x_tenant_id, idempotency_key)

Create a virtual account

Provisions a new virtual account for a customer. Identity verification (BVN/NIN) may be required depending on the partner tier. A creation fee is charged from the partner wallet.

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
    api_instance = mizancore_baas_generated.BaaSVirtualAccountsApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.

    try:
        # Create a virtual account
        api_response = api_instance.developer_virtual_accounts_create(x_tenant_id, idempotency_key)
        print("The response of BaaSVirtualAccountsApi->developer_virtual_accounts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaaSVirtualAccountsApi->developer_virtual_accounts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 

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
**422** | Validation error, identity required, or identity verification failed |  -  |
**401** | Invalid or missing API key |  -  |
**403** | Partner account is not active |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_virtual_accounts_index**
> VirtualAccountQueryIndex200Response developer_virtual_accounts_index(x_tenant_id)

List virtual accounts

Returns a paginated list of all virtual accounts created by the authenticated partner.

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
    api_instance = mizancore_baas_generated.BaaSVirtualAccountsApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # List virtual accounts
        api_response = api_instance.developer_virtual_accounts_index(x_tenant_id)
        print("The response of BaaSVirtualAccountsApi->developer_virtual_accounts_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaaSVirtualAccountsApi->developer_virtual_accounts_index: %s\n" % e)
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
**401** | Invalid or missing API key |  -  |
**403** | Partner account is not active |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_virtual_accounts_lookup**
> VirtualAccountQueryIndex200Response developer_virtual_accounts_lookup(x_tenant_id)

Find virtual account by customer reference

Looks up a virtual account using the partner-provided customer reference. Returns 404 if no account matches the given reference.

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
    api_instance = mizancore_baas_generated.BaaSVirtualAccountsApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Find virtual account by customer reference
        api_response = api_instance.developer_virtual_accounts_lookup(x_tenant_id)
        print("The response of BaaSVirtualAccountsApi->developer_virtual_accounts_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaaSVirtualAccountsApi->developer_virtual_accounts_lookup: %s\n" % e)
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
**401** | Invalid or missing API key |  -  |
**403** | Partner account is not active |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**404** | No virtual account found for the given customer reference |  -  |
**422** | Validation error — customer_reference is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_virtual_accounts_show**
> VirtualAccountQueryIndex200Response developer_virtual_accounts_show(id, x_tenant_id)

Get virtual account details

Retrieves the full details of a specific virtual account by its ID, including account number and status.

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
    api_instance = mizancore_baas_generated.BaaSVirtualAccountsApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Get virtual account details
        api_response = api_instance.developer_virtual_accounts_show(id, x_tenant_id)
        print("The response of BaaSVirtualAccountsApi->developer_virtual_accounts_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaaSVirtualAccountsApi->developer_virtual_accounts_show: %s\n" % e)
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
**401** | Invalid or missing API key |  -  |
**403** | Partner account is not active |  -  |
**404** | Virtual account not found |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_account_close**
> VirtualAccountQueryIndex200Response virtual_account_close(id, x_tenant_id, idempotency_key)

Close a virtual account

Closes a virtual account, preventing further deposits. The account number will no longer accept inbound transfers.

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
    api_instance = mizancore_baas_generated.BaaSVirtualAccountsApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.

    try:
        # Close a virtual account
        api_response = api_instance.virtual_account_close(id, x_tenant_id, idempotency_key)
        print("The response of BaaSVirtualAccountsApi->virtual_account_close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaaSVirtualAccountsApi->virtual_account_close: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 

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
**422** | Validation failed. |  -  |
**401** | Invalid or missing API key |  -  |
**403** | Partner account is not active |  -  |
**404** | Virtual account not found |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_account_create**
> VirtualAccountQueryIndex200Response virtual_account_create(x_tenant_id, idempotency_key)

Create a virtual account

Provisions a new virtual account for a customer. Identity verification (BVN/NIN) may be required depending on the partner tier. A creation fee is charged from the partner wallet.

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
    api_instance = mizancore_baas_generated.BaaSVirtualAccountsApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.

    try:
        # Create a virtual account
        api_response = api_instance.virtual_account_create(x_tenant_id, idempotency_key)
        print("The response of BaaSVirtualAccountsApi->virtual_account_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaaSVirtualAccountsApi->virtual_account_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 

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
**422** | Validation error, identity required, or identity verification failed |  -  |
**401** | Invalid or missing API key |  -  |
**403** | Partner account is not active |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_account_query_find_by_reference**
> VirtualAccountQueryIndex200Response virtual_account_query_find_by_reference(x_tenant_id)

Find virtual account by customer reference

Looks up a virtual account using the partner-provided customer reference. Returns 404 if no account matches the given reference.

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
    api_instance = mizancore_baas_generated.BaaSVirtualAccountsApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Find virtual account by customer reference
        api_response = api_instance.virtual_account_query_find_by_reference(x_tenant_id)
        print("The response of BaaSVirtualAccountsApi->virtual_account_query_find_by_reference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaaSVirtualAccountsApi->virtual_account_query_find_by_reference: %s\n" % e)
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
**401** | Invalid or missing API key |  -  |
**403** | Partner account is not active |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**404** | No virtual account found for the given customer reference |  -  |
**422** | Validation error — customer_reference is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_account_query_index**
> VirtualAccountQueryIndex200Response virtual_account_query_index(x_tenant_id)

List virtual accounts

Returns a paginated list of all virtual accounts created by the authenticated partner.

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
    api_instance = mizancore_baas_generated.BaaSVirtualAccountsApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # List virtual accounts
        api_response = api_instance.virtual_account_query_index(x_tenant_id)
        print("The response of BaaSVirtualAccountsApi->virtual_account_query_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaaSVirtualAccountsApi->virtual_account_query_index: %s\n" % e)
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
**401** | Invalid or missing API key |  -  |
**403** | Partner account is not active |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_account_query_show**
> VirtualAccountQueryIndex200Response virtual_account_query_show(id, x_tenant_id)

Get virtual account details

Retrieves the full details of a specific virtual account by its ID, including account number and status.

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
    api_instance = mizancore_baas_generated.BaaSVirtualAccountsApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Get virtual account details
        api_response = api_instance.virtual_account_query_show(id, x_tenant_id)
        print("The response of BaaSVirtualAccountsApi->virtual_account_query_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaaSVirtualAccountsApi->virtual_account_query_show: %s\n" % e)
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
**401** | Invalid or missing API key |  -  |
**403** | Partner account is not active |  -  |
**404** | Virtual account not found |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

