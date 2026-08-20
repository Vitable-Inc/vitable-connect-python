# Auth

Types:

```python
from vitable_connect.types import (
    AuthCompleteProfileResponse,
    AuthIssueAccessTokenResponse,
    AuthListPersonasResponse,
    AuthLoginResponse,
    AuthRetrieveMeResponse,
    AuthSignUpResponse,
)
```

Methods:

- <code title="post /v1/auth/complete-profile">client.auth.<a href="./src/vitable_connect/resources/auth.py">complete_profile</a>(\*\*<a href="src/vitable_connect/types/auth_complete_profile_params.py">params</a>) -> <a href="./src/vitable_connect/types/auth_complete_profile_response.py">AuthCompleteProfileResponse</a></code>
- <code title="post /v1/auth/access-tokens">client.auth.<a href="./src/vitable_connect/resources/auth.py">issue_access_token</a>(\*\*<a href="src/vitable_connect/types/auth_issue_access_token_params.py">params</a>) -> <a href="./src/vitable_connect/types/auth_issue_access_token_response.py">AuthIssueAccessTokenResponse</a></code>
- <code title="get /v1/auth/personas">client.auth.<a href="./src/vitable_connect/resources/auth.py">list_personas</a>() -> <a href="./src/vitable_connect/types/auth_list_personas_response.py">AuthListPersonasResponse</a></code>
- <code title="post /v1/auth/login">client.auth.<a href="./src/vitable_connect/resources/auth.py">login</a>(\*\*<a href="src/vitable_connect/types/auth_login_params.py">params</a>) -> <a href="./src/vitable_connect/types/auth_login_response.py">AuthLoginResponse</a></code>
- <code title="get /v1/auth/me">client.auth.<a href="./src/vitable_connect/resources/auth.py">retrieve_me</a>() -> <a href="./src/vitable_connect/types/auth_retrieve_me_response.py">AuthRetrieveMeResponse</a></code>
- <code title="post /v1/auth/sign-up">client.auth.<a href="./src/vitable_connect/resources/auth.py">sign_up</a>(\*\*<a href="src/vitable_connect/types/auth_sign_up_params.py">params</a>) -> <a href="./src/vitable_connect/types/auth_sign_up_response.py">AuthSignUpResponse</a></code>

# Employees

Types:

```python
from vitable_connect.types import (
    Employee,
    EmployeeClass,
    Pagination,
    EmployeeRetrieveResponse,
    EmployeeUpdateResponse,
)
```

Methods:

- <code title="get /v1/employees/{employee_id}">client.employees.<a href="./src/vitable_connect/resources/employees.py">retrieve</a>(employee_id) -> <a href="./src/vitable_connect/types/employee_retrieve_response.py">EmployeeRetrieveResponse</a></code>
- <code title="patch /v1/employees/{employee_id}">client.employees.<a href="./src/vitable_connect/resources/employees.py">update</a>(employee_id, \*\*<a href="src/vitable_connect/types/employee_update_params.py">params</a>) -> <a href="./src/vitable_connect/types/employee_update_response.py">EmployeeUpdateResponse</a></code>
- <code title="get /v1/employees/{employee_id}/enrollments">client.employees.<a href="./src/vitable_connect/resources/employees.py">list_enrollments</a>(employee_id, \*\*<a href="src/vitable_connect/types/employee_list_enrollments_params.py">params</a>) -> <a href="./src/vitable_connect/types/enrollment.py">SyncPageNumberPage[Enrollment]</a></code>

# Employers

Types:

```python
from vitable_connect.types import (
    Employer,
    EmployerResponse,
    EmployerListResponse,
    EmployerEnsurePayrollIntegrationEmailResponse,
    EmployerListBenefitPlanYearEnrollmentsResponse,
    EmployerListBenefitPlanYearsResponse,
    EmployerListHRISProvidersResponse,
    EmployerListInvoicesResponse,
    EmployerListPayrollDeductionStatementsResponse,
    EmployerRetrieveBenefitPlanYearResponse,
    EmployerRetrieveHRISResponse,
    EmployerRetrieveInvoicePdfResponse,
    EmployerRetrievePayrollAccessSetupResponse,
    EmployerSubmitCensusSyncResponse,
    EmployerSubmitPayrollAccessSetupResponse,
    EmployerUpdateSettingsResponse,
)
```

Methods:

- <code title="post /v1/employers">client.employers.<a href="./src/vitable_connect/resources/employers.py">create</a>(\*\*<a href="src/vitable_connect/types/employer_create_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="get /v1/employers/{employer_id}">client.employers.<a href="./src/vitable_connect/resources/employers.py">retrieve</a>(employer_id) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="put /v1/employers/{employer_id}">client.employers.<a href="./src/vitable_connect/resources/employers.py">update</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_update_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="get /v1/employers">client.employers.<a href="./src/vitable_connect/resources/employers.py">list</a>(\*\*<a href="src/vitable_connect/types/employer_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_list_response.py">SyncPageNumberPage[EmployerListResponse]</a></code>
- <code title="put /v1/employers/{employer_id}/payroll-integration-email">client.employers.<a href="./src/vitable_connect/resources/employers.py">ensure_payroll_integration_email</a>(employer_id) -> <a href="./src/vitable_connect/types/employer_ensure_payroll_integration_email_response.py">EmployerEnsurePayrollIntegrationEmailResponse</a></code>
- <code title="get /v1/employers/{employer_id}/benefit-plan-years/{benefit_plan_year_id}/enrollments">client.employers.<a href="./src/vitable_connect/resources/employers.py">list_benefit_plan_year_enrollments</a>(benefit_plan_year_id, \*, employer_id, \*\*<a href="src/vitable_connect/types/employer_list_benefit_plan_year_enrollments_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_list_benefit_plan_year_enrollments_response.py">SyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse]</a></code>
- <code title="get /v1/employers/{employer_id}/benefit-plan-years">client.employers.<a href="./src/vitable_connect/resources/employers.py">list_benefit_plan_years</a>(employer_id) -> <a href="./src/vitable_connect/types/employer_list_benefit_plan_years_response.py">EmployerListBenefitPlanYearsResponse</a></code>
- <code title="get /v1/employers/{employer_id}/employees">client.employers.<a href="./src/vitable_connect/resources/employers.py">list_employees</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_list_employees_params.py">params</a>) -> <a href="./src/vitable_connect/types/employee.py">SyncPageNumberPage[Employee]</a></code>
- <code title="get /v1/employers/hris-providers">client.employers.<a href="./src/vitable_connect/resources/employers.py">list_hris_providers</a>() -> <a href="./src/vitable_connect/types/employer_list_hris_providers_response.py">EmployerListHRISProvidersResponse</a></code>
- <code title="get /v1/employers/{employer_id}/invoices">client.employers.<a href="./src/vitable_connect/resources/employers.py">list_invoices</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_list_invoices_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_list_invoices_response.py">EmployerListInvoicesResponse</a></code>
- <code title="get /v1/employers/{employer_id}/payroll-deduction-statements">client.employers.<a href="./src/vitable_connect/resources/employers.py">list_payroll_deduction_statements</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_list_payroll_deduction_statements_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_list_payroll_deduction_statements_response.py">SyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse]</a></code>
- <code title="get /v1/employers/{employer_id}/benefit-plan-years/{benefit_plan_year_id}">client.employers.<a href="./src/vitable_connect/resources/employers.py">retrieve_benefit_plan_year</a>(benefit_plan_year_id, \*, employer_id) -> <a href="./src/vitable_connect/types/employer_retrieve_benefit_plan_year_response.py">EmployerRetrieveBenefitPlanYearResponse</a></code>
- <code title="get /v1/employers/{employer_id}/hris">client.employers.<a href="./src/vitable_connect/resources/employers.py">retrieve_hris</a>(employer_id) -> <a href="./src/vitable_connect/types/employer_retrieve_hris_response.py">EmployerRetrieveHRISResponse</a></code>
- <code title="get /v1/employers/{employer_id}/invoices/{invoice_id}/pdf">client.employers.<a href="./src/vitable_connect/resources/employers.py">retrieve_invoice_pdf</a>(invoice_id, \*, employer_id) -> <a href="./src/vitable_connect/types/employer_retrieve_invoice_pdf_response.py">EmployerRetrieveInvoicePdfResponse</a></code>
- <code title="get /v1/employers/{employer_id}/payroll-access-setup">client.employers.<a href="./src/vitable_connect/resources/employers.py">retrieve_payroll_access_setup</a>(employer_id) -> <a href="./src/vitable_connect/types/employer_retrieve_payroll_access_setup_response.py">EmployerRetrievePayrollAccessSetupResponse</a></code>
- <code title="post /v1/employers/{employer_id}/census-sync">client.employers.<a href="./src/vitable_connect/resources/employers.py">submit_census_sync</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_submit_census_sync_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_submit_census_sync_response.py">EmployerSubmitCensusSyncResponse</a></code>
- <code title="put /v1/employers/{employer_id}/payroll-access-setup">client.employers.<a href="./src/vitable_connect/resources/employers.py">submit_payroll_access_setup</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_submit_payroll_access_setup_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_submit_payroll_access_setup_response.py">EmployerSubmitPayrollAccessSetupResponse</a></code>
- <code title="put /v1/employers/{employer_id}/settings">client.employers.<a href="./src/vitable_connect/resources/employers.py">update_settings</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_update_settings_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_update_settings_response.py">EmployerUpdateSettingsResponse</a></code>

# Enrollments

Types:

```python
from vitable_connect.types import (
    Enrollment,
    EnrollmentStatus,
    EnrollmentRetrieveResponse,
    EnrollmentReissueResponse,
)
```

Methods:

- <code title="get /v1/enrollments/{enrollment_id}">client.enrollments.<a href="./src/vitable_connect/resources/enrollments.py">retrieve</a>(enrollment_id) -> <a href="./src/vitable_connect/types/enrollment_retrieve_response.py">EnrollmentRetrieveResponse</a></code>
- <code title="post /v1/enrollments/{enrollment_id}/reissue">client.enrollments.<a href="./src/vitable_connect/resources/enrollments.py">reissue</a>(enrollment_id, \*\*<a href="src/vitable_connect/types/enrollment_reissue_params.py">params</a>) -> <a href="./src/vitable_connect/types/enrollment_reissue_response.py">EnrollmentReissueResponse</a></code>
- <code title="post /v1/enrollments/{enrollment_id}/terminate">client.enrollments.<a href="./src/vitable_connect/resources/enrollments.py">terminate</a>(enrollment_id, \*\*<a href="src/vitable_connect/types/enrollment_terminate_params.py">params</a>) -> None</code>

# WebhookEvents

Types:

```python
from vitable_connect.types import (
    WebhookEvent,
    WebhookEventRetrieveResponse,
    WebhookEventListDeliveriesResponse,
)
```

Methods:

- <code title="get /v1/webhook-events/{event_id}">client.webhook_events.<a href="./src/vitable_connect/resources/webhook_events.py">retrieve</a>(event_id) -> <a href="./src/vitable_connect/types/webhook_event_retrieve_response.py">WebhookEventRetrieveResponse</a></code>
- <code title="get /v1/webhook-events">client.webhook_events.<a href="./src/vitable_connect/resources/webhook_events.py">list</a>(\*\*<a href="src/vitable_connect/types/webhook_event_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/webhook_event.py">SyncPageNumberPage[WebhookEvent]</a></code>
- <code title="get /v1/webhook-events/{event_id}/deliveries">client.webhook_events.<a href="./src/vitable_connect/resources/webhook_events.py">list_deliveries</a>(event_id) -> <a href="./src/vitable_connect/types/webhook_event_list_deliveries_response.py">WebhookEventListDeliveriesResponse</a></code>

# Groups

Types:

```python
from vitable_connect.types import Group, GroupResponse
```

Methods:

- <code title="post /v1/groups">client.groups.<a href="./src/vitable_connect/resources/groups/groups.py">create</a>(\*\*<a href="src/vitable_connect/types/group_create_params.py">params</a>) -> <a href="./src/vitable_connect/types/group_response.py">GroupResponse</a></code>
- <code title="get /v1/groups/{group_id}">client.groups.<a href="./src/vitable_connect/resources/groups/groups.py">retrieve</a>(group_id) -> <a href="./src/vitable_connect/types/group_response.py">GroupResponse</a></code>
- <code title="patch /v1/groups/{group_id}">client.groups.<a href="./src/vitable_connect/resources/groups/groups.py">update</a>(group_id, \*\*<a href="src/vitable_connect/types/group_update_params.py">params</a>) -> <a href="./src/vitable_connect/types/group_response.py">GroupResponse</a></code>
- <code title="get /v1/groups">client.groups.<a href="./src/vitable_connect/resources/groups/groups.py">list</a>(\*\*<a href="src/vitable_connect/types/group_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/group.py">SyncPageNumberPage[Group]</a></code>

## Members

### Sync

Types:

```python
from vitable_connect.types.groups.members import SyncRetrieveResponse, SyncSubmitResponse
```

Methods:

- <code title="get /v1/groups/{group_id}/members/sync/{request_id}">client.groups.members.sync.<a href="./src/vitable_connect/resources/groups/members/sync.py">retrieve</a>(request_id, \*, group_id) -> <a href="./src/vitable_connect/types/groups/members/sync_retrieve_response.py">SyncRetrieveResponse</a></code>
- <code title="post /v1/groups/{group_id}/members/sync">client.groups.members.sync.<a href="./src/vitable_connect/resources/groups/members/sync.py">submit</a>(group_id, \*\*<a href="src/vitable_connect/types/groups/members/sync_submit_params.py">params</a>) -> <a href="./src/vitable_connect/types/groups/members/sync_submit_response.py">SyncSubmitResponse</a></code>

# Members

Types:

```python
from vitable_connect.types import (
    MemberRetrieveResponse,
    MemberListResponse,
    MemberListDependentsResponse,
    MemberListEmploymentsResponse,
    MemberListEnrollmentsResponse,
    MemberListIDCardsResponse,
    MemberListQualifyingLifeEventsResponse,
    MemberRetrieveHouseholdResponse,
)
```

Methods:

- <code title="get /v1/members/{member_id}">client.members.<a href="./src/vitable_connect/resources/members.py">retrieve</a>(member_id) -> <a href="./src/vitable_connect/types/member_retrieve_response.py">MemberRetrieveResponse</a></code>
- <code title="get /v2/members">client.members.<a href="./src/vitable_connect/resources/members.py">list</a>(\*\*<a href="src/vitable_connect/types/member_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/member_list_response.py">SyncPageNumberPage[MemberListResponse]</a></code>
- <code title="get /v1/members/{member_id}/dependents">client.members.<a href="./src/vitable_connect/resources/members.py">list_dependents</a>(member_id) -> <a href="./src/vitable_connect/types/member_list_dependents_response.py">MemberListDependentsResponse</a></code>
- <code title="get /v1/members/{member_id}/employments">client.members.<a href="./src/vitable_connect/resources/members.py">list_employments</a>(member_id) -> <a href="./src/vitable_connect/types/member_list_employments_response.py">MemberListEmploymentsResponse</a></code>
- <code title="get /v1/members/{member_id}/enrollments">client.members.<a href="./src/vitable_connect/resources/members.py">list_enrollments</a>(member_id) -> <a href="./src/vitable_connect/types/member_list_enrollments_response.py">MemberListEnrollmentsResponse</a></code>
- <code title="get /v1/members/{member_id}/id-cards">client.members.<a href="./src/vitable_connect/resources/members.py">list_id_cards</a>(member_id) -> <a href="./src/vitable_connect/types/member_list_id_cards_response.py">MemberListIDCardsResponse</a></code>
- <code title="get /v1/members/{member_id}/qualifying-life-events">client.members.<a href="./src/vitable_connect/resources/members.py">list_qualifying_life_events</a>(member_id, \*\*<a href="src/vitable_connect/types/member_list_qualifying_life_events_params.py">params</a>) -> <a href="./src/vitable_connect/types/member_list_qualifying_life_events_response.py">SyncPageNumberPage[MemberListQualifyingLifeEventsResponse]</a></code>
- <code title="get /v1/members/{member_id}/household">client.members.<a href="./src/vitable_connect/resources/members.py">retrieve_household</a>(member_id) -> <a href="./src/vitable_connect/types/member_retrieve_household_response.py">MemberRetrieveHouseholdResponse</a></code>

# Organizations

Types:

```python
from vitable_connect.types import OrganizationCreateResponse, OrganizationListResponse
```

Methods:

- <code title="post /v1/organizations">client.organizations.<a href="./src/vitable_connect/resources/organizations.py">create</a>(\*\*<a href="src/vitable_connect/types/organization_create_params.py">params</a>) -> <a href="./src/vitable_connect/types/organization_create_response.py">OrganizationCreateResponse</a></code>
- <code title="get /v1/organizations">client.organizations.<a href="./src/vitable_connect/resources/organizations.py">list</a>() -> <a href="./src/vitable_connect/types/organization_list_response.py">OrganizationListResponse</a></code>

# Plans

Types:

```python
from vitable_connect.types import PlanListResponse
```

Methods:

- <code title="get /v1/plans">client.plans.<a href="./src/vitable_connect/resources/plans.py">list</a>(\*\*<a href="src/vitable_connect/types/plan_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/plan_list_response.py">SyncPageNumberPage[PlanListResponse]</a></code>
