# BenefitEligibilityPolicy

Types:

```python
from vitable_connect_api.types import BenefitEligibilityPolicy
```

# BenefitProducts

Types:

```python
from vitable_connect_api.types import Category, ProductCode, BenefitProductListResponse
```

Methods:

- <code title="get /v1/benefit-products">client.benefit_products.<a href="./src/vitable_connect_api/resources/benefit_products/benefit_products.py">list</a>(\*\*<a href="src/vitable_connect_api/types/benefit_product_list_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/benefit_product_list_response.py">BenefitProductListResponse</a></code>

## PlanYears

Types:

```python
from vitable_connect_api.types.benefit_products import (
    PlanYear,
    PlanYearStatus,
    PlanYearCreateResponse,
    PlanYearListResponse,
)
```

Methods:

- <code title="post /v1/benefit-products/{benefit_product_id}/plan-years">client.benefit_products.plan_years.<a href="./src/vitable_connect_api/resources/benefit_products/plan_years.py">create</a>(benefit_product_id, \*\*<a href="src/vitable_connect_api/types/benefit_products/plan_year_create_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/benefit_products/plan_year_create_response.py">PlanYearCreateResponse</a></code>
- <code title="get /v1/benefit-products/{benefit_product_id}/plan-years">client.benefit_products.plan_years.<a href="./src/vitable_connect_api/resources/benefit_products/plan_years.py">list</a>(benefit_product_id, \*\*<a href="src/vitable_connect_api/types/benefit_products/plan_year_list_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/benefit_products/plan_year_list_response.py">PlanYearListResponse</a></code>

# Dependents

Types:

```python
from vitable_connect_api.types import (
    Dependent,
    Sex,
    DependentRetrieveResponse,
    DependentUpdateResponse,
)
```

Methods:

- <code title="get /v1/dependents/{dependent_id}">client.dependents.<a href="./src/vitable_connect_api/resources/dependents.py">retrieve</a>(dependent_id) -> <a href="./src/vitable_connect_api/types/dependent_retrieve_response.py">DependentRetrieveResponse</a></code>
- <code title="put /v1/dependents/{dependent_id}">client.dependents.<a href="./src/vitable_connect_api/resources/dependents.py">update</a>(dependent_id, \*\*<a href="src/vitable_connect_api/types/dependent_update_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/dependent_update_response.py">DependentUpdateResponse</a></code>

# Employees

Types:

```python
from vitable_connect_api.types import Employee, EmployeeRetrieveResponse, EmployeeUpdateResponse
```

Methods:

- <code title="get /v1/employees/{employee_id}">client.employees.<a href="./src/vitable_connect_api/resources/employees/employees.py">retrieve</a>(employee_id) -> <a href="./src/vitable_connect_api/types/employee_retrieve_response.py">EmployeeRetrieveResponse</a></code>
- <code title="put /v1/employees/{employee_id}">client.employees.<a href="./src/vitable_connect_api/resources/employees/employees.py">update</a>(employee_id, \*\*<a href="src/vitable_connect_api/types/employee_update_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/employee_update_response.py">EmployeeUpdateResponse</a></code>
- <code title="delete /v1/employees/{employee_id}">client.employees.<a href="./src/vitable_connect_api/resources/employees/employees.py">terminate</a>(employee_id) -> None</code>

## Enrollments

Types:

```python
from vitable_connect_api.types.employees import (
    EnrollmentStatus,
    EnrollmentListResponse,
    EnrollmentSubmitElectionsResponse,
)
```

Methods:

- <code title="get /v1/employees/{employee_id}/enrollments">client.employees.enrollments.<a href="./src/vitable_connect_api/resources/employees/enrollments.py">list</a>(employee_id, \*\*<a href="src/vitable_connect_api/types/employees/enrollment_list_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/employees/enrollment_list_response.py">EnrollmentListResponse</a></code>
- <code title="post /v1/employees/{employee_id}/enrollments/elect">client.employees.enrollments.<a href="./src/vitable_connect_api/resources/employees/enrollments.py">submit_elections</a>(employee_id, \*\*<a href="src/vitable_connect_api/types/employees/enrollment_submit_elections_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/employees/enrollment_submit_elections_response.py">EnrollmentSubmitElectionsResponse</a></code>

# Employers

Types:

```python
from vitable_connect_api.types import (
    Employer,
    EmployerCreateResponse,
    EmployerRetrieveResponse,
    EmployerUpdateResponse,
    EmployerListResponse,
)
```

Methods:

- <code title="post /v1/employers">client.employers.<a href="./src/vitable_connect_api/resources/employers/employers.py">create</a>(\*\*<a href="src/vitable_connect_api/types/employer_create_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/employer_create_response.py">EmployerCreateResponse</a></code>
- <code title="get /v1/employers/{employer_id}">client.employers.<a href="./src/vitable_connect_api/resources/employers/employers.py">retrieve</a>(employer_id) -> <a href="./src/vitable_connect_api/types/employer_retrieve_response.py">EmployerRetrieveResponse</a></code>
- <code title="put /v1/employers/{employer_id}">client.employers.<a href="./src/vitable_connect_api/resources/employers/employers.py">update</a>(employer_id, \*\*<a href="src/vitable_connect_api/types/employer_update_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/employer_update_response.py">EmployerUpdateResponse</a></code>
- <code title="get /v1/employers">client.employers.<a href="./src/vitable_connect_api/resources/employers/employers.py">list</a>(\*\*<a href="src/vitable_connect_api/types/employer_list_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/employer_list_response.py">EmployerListResponse</a></code>

## Employees

Types:

```python
from vitable_connect_api.types.employers import (
    EmployeeClass,
    EmployeeCreateResponse,
    EmployeeListResponse,
)
```

Methods:

- <code title="post /v1/employers/{employer_id}/employees">client.employers.employees.<a href="./src/vitable_connect_api/resources/employers/employees.py">create</a>(employer_id, \*\*<a href="src/vitable_connect_api/types/employers/employee_create_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/employers/employee_create_response.py">EmployeeCreateResponse</a></code>
- <code title="get /v1/employers/{employer_id}/employees">client.employers.employees.<a href="./src/vitable_connect_api/resources/employers/employees.py">list</a>(employer_id, \*\*<a href="src/vitable_connect_api/types/employers/employee_list_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/employers/employee_list_response.py">EmployeeListResponse</a></code>

# Enrollments

Types:

```python
from vitable_connect_api.types import (
    CoverageTier,
    Enrollment,
    PlanTier,
    EnrollmentRetrieveResponse,
    EnrollmentListPlansResponse,
    EnrollmentReissueResponse,
)
```

Methods:

- <code title="get /v1/enrollments/{enrollment_id}">client.enrollments.<a href="./src/vitable_connect_api/resources/enrollments.py">retrieve</a>(enrollment_id) -> <a href="./src/vitable_connect_api/types/enrollment_retrieve_response.py">EnrollmentRetrieveResponse</a></code>
- <code title="get /v1/enrollments/{enrollment_id}/plans">client.enrollments.<a href="./src/vitable_connect_api/resources/enrollments.py">list_plans</a>(enrollment_id) -> <a href="./src/vitable_connect_api/types/enrollment_list_plans_response.py">EnrollmentListPlansResponse</a></code>
- <code title="post /v1/enrollments/{enrollment_id}/reissue">client.enrollments.<a href="./src/vitable_connect_api/resources/enrollments.py">reissue</a>(enrollment_id, \*\*<a href="src/vitable_connect_api/types/enrollment_reissue_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/enrollment_reissue_response.py">EnrollmentReissueResponse</a></code>

# Members

## Dependents

Types:

```python
from vitable_connect_api.types.members import (
    Relationship,
    DependentCreateResponse,
    DependentListResponse,
)
```

Methods:

- <code title="post /v1/members/{member_id}/dependents">client.members.dependents.<a href="./src/vitable_connect_api/resources/members/dependents.py">create</a>(member_id, \*\*<a href="src/vitable_connect_api/types/members/dependent_create_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/members/dependent_create_response.py">DependentCreateResponse</a></code>
- <code title="get /v1/members/{member_id}/dependents">client.members.dependents.<a href="./src/vitable_connect_api/resources/members/dependents.py">list</a>(member_id, \*\*<a href="src/vitable_connect_api/types/members/dependent_list_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/members/dependent_list_response.py">DependentListResponse</a></code>

## QualifyingLifeEvents

Types:

```python
from vitable_connect_api.types.members import (
    EventType,
    QualifyingLifeEvent,
    QualifyingLifeEventStatus,
    QualifyingLifeEventListResponse,
    QualifyingLifeEventRecordResponse,
)
```

Methods:

- <code title="get /v1/members/{member_id}/qualifying-life-events">client.members.qualifying_life_events.<a href="./src/vitable_connect_api/resources/members/qualifying_life_events.py">list</a>(member_id, \*\*<a href="src/vitable_connect_api/types/members/qualifying_life_event_list_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/members/qualifying_life_event_list_response.py">QualifyingLifeEventListResponse</a></code>
- <code title="post /v1/members/{member_id}/qualifying-life-events">client.members.qualifying_life_events.<a href="./src/vitable_connect_api/resources/members/qualifying_life_events.py">record</a>(member_id, \*\*<a href="src/vitable_connect_api/types/members/qualifying_life_event_record_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/members/qualifying_life_event_record_response.py">QualifyingLifeEventRecordResponse</a></code>

# PlanYears

Types:

```python
from vitable_connect_api.types import PlanYearRetrieveResponse, PlanYearUpdateResponse
```

Methods:

- <code title="get /v1/plan-years/{plan_year_id}">client.plan_years.<a href="./src/vitable_connect_api/resources/plan_years.py">retrieve</a>(plan_year_id) -> <a href="./src/vitable_connect_api/types/plan_year_retrieve_response.py">PlanYearRetrieveResponse</a></code>
- <code title="put /v1/plan-years/{plan_year_id}">client.plan_years.<a href="./src/vitable_connect_api/resources/plan_years.py">update</a>(plan_year_id, \*\*<a href="src/vitable_connect_api/types/plan_year_update_params.py">params</a>) -> <a href="./src/vitable_connect_api/types/plan_year_update_response.py">PlanYearUpdateResponse</a></code>
