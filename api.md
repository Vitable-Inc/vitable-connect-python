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
from vitable_connect.types import Employer, EmployerResponse, EmployerSubmitCensusSyncResponse
```

Methods:

- <code title="post /v1/employers">client.employers.<a href="./src/vitable_connect/resources/employers.py">create</a>(\*\*<a href="src/vitable_connect/types/employer_create_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="get /v1/employers/{employer_id}">client.employers.<a href="./src/vitable_connect/resources/employers.py">retrieve</a>(employer_id) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="get /v1/employers">client.employers.<a href="./src/vitable_connect/resources/employers.py">list</a>(\*\*<a href="src/vitable_connect/types/employer_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer.py">SyncPageNumberPage[Employer]</a></code>
- <code title="post /v1/employers/{employer_id}/benefit-eligibility-policies">client.employers.<a href="./src/vitable_connect/resources/employers.py">create_benefit_eligibility_policy</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_create_benefit_eligibility_policy_params.py">params</a>) -> <a href="./src/vitable_connect/types/benefit_eligibility_policy_response.py">BenefitEligibilityPolicyResponse</a></code>
- <code title="get /v1/employers/{employer_id}/employees">client.employers.<a href="./src/vitable_connect/resources/employers.py">list_employees</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_list_employees_params.py">params</a>) -> <a href="./src/vitable_connect/types/employee.py">SyncPageNumberPage[Employee]</a></code>
- <code title="post /v1/employers/{employer_id}/census-sync">client.employers.<a href="./src/vitable_connect/resources/employers.py">submit_census_sync</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_submit_census_sync_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_submit_census_sync_response.py">EmployerSubmitCensusSyncResponse</a></code>

# Enrollments

Types:

```python
from vitable_connect.types import Enrollment, EnrollmentStatus, EnrollmentRetrieveResponse
```

Methods:

- <code title="get /v1/enrollments/{enrollment_id}">client.enrollments.<a href="./src/vitable_connect/resources/enrollments.py">retrieve</a>(enrollment_id) -> <a href="./src/vitable_connect/types/enrollment_retrieve_response.py">EnrollmentRetrieveResponse</a></code>
