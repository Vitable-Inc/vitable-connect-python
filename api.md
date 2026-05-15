# Auth

Types:

```python
from vitable_connect.types import Type, AuthIssueAccessTokenResponse
```

Methods:

- <code title="post /v1/auth/access-tokens">client.auth.<a href="./src/vitable_connect/resources/auth.py">issue_access_token</a>(\*\*<a href="src/vitable_connect/types/auth_issue_access_token_params.py">params</a>) -> <a href="./src/vitable_connect/types/auth_issue_access_token_response.py">AuthIssueAccessTokenResponse</a></code>

# BenefitEligibilityPolicies

Types:

```python
from vitable_connect.types import BenefitEligibilityPolicy, BenefitEligibilityPolicyResponse
```

Methods:

- <code title="get /v1/benefit-eligibility-policies/{policy_id}">client.benefit_eligibility_policies.<a href="./src/vitable_connect/resources/benefit_eligibility_policies.py">retrieve</a>(policy_id) -> <a href="./src/vitable_connect/types/benefit_eligibility_policy_response.py">BenefitEligibilityPolicyResponse</a></code>

# Employees

Types:

```python
from vitable_connect.types import Employee, EmployeeClass, Pagination, EmployeeRetrieveResponse
```

Methods:

- <code title="get /v1/employees/{employee_id}">client.employees.<a href="./src/vitable_connect/resources/employees.py">retrieve</a>(employee_id) -> <a href="./src/vitable_connect/types/employee_retrieve_response.py">EmployeeRetrieveResponse</a></code>
- <code title="get /v1/employees/{employee_id}/enrollments">client.employees.<a href="./src/vitable_connect/resources/employees.py">list_enrollments</a>(employee_id, \*\*<a href="src/vitable_connect/types/employee_list_enrollments_params.py">params</a>) -> <a href="./src/vitable_connect/types/enrollment.py">SyncPageNumberPage[Enrollment]</a></code>

# Employers

Types:

```python
from vitable_connect.types import (
    Employer,
    EmployerResponse,
    EmployerSubmitCensusSyncResponse,
    EmployerUpdateSettingsResponse,
)
```

Methods:

- <code title="post /v1/employers">client.employers.<a href="./src/vitable_connect/resources/employers.py">create</a>(\*\*<a href="src/vitable_connect/types/employer_create_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="get /v1/employers/{employer_id}">client.employers.<a href="./src/vitable_connect/resources/employers.py">retrieve</a>(employer_id) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="get /v1/employers">client.employers.<a href="./src/vitable_connect/resources/employers.py">list</a>(\*\*<a href="src/vitable_connect/types/employer_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer.py">SyncPageNumberPage[Employer]</a></code>
- <code title="post /v1/employers/{employer_id}/benefit-eligibility-policies">client.employers.<a href="./src/vitable_connect/resources/employers.py">create_benefit_eligibility_policy</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_create_benefit_eligibility_policy_params.py">params</a>) -> <a href="./src/vitable_connect/types/benefit_eligibility_policy_response.py">BenefitEligibilityPolicyResponse</a></code>
- <code title="get /v1/employers/{employer_id}/employees">client.employers.<a href="./src/vitable_connect/resources/employers.py">list_employees</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_list_employees_params.py">params</a>) -> <a href="./src/vitable_connect/types/employee.py">SyncPageNumberPage[Employee]</a></code>
- <code title="post /v1/employers/{employer_id}/census-sync">client.employers.<a href="./src/vitable_connect/resources/employers.py">submit_census_sync</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_submit_census_sync_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_submit_census_sync_response.py">EmployerSubmitCensusSyncResponse</a></code>
- <code title="put /v1/employers/{employer_id}/settings">client.employers.<a href="./src/vitable_connect/resources/employers.py">update_settings</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_update_settings_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_update_settings_response.py">EmployerUpdateSettingsResponse</a></code>

# Enrollments

Types:

```python
from vitable_connect.types import Enrollment, EnrollmentStatus, EnrollmentRetrieveResponse
```

Methods:

- <code title="get /v1/enrollments/{enrollment_id}">client.enrollments.<a href="./src/vitable_connect/resources/enrollments.py">retrieve</a>(enrollment_id) -> <a href="./src/vitable_connect/types/enrollment_retrieve_response.py">EnrollmentRetrieveResponse</a></code>

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

# Plans

Types:

```python
from vitable_connect.types import PlanListResponse
```

Methods:

- <code title="get /v1/plans">client.plans.<a href="./src/vitable_connect/resources/plans.py">list</a>(\*\*<a href="src/vitable_connect/types/plan_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/plan_list_response.py">SyncPageNumberPage[PlanListResponse]</a></code>
