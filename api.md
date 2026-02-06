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
from vitable_connect.types import Category, Pagination, ProductCode, BenefitProductListResponse
```

Methods:

- <code title="get /v1/benefit-products">client.benefit_products.<a href="./src/vitable_connect/resources/benefit_products/benefit_products.py">list</a>(\*\*<a href="src/vitable_connect/types/benefit_product_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/benefit_product_list_response.py">BenefitProductListResponse</a></code>

## PlanYears

Types:

```python
from vitable_connect.types.benefit_products import (
    PlanYear,
    PlanYearResponse,
    PlanYearStatus,
    PlanYearListResponse,
)
```

Methods:

- <code title="post /v1/benefit-products/{benefit_product_id}/plan-years">client.benefit_products.plan_years.<a href="./src/vitable_connect/resources/benefit_products/plan_years.py">create</a>(benefit_product_id, \*\*<a href="src/vitable_connect/types/benefit_products/plan_year_create_params.py">params</a>) -> <a href="./src/vitable_connect/types/benefit_products/plan_year_response.py">PlanYearResponse</a></code>
- <code title="get /v1/benefit-products/{benefit_product_id}/plan-years">client.benefit_products.plan_years.<a href="./src/vitable_connect/resources/benefit_products/plan_years.py">list</a>(benefit_product_id, \*\*<a href="src/vitable_connect/types/benefit_products/plan_year_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/benefit_products/plan_year_list_response.py">PlanYearListResponse</a></code>

# Dependents

Types:

```python
from vitable_connect.types import Dependent, DependentResponse
```

Methods:

- <code title="get /v1/dependents/{dependent_id}">client.dependents.<a href="./src/vitable_connect/resources/dependents.py">retrieve</a>(dependent_id) -> <a href="./src/vitable_connect/types/dependent_response.py">DependentResponse</a></code>
- <code title="put /v1/dependents/{dependent_id}">client.dependents.<a href="./src/vitable_connect/resources/dependents.py">update</a>(dependent_id, \*\*<a href="src/vitable_connect/types/dependent_update_params.py">params</a>) -> <a href="./src/vitable_connect/types/dependent_response.py">DependentResponse</a></code>

# Employees

Types:

```python
from vitable_connect.types import Employee, EmployeeResponse
```

Methods:

- <code title="get /v1/employees/{employee_id}">client.employees.<a href="./src/vitable_connect/resources/employees/employees.py">retrieve</a>(employee_id) -> <a href="./src/vitable_connect/types/employee_response.py">EmployeeResponse</a></code>
- <code title="put /v1/employees/{employee_id}">client.employees.<a href="./src/vitable_connect/resources/employees/employees.py">update</a>(employee_id, \*\*<a href="src/vitable_connect/types/employee_update_params.py">params</a>) -> <a href="./src/vitable_connect/types/employee_response.py">EmployeeResponse</a></code>
- <code title="delete /v1/employees/{employee_id}">client.employees.<a href="./src/vitable_connect/resources/employees/employees.py">terminate</a>(employee_id) -> None</code>

## Enrollments

Types:

```python
from vitable_connect.types.employees import EnrollmentList, EnrollmentStatus
```

Methods:

- <code title="get /v1/employees/{employee_id}/enrollments">client.employees.enrollments.<a href="./src/vitable_connect/resources/employees/enrollments.py">list</a>(employee_id, \*\*<a href="src/vitable_connect/types/employees/enrollment_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/employees/enrollment_list.py">EnrollmentList</a></code>
- <code title="post /v1/employees/{employee_id}/enrollments/elect">client.employees.enrollments.<a href="./src/vitable_connect/resources/employees/enrollments.py">submit_elections</a>(employee_id, \*\*<a href="src/vitable_connect/types/employees/enrollment_submit_elections_params.py">params</a>) -> <a href="./src/vitable_connect/types/employees/enrollment_list.py">EnrollmentList</a></code>

# Employers

Types:

```python
from vitable_connect.types import Employer, EmployerResponse, EmployerListResponse
```

Methods:

- <code title="post /v1/employers">client.employers.<a href="./src/vitable_connect/resources/employers/employers.py">create</a>(\*\*<a href="src/vitable_connect/types/employer_create_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="get /v1/employers/{employer_id}">client.employers.<a href="./src/vitable_connect/resources/employers/employers.py">retrieve</a>(employer_id) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="put /v1/employers/{employer_id}">client.employers.<a href="./src/vitable_connect/resources/employers/employers.py">update</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_update_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_response.py">EmployerResponse</a></code>
- <code title="get /v1/employers">client.employers.<a href="./src/vitable_connect/resources/employers/employers.py">list</a>(\*\*<a href="src/vitable_connect/types/employer_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/employer_list_response.py">EmployerListResponse</a></code>
- <code title="post /v1/employers/{employer_id}/benefit-eligibility-policies">client.employers.<a href="./src/vitable_connect/resources/employers/employers.py">create_eligibility_policy</a>(employer_id, \*\*<a href="src/vitable_connect/types/employer_create_eligibility_policy_params.py">params</a>) -> <a href="./src/vitable_connect/types/benefit_eligibility_policy.py">BenefitEligibilityPolicy</a></code>

## Employees

Types:

```python
from vitable_connect.types.employers import EmployeeClass, Sex, EmployeeListResponse
```

Methods:

- <code title="post /v1/employers/{employer_id}/employees">client.employers.employees.<a href="./src/vitable_connect/resources/employers/employees.py">create</a>(employer_id, \*\*<a href="src/vitable_connect/types/employers/employee_create_params.py">params</a>) -> <a href="./src/vitable_connect/types/employee_response.py">EmployeeResponse</a></code>
- <code title="get /v1/employers/{employer_id}/employees">client.employers.employees.<a href="./src/vitable_connect/resources/employers/employees.py">list</a>(employer_id, \*\*<a href="src/vitable_connect/types/employers/employee_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/employers/employee_list_response.py">EmployeeListResponse</a></code>

# Enrollments

Types:

```python
from vitable_connect.types import (
    CoverageTier,
    Enrollment,
    EnrollmentResponse,
    PlanTier,
    EnrollmentListPlansResponse,
)
```

Methods:

- <code title="get /v1/enrollments/{enrollment_id}">client.enrollments.<a href="./src/vitable_connect/resources/enrollments.py">retrieve</a>(enrollment_id) -> <a href="./src/vitable_connect/types/enrollment_response.py">EnrollmentResponse</a></code>
- <code title="get /v1/enrollments/{enrollment_id}/plans">client.enrollments.<a href="./src/vitable_connect/resources/enrollments.py">list_plans</a>(enrollment_id) -> <a href="./src/vitable_connect/types/enrollment_list_plans_response.py">EnrollmentListPlansResponse</a></code>
- <code title="post /v1/enrollments/{enrollment_id}/reissue">client.enrollments.<a href="./src/vitable_connect/resources/enrollments.py">reissue</a>(enrollment_id, \*\*<a href="src/vitable_connect/types/enrollment_reissue_params.py">params</a>) -> <a href="./src/vitable_connect/types/enrollment_response.py">EnrollmentResponse</a></code>

# Members

## Dependents

Types:

```python
from vitable_connect.types.members import Relationship, DependentListResponse
```

Methods:

- <code title="post /v1/members/{member_id}/dependents">client.members.dependents.<a href="./src/vitable_connect/resources/members/dependents.py">create</a>(member_id, \*\*<a href="src/vitable_connect/types/members/dependent_create_params.py">params</a>) -> <a href="./src/vitable_connect/types/dependent_response.py">DependentResponse</a></code>
- <code title="get /v1/members/{member_id}/dependents">client.members.dependents.<a href="./src/vitable_connect/resources/members/dependents.py">list</a>(member_id, \*\*<a href="src/vitable_connect/types/members/dependent_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/members/dependent_list_response.py">DependentListResponse</a></code>

## QualifyingLifeEvents

Types:

```python
from vitable_connect.types.members import (
    EventType,
    QualifyingLifeEvent,
    QualifyingLifeEventResponse,
    QualifyingLifeEventStatus,
    QualifyingLifeEventListResponse,
)
```

Methods:

- <code title="get /v1/members/{member_id}/qualifying-life-events/{qle_id}">client.members.qualifying_life_events.<a href="./src/vitable_connect/resources/members/qualifying_life_events.py">retrieve</a>(qle_id, \*, member_id) -> <a href="./src/vitable_connect/types/members/qualifying_life_event_response.py">QualifyingLifeEventResponse</a></code>
- <code title="get /v1/members/{member_id}/qualifying-life-events">client.members.qualifying_life_events.<a href="./src/vitable_connect/resources/members/qualifying_life_events.py">list</a>(member_id, \*\*<a href="src/vitable_connect/types/members/qualifying_life_event_list_params.py">params</a>) -> <a href="./src/vitable_connect/types/members/qualifying_life_event_list_response.py">QualifyingLifeEventListResponse</a></code>
- <code title="post /v1/members/{member_id}/qualifying-life-events">client.members.qualifying_life_events.<a href="./src/vitable_connect/resources/members/qualifying_life_events.py">record</a>(member_id, \*\*<a href="src/vitable_connect/types/members/qualifying_life_event_record_params.py">params</a>) -> <a href="./src/vitable_connect/types/members/qualifying_life_event_response.py">QualifyingLifeEventResponse</a></code>

# PlanYears

Methods:

- <code title="get /v1/plan-years/{plan_year_id}">client.plan_years.<a href="./src/vitable_connect/resources/plan_years.py">retrieve</a>(plan_year_id) -> <a href="./src/vitable_connect/types/benefit_products/plan_year_response.py">PlanYearResponse</a></code>
- <code title="put /v1/plan-years/{plan_year_id}">client.plan_years.<a href="./src/vitable_connect/resources/plan_years.py">update</a>(plan_year_id, \*\*<a href="src/vitable_connect/types/plan_year_update_params.py">params</a>) -> <a href="./src/vitable_connect/types/benefit_products/plan_year_response.py">PlanYearResponse</a></code>
