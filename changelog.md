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

