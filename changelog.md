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

