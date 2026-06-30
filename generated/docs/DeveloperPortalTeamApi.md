# mizancore_baas_generated.DeveloperPortalTeamApi

All URIs are relative to *https://api.mizancore.ng*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_team_accept_invite**](DeveloperPortalTeamApi.md#developer_team_accept_invite) | **POST** /api/v1/developer/team/accept-invite | Accept a team invitation
[**developer_team_index**](DeveloperPortalTeamApi.md#developer_team_index) | **GET** /api/v1/developer/team | List team members
[**developer_team_invite**](DeveloperPortalTeamApi.md#developer_team_invite) | **POST** /api/v1/developer/team/invite | Invite a team member
[**developer_team_remove**](DeveloperPortalTeamApi.md#developer_team_remove) | **DELETE** /api/v1/developer/team/{id} | Remove a team member
[**developer_team_resend_invite**](DeveloperPortalTeamApi.md#developer_team_resend_invite) | **POST** /api/v1/developer/team/{id}/resend-invite | Resend a team invitation
[**developer_team_role**](DeveloperPortalTeamApi.md#developer_team_role) | **PATCH** /api/v1/developer/team/{id}/role | Change a team member role


# **developer_team_accept_invite**
> VirtualAccountQueryIndex200Response developer_team_accept_invite(x_tenant_id, accept_invite_request)

Accept a team invitation

Public, token-gated. Verifies the email/token pair, sets the new password, and activates the member so they can log in.

### Example


```python
import mizancore_baas_generated
from mizancore_baas_generated.models.accept_invite_request import AcceptInviteRequest
from mizancore_baas_generated.models.virtual_account_query_index200_response import VirtualAccountQueryIndex200Response
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
    api_instance = mizancore_baas_generated.DeveloperPortalTeamApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    accept_invite_request = {"email":"alice@world.test","token":"example","password":"example"} # AcceptInviteRequest | 

    try:
        # Accept a team invitation
        api_response = api_instance.developer_team_accept_invite(x_tenant_id, accept_invite_request)
        print("The response of DeveloperPortalTeamApi->developer_team_accept_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalTeamApi->developer_team_accept_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **accept_invite_request** | [**AcceptInviteRequest**](AcceptInviteRequest.md)|  | 

### Return type

[**VirtualAccountQueryIndex200Response**](VirtualAccountQueryIndex200Response.md)

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
**401** | Invalid or expired invitation token |  -  |
**403** | Unauthorized (insufficient permissions). |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_team_index**
> VirtualAccountQueryIndex200Response developer_team_index(x_tenant_id)

List team members

Returns all PartnerUsers belonging to the authenticated partner.

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
    api_instance = mizancore_baas_generated.DeveloperPortalTeamApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # List team members
        api_response = api_instance.developer_team_index(x_tenant_id)
        print("The response of DeveloperPortalTeamApi->developer_team_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalTeamApi->developer_team_index: %s\n" % e)
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

# **developer_team_invite**
> VirtualAccountQueryIndex200Response developer_team_invite(x_tenant_id, invite_member_request)

Invite a team member

Invites a teammate by email + role. Owner/admin only. The member is created without a password and must accept the invite to log in.

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.invite_member_request import InviteMemberRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalTeamApi(api_client)
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    invite_member_request = {"email":"alice@world.test","name":"example","role":"owner"} # InviteMemberRequest | 

    try:
        # Invite a team member
        api_response = api_instance.developer_team_invite(x_tenant_id, invite_member_request)
        print("The response of DeveloperPortalTeamApi->developer_team_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalTeamApi->developer_team_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **invite_member_request** | [**InviteMemberRequest**](InviteMemberRequest.md)|  | 

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
**422** | Validation error or duplicate email |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — not a team manager |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_team_remove**
> VirtualAccountQueryIndex200Response developer_team_remove(id, x_tenant_id)

Remove a team member

Removes a member from the partner team. Owner/admin only. The last owner cannot be removed (422).

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
    api_instance = mizancore_baas_generated.DeveloperPortalTeamApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Remove a team member
        api_response = api_instance.developer_team_remove(id, x_tenant_id)
        print("The response of DeveloperPortalTeamApi->developer_team_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalTeamApi->developer_team_remove: %s\n" % e)
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
**403** | Forbidden — not a team manager |  -  |
**404** | Member not found in this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |
**422** | Last-owner protection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_team_resend_invite**
> VirtualAccountQueryIndex200Response developer_team_resend_invite(id, x_tenant_id)

Resend a team invitation

Re-issues the one-time invite token for a member who has not yet accepted. Owner/admin only.

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
    api_instance = mizancore_baas_generated.DeveloperPortalTeamApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.

    try:
        # Resend a team invitation
        api_response = api_instance.developer_team_resend_invite(id, x_tenant_id)
        print("The response of DeveloperPortalTeamApi->developer_team_resend_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalTeamApi->developer_team_resend_invite: %s\n" % e)
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
**201** | Resource created successfully. |  -  |
**200** | Successful operation. |  -  |
**422** | Member has already accepted |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — not a team manager |  -  |
**404** | Member not found in this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_team_role**
> VirtualAccountQueryIndex200Response developer_team_role(id, x_tenant_id, change_member_role_request)

Change a team member role

Updates a member role. Owner/admin only. The last owner cannot be demoted (422).

### Example

* Api Key Authentication (tenantHeader):
* Api Key Authentication (hmacAuth):
* Api Key Authentication (apiKeyAuth):

```python
import mizancore_baas_generated
from mizancore_baas_generated.models.change_member_role_request import ChangeMemberRoleRequest
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
    api_instance = mizancore_baas_generated.DeveloperPortalTeamApi(api_client)
    id = '00000000-0000-0000-0000-000000000001' # str | 
    x_tenant_id = 'world.test.localhost' # str | Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts.
    change_member_role_request = {"role":"owner"} # ChangeMemberRoleRequest | 

    try:
        # Change a team member role
        api_response = api_instance.developer_team_role(id, x_tenant_id, change_member_role_request)
        print("The response of DeveloperPortalTeamApi->developer_team_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperPortalTeamApi->developer_team_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant identifier (UUID or domain, e.g. world.test.localhost). Required on every tenant-scoped route. Maps to the tenant whose database serves this request. In production, prefer Host-header-based resolution; X-Tenant-ID is intended for non-production environments and is rejected (HTTP 400) on production hosts. | 
 **change_member_role_request** | [**ChangeMemberRoleRequest**](ChangeMemberRoleRequest.md)|  | 

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
**422** | Last-owner protection |  -  |
**401** | Unauthenticated |  -  |
**403** | Forbidden — not a team manager |  -  |
**404** | Member not found in this partner |  -  |
**400** | Bad Request — tenant routing information missing or invalid (e.g. neither Host header nor X-Tenant-ID resolved to a tenant), or X-Tenant-ID supplied in production where it is disallowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

