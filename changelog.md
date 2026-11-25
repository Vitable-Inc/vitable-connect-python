## 6.7.0 - 2026-11-25
### Added
* **`MemberEnrollment.requires_qle_for_termination`** — new required `bool` field indicating whether terminating the enrollment requires a qualifying life event under its benefit product.
* **`MemberEnrollment.plan_selection_required`** — new required `bool` field indicating whether enrolling in the benefit product involves choosing a plan.
### Changed
* **`EnrollmentsClient.terminate` / `RawEnrollmentsClient.terminate`** — docstrings updated to clarify that `carrier_coverage_end_date` is accepted for all enrollments whose benefit requires an external plan (`requires_external_plan`), not only ICHRA, and that the QLE exemption applies to all allowance-based plans (ICHRA, QSEHRA, GCHRA).

## 6.6.1 - 2026-11-20
* chore: update docstrings to replace ICHRA-specific language with generalized terms
* Refresh documentation strings across `BenefitPlanYearDetail`,
* `BenefitPlanYearList`, `ContributionStrategy`, and
* `IchraContributionClass` to reflect that the described behaviors apply
* to all external-plan / allowance-based benefits, not just ICHRA. No
* public API surface, field names, types, or runtime behavior changed.
* Key changes:
* `BenefitPlanYearDetail` and `BenefitPlanYearList`: clarify that `network_names` returns `["multi"]` for all external-plan benefits (not only ICHRA) and is empty for benefits without plan selection
* `BenefitPlanYearDetail` and `BenefitPlanYearList`: update `premium_in_cents` docstring from "ICHRA benefit" to "external-plan benefit"
* `ContributionStrategy` and `IchraContributionClass`: replace "ICHRA" terminology with "allowance-based" / "allowance classes" in class and field docstrings
* 🌿 Generated with Fern

## 6.6.0 - 2026-11-18
### Added
* **`BenefitFamily` / `BenefitFamilyParamItem`** — new `"hra"` literal value recognized alongside the existing `mec`, `mvp`, `ichra`, `vpc`, `dental`, and `vision` families.
* **`ProductCode`** — two new HRA product codes, `QSEHRA_REIMBURSEMENT_ONLY` and `GCHRA_REIMBURSEMENT_ONLY`, are now recognized; docstrings on `BenefitSummary`, `DigitalBenefitCard`, and `MemberEnrollment` updated to document them.
* **`MemberLegalDependent.legal_dependent_id`** — new required `str` field carrying the dependent-relationship identifier (prefixed with `ldep_`).

## 6.5.0 - 2026-11-10
### Added
* **`vitable_organization`** — new optional `XVitableOrganization` parameter on `EmployeesClient.get` and `EmployeesClient.update` (sync, async, raw, and async-raw variants) that sends the `X-Vitable-Organization` HTTP header, allowing multi-organization API key holders to specify which organization to act as on a per-request basis.
* **`UnprocessableEntityError`** — `EmployeesClient.update` (and its async/raw variants) now raises `UnprocessableEntityError` on HTTP 422 responses, surfacing `email_taken` and `invalid_account_update` app error codes.
* **`update` error documentation** — docstrings expanded to document 403 `organization_access_denied`, 404 employee-not-found, 422 `app_error_code` values, and 400 malformed-input / `invalid_employee_update` / `employee_already_terminated` responses.

## 6.4.1 - 2026-11-06
* chore: document 409 HRIS connection error for employee update endpoint
* Expand the docstring on `EmployeesClient.update` (sync, async, raw, and
* async-raw variants) to document the new 409 `employer_has_hris_connection`
* error that the API returns when a caller attempts to change `employee_class`,
* `compensation_type`, or `start_date` for an employer with an active, pending,
* or inactive HRIS connection. Paused connections do not block the request;
* re-sending the current values with a new `effective_date` is still allowed.
* Key changes:
* Updated docstring on `EmployeesClient.update` (sync) to describe the 409 response
* Updated docstring on `AsyncEmployeesClient.update` (async) to describe the 409 response
* Updated docstrings on `RawEmployeesClient.update` and `AsyncRawEmployeesClient.update` to match
* 🌿 Generated with Fern

## 6.4.0 - 2026-11-05
### Added
* **`MemberEnrollment.requires_external_plan`** — new `bool` field indicating whether the enrollment's benefit product requires the member to choose an external health plan through a carrier application.

## 6.3.0 - 2026-11-03
### Added
* **`PlanYearEnrollmentElectionStatus`** and **`ElectionStatusItem`** now include an `Upcoming` value, representing enrollments whose window has not yet opened.
* **`MemberEnrollment.election_status`** and **`PlanYearEnrollment.election_status`** documentation updated to clarify that a terminated unanswered enrollment is `Expired` even before its window opens.

## 6.2.0 - 2026-10-26
### Added
* **`EnrollmentsClient.terminate`** — new optional `carrier_coverage_end_date` (`dt.date`) parameter lets ICHRA callers supply the exact date the carrier policy ended; accepted on both sync and async variants as well as the raw HTTP clients.
* **`MemberEnrollment.answered_at`** — new optional `datetime` field exposing when the employee enrolled or waived.

## 6.1.0 - 2026-10-16
### Added
* **`Member.individual_income_in_cents`** — new optional field exposing the member's annual individual income in cents, if provided.
* **`Member.household_income_in_cents`** — new optional field exposing the member's annual household income in cents, if provided.
* **`MemberAddress.county_name`** — new optional field exposing the member's county name, if known.

## 6.0.0 - 2026-10-15
### Breaking Changes
* **`MemberEnrollment.in_last_month_of_coverage`** has been renamed to **`plan_year_ends_this_month`**. Update all references from `enrollment.in_last_month_of_coverage` to `enrollment.plan_year_ends_this_month`; accessing the old name will raise `AttributeError` at runtime.

## 5.2.0 - 2026-10-02
### Added
* **`MembersClient.create_dependent`** — new sync and async method to save a spouse or child dependent for a member via `POST v1/members/{member_id}/dependents`; also available as a raw HTTP variant on `RawMembersClient` and `AsyncRawMembersClient`.
* **`CreateMemberDependentAddressRequest`** — new request model for supplying a dependent's residential address (`address_line1`, `address_line2`, `city`, `state`, `zipcode`), exported from `vitable_connect` and `vitable_connect.types`.
* **`SavedMemberDependent`** and **`SavedMemberDependentResponse`** — new response models returned by `create_dependent`, representing the saved dependent row and its wrapper; exported from `vitable_connect` and `vitable_connect.types`.

## 5.1.2 - 2026-10-02
* chore: clarify `in_last_month_of_coverage` field documentation
* Update the docstring for `MemberEnrollment.in_last_month_of_coverage` to
* more precisely describe the coverage window logic. The field now documents
* that "today" is evaluated in ET (Eastern Time) and that the final-month
* check considers the earliest of termination, subscription end, plan-year
* end, and selected-plan end dates — not just the plan-year coverage window.
* Key changes:
* Adds "(ET)" timezone qualifier to clarify how "today" is determined
* Expands the coverage window definition to include termination date, subscription end, and selected-plan end alongside plan-year end
* No runtime or API surface changes; documentation only
* 🌿 Generated with Fern

## 5.1.1 - 2026-10-01
* chore: clarify phone and country field documentation
* Update docstrings for the `phone` and `country` parameters across
* employee client methods and the `EmployeeAddressInput` type to provide
* more precise usage guidance.
* Key changes:
* `phone` parameter docstring now specifies "10-digit US phone number; formatting characters and a leading 1 are ignored"
* `EmployeeAddressInput.country` docstring now notes "Only US addresses are supported; the value is ignored"
* Changes apply consistently across `EmployeesClient`, `AsyncEmployeesClient`, `RawEmployeesClient`, and `AsyncRawEmployeesClient`
* 🌿 Generated with Fern

## 5.1.0 - 2026-09-28
### Added
* **`PlanYearIchraAffordability`** — new type alias (`"Affordable" | "Not Affordable"`) exported from `vitable_connect` and `vitable_connect.types` representing whether an ICHRA plan year was configured as affordable.
* **`MemberEnrollment.plan_year_ichra_affordability`** — new optional `PlanYearIchraAffordability` field indicating the affordability setting of the ICHRA plan year; `None` for non-ICHRA rows or ICHRA plan years where it has not been set.
* **`PlanYearEnrollment.plan_year_ichra_affordability`** — new optional `PlanYearIchraAffordability` field with the same semantics as the `MemberEnrollment` counterpart.

## 5.0.0 - 2026-09-24
### Breaking Changes
* **`AccessMethod`** has been removed from `vitable_connect` and `vitable_connect.types`. Replace all imports with `PayrollAccessMethod`, which carries the same literal values (`"SELF_SETUP"`, `"NEEDS_HELP"`).
* **`AdditionalAccessMethod`** has been removed from `vitable_connect` and `vitable_connect.types`. Replace all imports with `PayrollAccessMethod`, which carries the same literal values (`"SELF_SETUP"`, `"NEEDS_HELP"`).
* **`EmployersClient.setup_payroll_access`** (and `AsyncEmployersClient`, `RawEmployersClient`, `AsyncRawEmployersClient`) — the `access_method` and `additional_access_method` parameters now accept `PayrollAccessMethod` instead of `AccessMethod`/`AdditionalAccessMethod`; update any static type annotations accordingly.
* **`BenefitPlanNetwork.address`** is now typed as `DetailedAddress` instead of `Address`; update any code that constructs or type-checks this field.
### Added
* **`PayrollAccessMethod`** — new unified type alias (`Literal["SELF_SETUP", "NEEDS_HELP"] | Any`) that replaces the former `AccessMethod` and `AdditionalAccessMethod`; exported from `vitable_connect` and `vitable_connect.types`.
* **`DetailedAddress`** — new Pydantic model extending address data with `latitude`, `longitude`, `county_fips_code`, and `county_name` fields; exported from `vitable_connect` and `vitable_connect.types`.

## 4.1.0 - 2026-09-22
### Added
* **`MemberEnrollment.enrolled_date`** — new optional `date` field (YYYY-MM-DD) representing the date the member enrolled; `None` unless the row is an election.

## 4.0.0 - 2026-09-16
### Breaking Changes
* **`Organization`** has been removed from `vitable_connect` and `vitable_connect.types`. Remove all imports of `Organization`; if you need organization data, use `OrganizationMembership` (introduced in v3.0.0) which covers the same fields plus a `role` field.
* **`OrganizationsClient.create`** (and `AsyncOrganizationsClient`, `RawOrganizationsClient`, `AsyncRawOrganizationsClient`) has been removed. The organization onboarding endpoint is no longer available through the SDK; remove all calls to `organizations.create()`.

## 3.0.0 - 2026-09-11
### Breaking Changes
* **`CreateOrganizationRequestType`** has been removed from `vitable_connect` and `vitable_connect.types`. Replace all imports with `OrganizationType`, which covers the same set of literal values (`"BROKERAGE"`, `"TPA"`, `"GENERAL_AGENT"`, `"CHANNEL_PARTNER"`, `"CONSULTING_FIRM"`, `"API_PLATFORM"`).
* **`OrganizationsListResponse.organizations`** now contains `List[OrganizationMembership]` instead of `List[Organization]`. Update any code that accesses fields unique to `Organization` to use the new `OrganizationMembership` model, which adds a `role` field and retains all core organization fields.
* **`OrganizationsClient.create`** (and `AsyncOrganizationsClient`, `RawOrganizationsClient`, `AsyncRawOrganizationsClient`) — the `type` parameter type annotation changes from `CreateOrganizationRequestType` to `OrganizationType`; runtime behavior is unchanged but static type checkers will flag the old import.
### Added
* **`OrganizationMembership`** — new Pydantic model representing an organization the caller belongs to, including `id`, `name`, `type`, `idp_org_id`, `idp_provider`, `super_in`, and `role`; exported from `vitable_connect` and `vitable_connect.types`.
* **`OrganizationUserRole`** — new type alias (`Literal["ADMIN", "OPERATIONS", "SALES", "ENROLLMENT_AGENT"] | Any`) representing the caller's role within an organization; exported from `vitable_connect` and `vitable_connect.types`.

## 2.1.0 - 2026-09-08
### Added
* **`vitable_organization`** — new optional `XVitableOrganization` keyword argument added to all methods on `MembersClient`, `AsyncMembersClient`, `EmployersClient`, `AsyncEmployersClient`, `RawEmployersClient`, `AsyncRawEmployersClient`, `EnrollmentsClient`, and their async equivalents; pass an organization ID to forward the `X-Vitable-Organization` HTTP header and scope requests when credentials span multiple organizations.
* **`XVitableOrganization`** — new type alias (`str`) exported from `vitable_connect` and `vitable_connect.types` representing an organization identifier for multi-org API calls.
### Changed
* **`OrganizationsClient.create`** — docstring updated to reflect multi-org semantics; the previous one-organization-per-user restriction and `409 organization_already_exists` note have been replaced with new multi-org and domain-claiming behavior.

## 2.0.0 - 2026-09-08
### Breaking Changes
* **`Operation`** has been removed from `vitable_connect` and `vitable_connect.types`. Replace all imports of `Operation` with `GroupMemberSyncFailureOperation`, which is functionally identical (`Union[Literal["add", "remove"], Any]`).
### Added
* **`GroupMemberSyncFailureOperation`** — a new, more specifically scoped type alias replacing `Operation`, exported from both `vitable_connect` and `vitable_connect.types`.

## 1.0.1 - 2026-09-04
* chore: update User-Agent header to SDK version placeholder
* Replace the hardcoded version string in the User-Agent header with the
* Fern-managed placeholder value. This is an internal SDK regeneration
* artifact and has no effect on public API behavior.
* Key changes:
* Updated `User-Agent` header value from `vitable-connect/1.0.0` to `vitable-connect/0.0.0-fern-placeholder` in `BaseClientWrapper`
* 🌿 Generated with Fern

