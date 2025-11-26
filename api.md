# Employers

Types:

```python
from vitable_partner_api.types import (
    CreateEligibilityPolicyRequest,
    CreateEmployerRequest,
    EligibilityPolicy,
    Employer,
    UpdateEmployerRequest,
    EmployerListResponse,
)
```

Methods:

- <code title="post /employers">client.employers.<a href="./src/vitable_partner_api/resources/employers/employers.py">create</a>(\*\*<a href="src/vitable_partner_api/types/employer_create_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/employer.py">Employer</a></code>
- <code title="get /employers/{id}">client.employers.<a href="./src/vitable_partner_api/resources/employers/employers.py">retrieve</a>(id) -> <a href="./src/vitable_partner_api/types/employer.py">Employer</a></code>
- <code title="put /employers/{id}">client.employers.<a href="./src/vitable_partner_api/resources/employers/employers.py">update</a>(id, \*\*<a href="src/vitable_partner_api/types/employer_update_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/employer.py">Employer</a></code>
- <code title="get /employers">client.employers.<a href="./src/vitable_partner_api/resources/employers/employers.py">list</a>(\*\*<a href="src/vitable_partner_api/types/employer_list_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/employer_list_response.py">EmployerListResponse</a></code>
- <code title="post /employers/{id}/benefit-eligibility-policy">client.employers.<a href="./src/vitable_partner_api/resources/employers/employers.py">create_eligibility_policy</a>(id, \*\*<a href="src/vitable_partner_api/types/employer_create_eligibility_policy_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/eligibility_policy.py">EligibilityPolicy</a></code>

## Employees

Types:

```python
from vitable_partner_api.types.employers import (
    CreateEmployeeRequest,
    UpdateEmployeeRequest,
    EmployeeListResponse,
)
```

Methods:

- <code title="post /employers/{id}/employees">client.employers.employees.<a href="./src/vitable_partner_api/resources/employers/employees.py">create</a>(id, \*\*<a href="src/vitable_partner_api/types/employers/employee_create_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/employee.py">Employee</a></code>
- <code title="get /employers/{id}/employees">client.employers.employees.<a href="./src/vitable_partner_api/resources/employers/employees.py">list</a>(id, \*\*<a href="src/vitable_partner_api/types/employers/employee_list_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/employers/employee_list_response.py">EmployeeListResponse</a></code>

# Employees

Types:

```python
from vitable_partner_api.types import (
    CreateQualifyingLifeEventRequest,
    ElectBenefitsRequest,
    Employee,
    Member,
    QualifyingLifeEvent,
)
```

Methods:

- <code title="get /employees/{id}">client.employees.<a href="./src/vitable_partner_api/resources/employees/employees.py">retrieve</a>(id) -> <a href="./src/vitable_partner_api/types/employee.py">Employee</a></code>
- <code title="put /employees/{id}">client.employees.<a href="./src/vitable_partner_api/resources/employees/employees.py">update</a>(id, \*\*<a href="src/vitable_partner_api/types/employee_update_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/employee.py">Employee</a></code>
- <code title="delete /employees/{id}">client.employees.<a href="./src/vitable_partner_api/resources/employees/employees.py">terminate</a>(id) -> None</code>

## Dependents

Types:

```python
from vitable_partner_api.types.employees import DependentListResponse
```

Methods:

- <code title="post /employees/{id}/dependents">client.employees.dependents.<a href="./src/vitable_partner_api/resources/employees/dependents.py">create</a>(id, \*\*<a href="src/vitable_partner_api/types/employees/dependent_create_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/dependent.py">Dependent</a></code>
- <code title="get /employees/{id}/dependents">client.employees.dependents.<a href="./src/vitable_partner_api/resources/employees/dependents.py">list</a>(id) -> <a href="./src/vitable_partner_api/types/employees/dependent_list_response.py">DependentListResponse</a></code>

## QualifyingLifeEvents

Types:

```python
from vitable_partner_api.types.employees import QualifyingLifeEventListResponse
```

Methods:

- <code title="post /employees/{id}/qualifying-life-events">client.employees.qualifying_life_events.<a href="./src/vitable_partner_api/resources/employees/qualifying_life_events.py">create</a>(id, \*\*<a href="src/vitable_partner_api/types/employees/qualifying_life_event_create_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/qualifying_life_event.py">QualifyingLifeEvent</a></code>
- <code title="get /employees/{id}/qualifying-life-events">client.employees.qualifying_life_events.<a href="./src/vitable_partner_api/resources/employees/qualifying_life_events.py">list</a>(id) -> <a href="./src/vitable_partner_api/types/employees/qualifying_life_event_list_response.py">QualifyingLifeEventListResponse</a></code>

## Enrollments

Types:

```python
from vitable_partner_api.types.employees import EnrollmentListResponse, EnrollmentElectResponse
```

Methods:

- <code title="get /employees/{id}/enrollments">client.employees.enrollments.<a href="./src/vitable_partner_api/resources/employees/enrollments.py">list</a>(id, \*\*<a href="src/vitable_partner_api/types/employees/enrollment_list_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/employees/enrollment_list_response.py">EnrollmentListResponse</a></code>
- <code title="post /employees/{id}/enrollments/elect">client.employees.enrollments.<a href="./src/vitable_partner_api/resources/employees/enrollments.py">elect</a>(id, \*\*<a href="src/vitable_partner_api/types/employees/enrollment_elect_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/employees/enrollment_elect_response.py">EnrollmentElectResponse</a></code>

# Dependents

Types:

```python
from vitable_partner_api.types import CreateDependentRequest, Dependent, UpdateDependentRequest
```

Methods:

- <code title="put /dependents/{id}">client.dependents.<a href="./src/vitable_partner_api/resources/dependents.py">update</a>(id, \*\*<a href="src/vitable_partner_api/types/dependent_update_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/dependent.py">Dependent</a></code>

# BenefitProducts

Types:

```python
from vitable_partner_api.types import (
    BenefitProduct,
    Plan,
    Quote,
    QuoteRequest,
    BenefitProductListResponse,
)
```

Methods:

- <code title="get /benefit-products">client.benefit_products.<a href="./src/vitable_partner_api/resources/benefit_products/benefit_products.py">list</a>(\*\*<a href="src/vitable_partner_api/types/benefit_product_list_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/benefit_product_list_response.py">BenefitProductListResponse</a></code>
- <code title="post /benefit-products/{id}/quote">client.benefit_products.<a href="./src/vitable_partner_api/resources/benefit_products/benefit_products.py">generate_quote</a>(id, \*\*<a href="src/vitable_partner_api/types/benefit_product_generate_quote_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/quote.py">Quote</a></code>

## PlanYears

Types:

```python
from vitable_partner_api.types.benefit_products import (
    CreatePlanYearRequest,
    PlanContributionClass,
    PlanCost,
    PlanYearListResponse,
)
```

Methods:

- <code title="post /benefit-products/{id}/plan-years">client.benefit_products.plan_years.<a href="./src/vitable_partner_api/resources/benefit_products/plan_years.py">create</a>(id, \*\*<a href="src/vitable_partner_api/types/benefit_products/plan_year_create_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/plan_year.py">PlanYear</a></code>
- <code title="get /benefit-products/{id}/plan-years">client.benefit_products.plan_years.<a href="./src/vitable_partner_api/resources/benefit_products/plan_years.py">list</a>(id, \*\*<a href="src/vitable_partner_api/types/benefit_products/plan_year_list_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/benefit_products/plan_year_list_response.py">PlanYearListResponse</a></code>

# PlanYears

Types:

```python
from vitable_partner_api.types import PlanYear, UpdatePlanYearRequest
```

Methods:

- <code title="put /plan-years/{id}">client.plan_years.<a href="./src/vitable_partner_api/resources/plan_years.py">update</a>(id, \*\*<a href="src/vitable_partner_api/types/plan_year_update_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/plan_year.py">PlanYear</a></code>

# Enrollments

Types:

```python
from vitable_partner_api.types import (
    Enrollment,
    ReissueEnrollmentRequest,
    EnrollmentGetEligiblePlansResponse,
)
```

Methods:

- <code title="get /enrollments/{id}/plans">client.enrollments.<a href="./src/vitable_partner_api/resources/enrollments.py">get_eligible_plans</a>(id) -> <a href="./src/vitable_partner_api/types/enrollment_get_eligible_plans_response.py">EnrollmentGetEligiblePlansResponse</a></code>
- <code title="post /enrollments/{id}/reissue">client.enrollments.<a href="./src/vitable_partner_api/resources/enrollments.py">reissue</a>(id, \*\*<a href="src/vitable_partner_api/types/enrollment_reissue_params.py">params</a>) -> <a href="./src/vitable_partner_api/types/enrollment.py">Enrollment</a></code>
