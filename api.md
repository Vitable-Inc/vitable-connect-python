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
from vitable_connect.types import BenefitEligibilityPolicy
```

Methods:

- <code title="get /v1/benefit-eligibility-policies/{policy_id}">client.benefit_eligibility_policies.<a href="./src/vitable_connect/resources/benefit_eligibility_policies.py">retrieve</a>(policy_id) -> <a href="./src/vitable_connect/types/benefit_eligibility_policy.py">BenefitEligibilityPolicy</a></code>

# BenefitProducts

Types:

```python
from vitable_connect.types import Category, Pagination, ProductCode
```

# Employees

Types:

```python
from vitable_connect.types import Employee, EmployeeClass, EmployeeResponse
```

Methods:

- <code title="get /v1/employees/{employee_id}">client.employees.<a href="./src/vitable_connect/resources/employees/employees.py">retrieve</a>(employee_id) -> <a href="./src/vitable_connect/types/employee_response.py">EmployeeResponse</a></code>

## Enrollments

Types:

```python
from vitable_connect.types.employees import EnrollmentList
```

Methods:

- <code title="get /v1/employees/{employee_id}/enrollments">client.employees.enrollments.<a href="./src/vitable_connect/resources/employees/enrollments.py">list</a>(employee_id, \*\*<a href="src/vitable_connect/types/employees/enrollment_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/employees/enrollment_list.py">EnrollmentList</a></code>

# Employers

Types:

```python
from vitable_connect.types import Employer, EmployerResponse, EmployerListResponse
```

Methods:

- <code title="post /v1/employers">client.employers.<a href="./src/vitable_connect/resources/employers/employers.py">create</a>(\*\*<a href="src/vitable_connect/types/employer_create_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="get /v1/employers/{employer_id}">client.employers.<a href="./src/vitable_connect/resources/employers/employers.py">retrieve</a>(employer_id) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="get /v1/employers">client.employers.<a href="./src/vitable_connect/resources/employers/employers.py">list</a>(\*\*<a href="src/vitable_connect/types/employer_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_list_response.py">EmployerListResponse</a></code>
- <code title="post /v1/employers/{employer_id}/benefit-eligibility-policies">client.employers.<a href="./src/vitable_connect/resources/employers/employers.py">create_eligibility_policy</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_create_eligibility_policy_params.py">params</a>) -> <a href="./src/vitable_connect/types/benefit_eligibility_policy.py">BenefitEligibilityPolicy</a></code>

## Employees

Types:

```python
from vitable_connect.types.employers import EmployeeListResponse
```

Methods:

- <code title="get /v1/employers/{employer_id}/employees">client.employers.employees.<a href="./src/vitable_connect/resources/employers/employees.py">list</a>(employer_id, \*\*<a href="src/vitable_connect/types/employers/employee_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/employers/employee_list_response.py">EmployeeListResponse</a></code>

# Enrollments

Types:

```python
from vitable_connect.types import Enrollment, EnrollmentResponse, EnrollmentStatus
```

Methods:

- <code title="get /v1/enrollments/{enrollment_id}">client.enrollments.<a href="./src/vitable_connect/resources/enrollments.py">retrieve</a>(enrollment_id) -> <a href="./src/vitable_connect/types/enrollment_response.py">EnrollmentResponse</a></code>
