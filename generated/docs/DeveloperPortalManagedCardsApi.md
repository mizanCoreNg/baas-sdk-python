# mizancore_baas_generated.DeveloperPortalManagedCardsApi

All URIs are relative to *https://api.mizancore.ng*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_customers_accounts_cards_freeze**](DeveloperPortalManagedCardsApi.md#developer_customers_accounts_cards_freeze) | **POST** /api/v1/developer/customers/{customerId}/accounts/{accountId}/cards/{cardId}/freeze | Freeze a managed card
[**developer_customers_accounts_cards_index**](DeveloperPortalManagedCardsApi.md#developer_customers_accounts_cards_index) | **GET** /api/v1/developer/customers/{customerId}/accounts/{accountId}/cards | List managed cards for an account
[**developer_customers_accounts_cards_issue**](DeveloperPortalManagedCardsApi.md#developer_customers_accounts_cards_issue) | **POST** /api/v1/developer/customers/{customerId}/accounts/{accountId}/cards | Issue a managed virtual card
[**developer_customers_accounts_cards_limits**](DeveloperPortalManagedCardsApi.md#developer_customers_accounts_cards_limits) | **PUT** /api/v1/developer/customers/{customerId}/accounts/{accountId}/cards/{cardId}/limits | Set managed card spending limits
[**developer_customers_accounts_cards_pin**](DeveloperPortalManagedCardsApi.md#developer_customers_accounts_cards_pin) | **POST** /api/v1/developer/customers/{customerId}/accounts/{accountId}/cards/{cardId}/pin | Set or change a managed card PIN
[**developer_customers_accounts_cards_show**](DeveloperPortalManagedCardsApi.md#developer_customers_accounts_cards_show) | **GET** /api/v1/developer/customers/{customerId}/accounts/{accountId}/cards/{cardId} | Show a managed card
[**developer_customers_accounts_cards_terminate**](DeveloperPortalManagedCardsApi.md#developer_customers_accounts_cards_terminate) | **POST** /api/v1/developer/customers/{customerId}/accounts/{accountId}/cards/{cardId}/terminate | Terminate a managed card
[**developer_customers_accounts_cards_transactions**](DeveloperPortalManagedCardsApi.md#developer_customers_accounts_cards_transactions) | **GET** /api/v1/developer/customers/{customerId}/accounts/{accountId}/cards/{cardId}/transactions | List managed card transactions
[**developer_customers_accounts_cards_unfreeze**](DeveloperPortalManagedCardsApi.md#developer_customers_accounts_cards_unfreeze) | **POST** /api/v1/developer/customers/{customerId}/accounts/{accountId}/cards/{cardId}/unfreeze | Unfreeze a managed card
[**managed_card_issue**](DeveloperPortalManagedCardsApi.md#managed_card_issue) | **POST** /api/v1/baas/customers/{customerId}/accounts/{accountId}/cards | Issue a managed virtual card
[**managed_card_lifecycle_freeze**](DeveloperPortalManagedCardsApi.md#managed_card_lifecycle_freeze) | **POST** /api/v1/baas/customers/{customerId}/accounts/{accountId}/cards/{cardId}/freeze | Freeze a managed card
[**managed_card_lifecycle_set_limits**](DeveloperPortalManagedCardsApi.md#managed_card_lifecycle_set_limits) | **PUT** /api/v1/baas/customers/{customerId}/accounts/{accountId}/cards/{cardId}/limits | Set managed card spending limits
[**managed_card_lifecycle_set_pin**](DeveloperPortalManagedCardsApi.md#managed_card_lifecycle_set_pin) | **POST** /api/v1/baas/customers/{customerId}/accounts/{accountId}/cards/{cardId}/pin | Set or change a managed card PIN
[**managed_card_lifecycle_terminate**](DeveloperPortalManagedCardsApi.md#managed_card_lifecycle_terminate) | **POST** /api/v1/baas/customers/{customerId}/accounts/{accountId}/cards/{cardId}/terminate | Terminate a managed card
[**managed_card_lifecycle_unfreeze**](DeveloperPortalManagedCardsApi.md#managed_card_lifecycle_unfreeze) | **POST** /api/v1/baas/customers/{customerId}/accounts/{accountId}/cards/{cardId}/unfreeze | Unfreeze a managed card
[**managed_card_read_index**](DeveloperPortalManagedCardsApi.md#managed_card_read_index) | **GET** /api/v1/baas/customers/{customerId}/accounts/{accountId}/cards | List managed cards for an account
[**managed_card_read_show**](DeveloperPortalManagedCardsApi.md#managed_card_read_show) | **GET** /api/v1/baas/customers/{customerId}/accounts/{accountId}/cards/{cardId} | Show a managed card
[**managed_card_read_transactions**](DeveloperPortalManagedCardsApi.md#managed_card_read_transactions) | **GET** /api/v1/baas/customers/{customerId}/accounts/{accountId}/cards/{cardId}/transactions | List managed card transactions


# **developer_customers_accounts_cards_freeze**
> VirtualAccountQueryIndex200Response developer_customers_accounts_cards_freeze(customer_id, account_id, card_id, x_tenant_id, idempotency_key)

Freeze a managed card

Freezes (suspends) one of the partner's managed cards — reversible via unfreeze. Managed partners only; MANAGE_CARD consent required. Idempotent. Returns the masked card.

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.

    try:
        # Freeze a managed card
        api_response = api_instance.developer_customers_accounts_cards_freeze(customer_id, account_id, card_id, x_tenant_id, idempotency_key)
        print("The response of DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_freeze:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_freeze: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
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
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_accounts_cards_index**
> VirtualAccountQueryIndex200Response developer_customers_accounts_cards_index(customer_id, account_id, x_tenant_id)

List managed cards for an account

Lists every card bound to one of the partner's sponsored accounts, newest first. Managed partners only; MANAGE_CARD consent required. Returns masked PANs only (never the raw card).

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # List managed cards for an account
        api_response = api_instance.developer_customers_accounts_cards_index(customer_id, account_id, x_tenant_id)
        print("The response of DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
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
**403** | Forbidden — cannot read cards, or no valid MANAGE_CARD consent |  -  |
**404** | Account not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_accounts_cards_issue**
> VirtualAccountQueryIndex200Response developer_customers_accounts_cards_issue(customer_id, account_id, x_tenant_id, idempotency_key, issue_managed_card_request)

Issue a managed virtual card

Issues a VIRTUAL debit card for one of the partner's sponsored accounts, inheriting the MFB tenant's card scheme/processor (sandbox → Fake/Mock adapter, no real card minted). Managed partners only; ISSUE_CARD consent required. Returns a masked PAN, never the raw card. Idempotent.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.issue_managed_card_request import IssueManagedCardRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    issue_managed_card_request = {"nickname":"example","limits":{}} # IssueManagedCardRequest | 

    try:
        # Issue a managed virtual card
        api_response = api_instance.developer_customers_accounts_cards_issue(customer_id, account_id, x_tenant_id, idempotency_key, issue_managed_card_request)
        print("The response of DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **issue_managed_card_request** | [**IssueManagedCardRequest**](IssueManagedCardRequest.md)|  | 

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
**422** | Validation error, partner not managed, or no tenant card scheme configured |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot issue cards, or no valid ISSUE_CARD consent for this customer |  -  |
**404** | Customer not linked / account not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_accounts_cards_limits**
> VirtualAccountQueryIndex200Response developer_customers_accounts_cards_limits(customer_id, account_id, card_id, x_tenant_id, idempotency_key, set_managed_card_limits_request)

Set managed card spending limits

Sets per-card spending limits (daily ATM/POS/web + per-transaction, all in kobo) on a managed card. Partner-authorized: managed partners only; MANAGE_CARD consent + card ownership required.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.set_managed_card_limits_request import SetManagedCardLimitsRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    set_managed_card_limits_request = {"limits":{}} # SetManagedCardLimitsRequest | 

    try:
        # Set managed card spending limits
        api_response = api_instance.developer_customers_accounts_cards_limits(customer_id, account_id, card_id, x_tenant_id, idempotency_key, set_managed_card_limits_request)
        print("The response of DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_limits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **set_managed_card_limits_request** | [**SetManagedCardLimitsRequest**](SetManagedCardLimitsRequest.md)|  | 

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
**422** | Validation error (no limit keys / non-integer kobo) |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_accounts_cards_pin**
> VirtualAccountQueryIndex200Response developer_customers_accounts_cards_pin(customer_id, account_id, card_id, x_tenant_id, idempotency_key, set_managed_card_pin_request)

Set or change a managed card PIN

Sets or changes a managed card's PIN via the processor's secure PIN path. The raw PIN is transient — never persisted or logged at any layer. Managed partners only; MANAGE_CARD consent required. Returns the masked card (no PIN echo).

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.set_managed_card_pin_request import SetManagedCardPinRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    set_managed_card_pin_request = {"pin":"example","current_pin":"example"} # SetManagedCardPinRequest | 

    try:
        # Set or change a managed card PIN
        api_response = api_instance.developer_customers_accounts_cards_pin(customer_id, account_id, card_id, x_tenant_id, idempotency_key, set_managed_card_pin_request)
        print("The response of DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **set_managed_card_pin_request** | [**SetManagedCardPinRequest**](SetManagedCardPinRequest.md)|  | 

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
**422** | Validation error (PIN not 4 digits) |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_accounts_cards_show**
> VirtualAccountQueryIndex200Response developer_customers_accounts_cards_show(customer_id, account_id, card_id, x_tenant_id)

Show a managed card

Returns one of the partner's managed cards — status, masked PAN + last4, expiry, network/scheme, and lifecycle state. Managed partners only; MANAGE_CARD consent + card ownership required. Never the raw card.

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Show a managed card
        api_response = api_instance.developer_customers_accounts_cards_show(customer_id, account_id, card_id, x_tenant_id)
        print("The response of DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
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
**403** | Forbidden — cannot read cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_accounts_cards_terminate**
> VirtualAccountQueryIndex200Response developer_customers_accounts_cards_terminate(customer_id, account_id, card_id, x_tenant_id, idempotency_key, terminate_managed_card_request)

Terminate a managed card

Permanently terminates a managed card — IRREVERSIBLE (the card can never transact or be re-activated). Partner-authorized: managed partners only; MANAGE_CARD consent + card ownership required. Returns the masked card.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.terminate_managed_card_request import TerminateManagedCardRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    terminate_managed_card_request = {"reason":"example"} # TerminateManagedCardRequest | 

    try:
        # Terminate a managed card
        api_response = api_instance.developer_customers_accounts_cards_terminate(customer_id, account_id, card_id, x_tenant_id, idempotency_key, terminate_managed_card_request)
        print("The response of DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_terminate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_terminate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **terminate_managed_card_request** | [**TerminateManagedCardRequest**](TerminateManagedCardRequest.md)|  | 

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
**422** | Validation failed. |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_accounts_cards_transactions**
> VirtualAccountQueryIndex200Response developer_customers_accounts_cards_transactions(customer_id, account_id, card_id, x_tenant_id, per_page=per_page, page=page)

List managed card transactions

Returns a paginated transaction history for one of the partner's managed cards, newest first. Money values are in kobo. Managed partners only; requires a granted TRANSACTION_HISTORY consent for the customer (stronger than MANAGE_CARD — reading card spend history is a distinct purpose) + card ownership.

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    per_page = 56 # int | Page size (1–100, default 20). (optional)
    page = 56 # int | 1-based page number (default 1). (optional)

    try:
        # List managed card transactions
        api_response = api_instance.developer_customers_accounts_cards_transactions(customer_id, account_id, card_id, x_tenant_id, per_page=per_page, page=page)
        print("The response of DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **per_page** | **int**| Page size (1–100, default 20). | [optional] 
 **page** | **int**| 1-based page number (default 1). | [optional] 

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
**403** | Forbidden — no valid TRANSACTION_HISTORY consent for this customer |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_customers_accounts_cards_unfreeze**
> VirtualAccountQueryIndex200Response developer_customers_accounts_cards_unfreeze(customer_id, account_id, card_id, x_tenant_id, idempotency_key)

Unfreeze a managed card

Unfreezes (resumes) a previously-frozen managed card → active. A terminated card can never be unfrozen. Managed partners only; MANAGE_CARD consent required. Idempotent. Returns the masked card.

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.

    try:
        # Unfreeze a managed card
        api_response = api_instance.developer_customers_accounts_cards_unfreeze(customer_id, account_id, card_id, x_tenant_id, idempotency_key)
        print("The response of DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_unfreeze:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->developer_customers_accounts_cards_unfreeze: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
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
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_card_issue**
> VirtualAccountQueryIndex200Response managed_card_issue(customer_id, account_id, x_tenant_id, idempotency_key, issue_managed_card_request)

Issue a managed virtual card

Issues a VIRTUAL debit card for one of the partner's sponsored accounts, inheriting the MFB tenant's card scheme/processor (sandbox → Fake/Mock adapter, no real card minted). Managed partners only; ISSUE_CARD consent required. Returns a masked PAN, never the raw card. Idempotent.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.issue_managed_card_request import IssueManagedCardRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    issue_managed_card_request = {"nickname":"example","limits":{}} # IssueManagedCardRequest | 

    try:
        # Issue a managed virtual card
        api_response = api_instance.managed_card_issue(customer_id, account_id, x_tenant_id, idempotency_key, issue_managed_card_request)
        print("The response of DeveloperPortalManagedCardsApi->managed_card_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->managed_card_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **issue_managed_card_request** | [**IssueManagedCardRequest**](IssueManagedCardRequest.md)|  | 

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
**422** | Validation error, partner not managed, or no tenant card scheme configured |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot issue cards, or no valid ISSUE_CARD consent for this customer |  -  |
**404** | Customer not linked / account not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_card_lifecycle_freeze**
> VirtualAccountQueryIndex200Response managed_card_lifecycle_freeze(customer_id, account_id, card_id, x_tenant_id, idempotency_key)

Freeze a managed card

Freezes (suspends) one of the partner's managed cards — reversible via unfreeze. Managed partners only; MANAGE_CARD consent required. Idempotent. Returns the masked card.

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.

    try:
        # Freeze a managed card
        api_response = api_instance.managed_card_lifecycle_freeze(customer_id, account_id, card_id, x_tenant_id, idempotency_key)
        print("The response of DeveloperPortalManagedCardsApi->managed_card_lifecycle_freeze:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->managed_card_lifecycle_freeze: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
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
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_card_lifecycle_set_limits**
> VirtualAccountQueryIndex200Response managed_card_lifecycle_set_limits(customer_id, account_id, card_id, x_tenant_id, idempotency_key, set_managed_card_limits_request)

Set managed card spending limits

Sets per-card spending limits (daily ATM/POS/web + per-transaction, all in kobo) on a managed card. Partner-authorized: managed partners only; MANAGE_CARD consent + card ownership required.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.set_managed_card_limits_request import SetManagedCardLimitsRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    set_managed_card_limits_request = {"limits":{}} # SetManagedCardLimitsRequest | 

    try:
        # Set managed card spending limits
        api_response = api_instance.managed_card_lifecycle_set_limits(customer_id, account_id, card_id, x_tenant_id, idempotency_key, set_managed_card_limits_request)
        print("The response of DeveloperPortalManagedCardsApi->managed_card_lifecycle_set_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->managed_card_lifecycle_set_limits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **set_managed_card_limits_request** | [**SetManagedCardLimitsRequest**](SetManagedCardLimitsRequest.md)|  | 

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
**422** | Validation error (no limit keys / non-integer kobo) |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_card_lifecycle_set_pin**
> VirtualAccountQueryIndex200Response managed_card_lifecycle_set_pin(customer_id, account_id, card_id, x_tenant_id, idempotency_key, set_managed_card_pin_request)

Set or change a managed card PIN

Sets or changes a managed card's PIN via the processor's secure PIN path. The raw PIN is transient — never persisted or logged at any layer. Managed partners only; MANAGE_CARD consent required. Returns the masked card (no PIN echo).

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.set_managed_card_pin_request import SetManagedCardPinRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    set_managed_card_pin_request = {"pin":"example","current_pin":"example"} # SetManagedCardPinRequest | 

    try:
        # Set or change a managed card PIN
        api_response = api_instance.managed_card_lifecycle_set_pin(customer_id, account_id, card_id, x_tenant_id, idempotency_key, set_managed_card_pin_request)
        print("The response of DeveloperPortalManagedCardsApi->managed_card_lifecycle_set_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->managed_card_lifecycle_set_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **set_managed_card_pin_request** | [**SetManagedCardPinRequest**](SetManagedCardPinRequest.md)|  | 

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
**422** | Validation error (PIN not 4 digits) |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_card_lifecycle_terminate**
> VirtualAccountQueryIndex200Response managed_card_lifecycle_terminate(customer_id, account_id, card_id, x_tenant_id, idempotency_key, terminate_managed_card_request)

Terminate a managed card

Permanently terminates a managed card — IRREVERSIBLE (the card can never transact or be re-activated). Partner-authorized: managed partners only; MANAGE_CARD consent + card ownership required. Returns the masked card.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.terminate_managed_card_request import TerminateManagedCardRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.
    terminate_managed_card_request = {"reason":"example"} # TerminateManagedCardRequest | 

    try:
        # Terminate a managed card
        api_response = api_instance.managed_card_lifecycle_terminate(customer_id, account_id, card_id, x_tenant_id, idempotency_key, terminate_managed_card_request)
        print("The response of DeveloperPortalManagedCardsApi->managed_card_lifecycle_terminate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->managed_card_lifecycle_terminate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **idempotency_key** | **str**| Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true. | 
 **terminate_managed_card_request** | [**TerminateManagedCardRequest**](TerminateManagedCardRequest.md)|  | 

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
**422** | Validation failed. |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_card_lifecycle_unfreeze**
> VirtualAccountQueryIndex200Response managed_card_lifecycle_unfreeze(customer_id, account_id, card_id, x_tenant_id, idempotency_key)

Unfreeze a managed card

Unfreezes (resumes) a previously-frozen managed card → active. A terminated card can never be unfrozen. Managed partners only; MANAGE_CARD consent required. Idempotent. Returns the masked card.

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    idempotency_key = 'idempotency_key_example' # str | Unique client-generated key (UUID recommended) for idempotent retry semantics. Duplicate requests return the cached response with header Idempotency-Replayed: true.

    try:
        # Unfreeze a managed card
        api_response = api_instance.managed_card_lifecycle_unfreeze(customer_id, account_id, card_id, x_tenant_id, idempotency_key)
        print("The response of DeveloperPortalManagedCardsApi->managed_card_lifecycle_unfreeze:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->managed_card_lifecycle_unfreeze: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
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
**401** | Unauthenticated |  -  |
**403** | Forbidden — cannot manage cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**409** | Idempotency-Key conflict — same key replayed with a different payload, or another request is concurrently processing this key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_card_read_index**
> VirtualAccountQueryIndex200Response managed_card_read_index(customer_id, account_id, x_tenant_id)

List managed cards for an account

Lists every card bound to one of the partner's sponsored accounts, newest first. Managed partners only; MANAGE_CARD consent required. Returns masked PANs only (never the raw card).

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # List managed cards for an account
        api_response = api_instance.managed_card_read_index(customer_id, account_id, x_tenant_id)
        print("The response of DeveloperPortalManagedCardsApi->managed_card_read_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->managed_card_read_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
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
**403** | Forbidden — cannot read cards, or no valid MANAGE_CARD consent |  -  |
**404** | Account not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_card_read_show**
> VirtualAccountQueryIndex200Response managed_card_read_show(customer_id, account_id, card_id, x_tenant_id)

Show a managed card

Returns one of the partner's managed cards — status, masked PAN + last4, expiry, network/scheme, and lifecycle state. Managed partners only; MANAGE_CARD consent + card ownership required. Never the raw card.

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Show a managed card
        api_response = api_instance.managed_card_read_show(customer_id, account_id, card_id, x_tenant_id)
        print("The response of DeveloperPortalManagedCardsApi->managed_card_read_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->managed_card_read_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
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
**403** | Forbidden — cannot read cards, or no valid MANAGE_CARD consent |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_card_read_transactions**
> VirtualAccountQueryIndex200Response managed_card_read_transactions(customer_id, account_id, card_id, x_tenant_id, per_page=per_page, page=page)

List managed card transactions

Returns a paginated transaction history for one of the partner's managed cards, newest first. Money values are in kobo. Managed partners only; requires a granted TRANSACTION_HISTORY consent for the customer (stronger than MANAGE_CARD — reading card spend history is a distinct purpose) + card ownership.

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
    api_instance = mizancore_baas_generated.DeveloperPortalManagedCardsApi(api_client)
    customer_id = '00000000-0000-0000-0000-000000000001' # str | 
    account_id = '00000000-0000-0000-0000-000000000001' # str | 
    card_id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    per_page = 56 # int | Page size (1–100, default 20). (optional)
    page = 56 # int | 1-based page number (default 1). (optional)

    try:
        # List managed card transactions
        api_response = api_instance.managed_card_read_transactions(customer_id, account_id, card_id, x_tenant_id, per_page=per_page, page=page)
        print("The response of DeveloperPortalManagedCardsApi->managed_card_read_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalManagedCardsApi->managed_card_read_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **card_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **per_page** | **int**| Page size (1–100, default 20). | [optional] 
 **page** | **int**| 1-based page number (default 1). | [optional] 

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
**403** | Forbidden — no valid TRANSACTION_HISTORY consent for this customer |  -  |
**404** | Card not found / not owned by this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

