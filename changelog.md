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

