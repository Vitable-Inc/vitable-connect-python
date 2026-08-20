# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types import (
    Employee,
    EmployerResponse,
    EmployerListResponse,
    EmployerListInvoicesResponse,
    EmployerRetrieveHRISResponse,
    EmployerUpdateSettingsResponse,
    EmployerSubmitCensusSyncResponse,
    EmployerListHRISProvidersResponse,
    EmployerRetrieveInvoicePdfResponse,
    EmployerListBenefitPlanYearsResponse,
    EmployerRetrieveBenefitPlanYearResponse,
    EmployerSubmitPayrollAccessSetupResponse,
    EmployerRetrievePayrollAccessSetupResponse,
    EmployerEnsurePayrollIntegrationEmailResponse,
    EmployerListBenefitPlanYearEnrollmentsResponse,
    EmployerListPayrollDeductionStatementsResponse,
)
from vitable_connect._utils import parse_date
from vitable_connect.pagination import SyncPageNumberPage, AsyncPageNumberPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: VitableConnect) -> None:
        employer = client.employers.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
                "address_line_2": "Floor 5",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
            phone_number="2065550100",
            reference_id="partner-emp-001",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VitableConnect) -> None:
        employer = client.employers.retrieve(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.retrieve(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.retrieve(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: VitableConnect) -> None:
        employer = client.employers.update(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.update(
            employer_id="empr_abc123def456",
            active=True,
            address={
                "address_line_1": "address_line_1",
                "city": "city",
                "state": "xx",
                "zipcode": "zipcode",
                "address_line_2": "address_line_2",
            },
            legal_name="x",
            name="x",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.update(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.update(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.update(
                employer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnect) -> None:
        employer = client.employers.list()
        assert_matches_type(SyncPageNumberPage[EmployerListResponse], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.list(
            benefit_family=["mec"],
            benefit_lifecycle_stage=["open_enrollment"],
            hris_provider=["string"],
            hris_status=["Pending"],
            include_cancelled=True,
            limit=20,
            page=1,
            search="x",
        )
        assert_matches_type(SyncPageNumberPage[EmployerListResponse], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(SyncPageNumberPage[EmployerListResponse], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(SyncPageNumberPage[EmployerListResponse], employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ensure_payroll_integration_email(self, client: VitableConnect) -> None:
        employer = client.employers.ensure_payroll_integration_email(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerEnsurePayrollIntegrationEmailResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ensure_payroll_integration_email(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.ensure_payroll_integration_email(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerEnsurePayrollIntegrationEmailResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ensure_payroll_integration_email(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.ensure_payroll_integration_email(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerEnsurePayrollIntegrationEmailResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_ensure_payroll_integration_email(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.ensure_payroll_integration_email(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_benefit_plan_year_enrollments(self, client: VitableConnect) -> None:
        employer = client.employers.list_benefit_plan_year_enrollments(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        )
        assert_matches_type(
            SyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_benefit_plan_year_enrollments_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.list_benefit_plan_year_enrollments(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
            election_status=["Enrolled"],
            limit=20,
            page=1,
            search="search",
        )
        assert_matches_type(
            SyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_benefit_plan_year_enrollments(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.list_benefit_plan_year_enrollments(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(
            SyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_benefit_plan_year_enrollments(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.list_benefit_plan_year_enrollments(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(
                SyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse], employer, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_benefit_plan_year_enrollments(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.list_benefit_plan_year_enrollments(
                benefit_plan_year_id="plyr_abc123def456",
                employer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_plan_year_id` but received ''"):
            client.employers.with_raw_response.list_benefit_plan_year_enrollments(
                benefit_plan_year_id="",
                employer_id="empr_abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_benefit_plan_years(self, client: VitableConnect) -> None:
        employer = client.employers.list_benefit_plan_years(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerListBenefitPlanYearsResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_benefit_plan_years(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.list_benefit_plan_years(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerListBenefitPlanYearsResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_benefit_plan_years(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.list_benefit_plan_years(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerListBenefitPlanYearsResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_benefit_plan_years(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.list_benefit_plan_years(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_employees(self, client: VitableConnect) -> None:
        employer = client.employers.list_employees(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(SyncPageNumberPage[Employee], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_employees_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.list_employees(
            employer_id="empr_abc123def456",
            employment_status="active",
            limit=20,
            page=1,
            search="jane",
        )
        assert_matches_type(SyncPageNumberPage[Employee], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_employees(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.list_employees(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(SyncPageNumberPage[Employee], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_employees(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.list_employees(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(SyncPageNumberPage[Employee], employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_employees(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.list_employees(
                employer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_hris_providers(self, client: VitableConnect) -> None:
        employer = client.employers.list_hris_providers()
        assert_matches_type(EmployerListHRISProvidersResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_hris_providers(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.list_hris_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerListHRISProvidersResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_hris_providers(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.list_hris_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerListHRISProvidersResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_invoices(self, client: VitableConnect) -> None:
        employer = client.employers.list_invoices(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployerListInvoicesResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_invoices_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.list_invoices(
            employer_id="empr_abc123def456",
            limit=20,
            offset="x",
        )
        assert_matches_type(EmployerListInvoicesResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_invoices(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.list_invoices(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerListInvoicesResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_invoices(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.list_invoices(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerListInvoicesResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_invoices(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.list_invoices(
                employer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_payroll_deduction_statements(self, client: VitableConnect) -> None:
        employer = client.employers.list_payroll_deduction_statements(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(
            SyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_payroll_deduction_statements_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.list_payroll_deduction_statements(
            employer_id="empr_abc123def456",
            limit=20,
            page=1,
        )
        assert_matches_type(
            SyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_payroll_deduction_statements(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.list_payroll_deduction_statements(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(
            SyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_payroll_deduction_statements(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.list_payroll_deduction_statements(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(
                SyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse], employer, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_payroll_deduction_statements(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.list_payroll_deduction_statements(
                employer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_benefit_plan_year(self, client: VitableConnect) -> None:
        employer = client.employers.retrieve_benefit_plan_year(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployerRetrieveBenefitPlanYearResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_benefit_plan_year(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.retrieve_benefit_plan_year(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerRetrieveBenefitPlanYearResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_benefit_plan_year(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.retrieve_benefit_plan_year(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerRetrieveBenefitPlanYearResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_benefit_plan_year(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.retrieve_benefit_plan_year(
                benefit_plan_year_id="plyr_abc123def456",
                employer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_plan_year_id` but received ''"):
            client.employers.with_raw_response.retrieve_benefit_plan_year(
                benefit_plan_year_id="",
                employer_id="empr_abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_hris(self, client: VitableConnect) -> None:
        employer = client.employers.retrieve_hris(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerRetrieveHRISResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_hris(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.retrieve_hris(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerRetrieveHRISResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_hris(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.retrieve_hris(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerRetrieveHRISResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_hris(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.retrieve_hris(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_invoice_pdf(self, client: VitableConnect) -> None:
        employer = client.employers.retrieve_invoice_pdf(
            invoice_id="INV-00042",
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployerRetrieveInvoicePdfResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_invoice_pdf(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.retrieve_invoice_pdf(
            invoice_id="INV-00042",
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerRetrieveInvoicePdfResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_invoice_pdf(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.retrieve_invoice_pdf(
            invoice_id="INV-00042",
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerRetrieveInvoicePdfResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_invoice_pdf(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.retrieve_invoice_pdf(
                invoice_id="INV-00042",
                employer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.employers.with_raw_response.retrieve_invoice_pdf(
                invoice_id="",
                employer_id="empr_abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_payroll_access_setup(self, client: VitableConnect) -> None:
        employer = client.employers.retrieve_payroll_access_setup(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerRetrievePayrollAccessSetupResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_payroll_access_setup(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.retrieve_payroll_access_setup(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerRetrievePayrollAccessSetupResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_payroll_access_setup(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.retrieve_payroll_access_setup(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerRetrievePayrollAccessSetupResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_payroll_access_setup(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.retrieve_payroll_access_setup(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_census_sync(self, client: VitableConnect) -> None:
        employer = client.employers.submit_census_sync(
            employer_id="empr_abc123def456",
            employees=[
                {
                    "date_of_birth": parse_date("1990-05-15"),
                    "email": "jane.doe@acme.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                },
                {
                    "date_of_birth": parse_date("1985-11-20"),
                    "email": "john.smith@acme.com",
                    "first_name": "John",
                    "last_name": "Smith",
                },
            ],
        )
        assert_matches_type(EmployerSubmitCensusSyncResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_census_sync(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.submit_census_sync(
            employer_id="empr_abc123def456",
            employees=[
                {
                    "date_of_birth": parse_date("1990-05-15"),
                    "email": "jane.doe@acme.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                },
                {
                    "date_of_birth": parse_date("1985-11-20"),
                    "email": "john.smith@acme.com",
                    "first_name": "John",
                    "last_name": "Smith",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerSubmitCensusSyncResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_census_sync(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.submit_census_sync(
            employer_id="empr_abc123def456",
            employees=[
                {
                    "date_of_birth": parse_date("1990-05-15"),
                    "email": "jane.doe@acme.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                },
                {
                    "date_of_birth": parse_date("1985-11-20"),
                    "email": "john.smith@acme.com",
                    "first_name": "John",
                    "last_name": "Smith",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerSubmitCensusSyncResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_census_sync(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.submit_census_sync(
                employer_id="",
                employees=[
                    {
                        "date_of_birth": parse_date("1990-05-15"),
                        "email": "jane.doe@acme.com",
                        "first_name": "Jane",
                        "last_name": "Doe",
                    },
                    {
                        "date_of_birth": parse_date("1985-11-20"),
                        "email": "john.smith@acme.com",
                        "first_name": "John",
                        "last_name": "Smith",
                    },
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_payroll_access_setup(self, client: VitableConnect) -> None:
        employer = client.employers.submit_payroll_access_setup(
            employer_id="empr_abc123def456",
            access_method="SELF_SETUP",
            all_benefit_eligible_employees_present=True,
            classifications_accurate=True,
            employees_in_payroll_acknowledged=True,
            has_additional_payroll_system=True,
            is_controlled_group=True,
            payroll_data_impacts_eligibility_acknowledged=True,
        )
        assert_matches_type(EmployerSubmitPayrollAccessSetupResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_payroll_access_setup_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.submit_payroll_access_setup(
            employer_id="empr_abc123def456",
            access_method="SELF_SETUP",
            all_benefit_eligible_employees_present=True,
            classifications_accurate=True,
            employees_in_payroll_acknowledged=True,
            has_additional_payroll_system=True,
            is_controlled_group=True,
            payroll_data_impacts_eligibility_acknowledged=True,
            additional_access_method="SELF_SETUP",
            additional_integration_confirmed=True,
            additional_login_url="additional_login_url",
            additional_password="additional_password",
            additional_phone="additional_phone",
            additional_username="additional_username",
            classification_correction_source="ENTER_NAMES",
            integration_confirmed=True,
            login_url="login_url",
            misclassified_employee_names=["string"],
            missing_employee_resolution="EMAIL_CENSUS",
            password="password",
            phone="phone",
            remaining_employee_action="VITABLE_UPDATE",
            same_payroll_covers_other_eins=True,
            username="username",
        )
        assert_matches_type(EmployerSubmitPayrollAccessSetupResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_payroll_access_setup(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.submit_payroll_access_setup(
            employer_id="empr_abc123def456",
            access_method="SELF_SETUP",
            all_benefit_eligible_employees_present=True,
            classifications_accurate=True,
            employees_in_payroll_acknowledged=True,
            has_additional_payroll_system=True,
            is_controlled_group=True,
            payroll_data_impacts_eligibility_acknowledged=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerSubmitPayrollAccessSetupResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_payroll_access_setup(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.submit_payroll_access_setup(
            employer_id="empr_abc123def456",
            access_method="SELF_SETUP",
            all_benefit_eligible_employees_present=True,
            classifications_accurate=True,
            employees_in_payroll_acknowledged=True,
            has_additional_payroll_system=True,
            is_controlled_group=True,
            payroll_data_impacts_eligibility_acknowledged=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerSubmitPayrollAccessSetupResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_payroll_access_setup(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.submit_payroll_access_setup(
                employer_id="",
                access_method="SELF_SETUP",
                all_benefit_eligible_employees_present=True,
                classifications_accurate=True,
                employees_in_payroll_acknowledged=True,
                has_additional_payroll_system=True,
                is_controlled_group=True,
                payroll_data_impacts_eligibility_acknowledged=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_settings(self, client: VitableConnect) -> None:
        employer = client.employers.update_settings(
            employer_id="empr_abc123def456",
            pay_frequency="bi_weekly",
        )
        assert_matches_type(EmployerUpdateSettingsResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_settings(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.update_settings(
            employer_id="empr_abc123def456",
            pay_frequency="bi_weekly",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerUpdateSettingsResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_settings(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.update_settings(
            employer_id="empr_abc123def456",
            pay_frequency="bi_weekly",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerUpdateSettingsResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_settings(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.update_settings(
                employer_id="",
                pay_frequency="bi_weekly",
            )


class TestAsyncEmployers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
                "address_line_2": "Floor 5",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
            phone_number="2065550100",
            reference_id="partner-emp-001",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.retrieve(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.retrieve(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.retrieve(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.update(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.update(
            employer_id="empr_abc123def456",
            active=True,
            address={
                "address_line_1": "address_line_1",
                "city": "city",
                "state": "xx",
                "zipcode": "zipcode",
                "address_line_2": "address_line_2",
            },
            legal_name="x",
            name="x",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.update(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.update(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.update(
                employer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list()
        assert_matches_type(AsyncPageNumberPage[EmployerListResponse], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list(
            benefit_family=["mec"],
            benefit_lifecycle_stage=["open_enrollment"],
            hris_provider=["string"],
            hris_status=["Pending"],
            include_cancelled=True,
            limit=20,
            page=1,
            search="x",
        )
        assert_matches_type(AsyncPageNumberPage[EmployerListResponse], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(AsyncPageNumberPage[EmployerListResponse], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(AsyncPageNumberPage[EmployerListResponse], employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ensure_payroll_integration_email(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.ensure_payroll_integration_email(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerEnsurePayrollIntegrationEmailResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ensure_payroll_integration_email(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.ensure_payroll_integration_email(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerEnsurePayrollIntegrationEmailResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ensure_payroll_integration_email(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.ensure_payroll_integration_email(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerEnsurePayrollIntegrationEmailResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_ensure_payroll_integration_email(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.ensure_payroll_integration_email(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_benefit_plan_year_enrollments(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list_benefit_plan_year_enrollments(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        )
        assert_matches_type(
            AsyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_benefit_plan_year_enrollments_with_all_params(
        self, async_client: AsyncVitableConnect
    ) -> None:
        employer = await async_client.employers.list_benefit_plan_year_enrollments(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
            election_status=["Enrolled"],
            limit=20,
            page=1,
            search="search",
        )
        assert_matches_type(
            AsyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_benefit_plan_year_enrollments(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.list_benefit_plan_year_enrollments(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(
            AsyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_benefit_plan_year_enrollments(
        self, async_client: AsyncVitableConnect
    ) -> None:
        async with async_client.employers.with_streaming_response.list_benefit_plan_year_enrollments(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(
                AsyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse], employer, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_benefit_plan_year_enrollments(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.list_benefit_plan_year_enrollments(
                benefit_plan_year_id="plyr_abc123def456",
                employer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_plan_year_id` but received ''"):
            await async_client.employers.with_raw_response.list_benefit_plan_year_enrollments(
                benefit_plan_year_id="",
                employer_id="empr_abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_benefit_plan_years(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list_benefit_plan_years(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerListBenefitPlanYearsResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_benefit_plan_years(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.list_benefit_plan_years(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerListBenefitPlanYearsResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_benefit_plan_years(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.list_benefit_plan_years(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerListBenefitPlanYearsResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_benefit_plan_years(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.list_benefit_plan_years(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_employees(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list_employees(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(AsyncPageNumberPage[Employee], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_employees_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list_employees(
            employer_id="empr_abc123def456",
            employment_status="active",
            limit=20,
            page=1,
            search="jane",
        )
        assert_matches_type(AsyncPageNumberPage[Employee], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_employees(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.list_employees(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(AsyncPageNumberPage[Employee], employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_employees(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.list_employees(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(AsyncPageNumberPage[Employee], employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_employees(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.list_employees(
                employer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_hris_providers(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list_hris_providers()
        assert_matches_type(EmployerListHRISProvidersResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_hris_providers(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.list_hris_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerListHRISProvidersResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_hris_providers(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.list_hris_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerListHRISProvidersResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_invoices(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list_invoices(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployerListInvoicesResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_invoices_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list_invoices(
            employer_id="empr_abc123def456",
            limit=20,
            offset="x",
        )
        assert_matches_type(EmployerListInvoicesResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_invoices(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.list_invoices(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerListInvoicesResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_invoices(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.list_invoices(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerListInvoicesResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_invoices(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.list_invoices(
                employer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_payroll_deduction_statements(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list_payroll_deduction_statements(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(
            AsyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_payroll_deduction_statements_with_all_params(
        self, async_client: AsyncVitableConnect
    ) -> None:
        employer = await async_client.employers.list_payroll_deduction_statements(
            employer_id="empr_abc123def456",
            limit=20,
            page=1,
        )
        assert_matches_type(
            AsyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_payroll_deduction_statements(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.list_payroll_deduction_statements(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(
            AsyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse], employer, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_payroll_deduction_statements(
        self, async_client: AsyncVitableConnect
    ) -> None:
        async with async_client.employers.with_streaming_response.list_payroll_deduction_statements(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(
                AsyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse], employer, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_payroll_deduction_statements(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.list_payroll_deduction_statements(
                employer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_benefit_plan_year(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.retrieve_benefit_plan_year(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployerRetrieveBenefitPlanYearResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_benefit_plan_year(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.retrieve_benefit_plan_year(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerRetrieveBenefitPlanYearResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_benefit_plan_year(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.retrieve_benefit_plan_year(
            benefit_plan_year_id="plyr_abc123def456",
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerRetrieveBenefitPlanYearResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_benefit_plan_year(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.retrieve_benefit_plan_year(
                benefit_plan_year_id="plyr_abc123def456",
                employer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_plan_year_id` but received ''"):
            await async_client.employers.with_raw_response.retrieve_benefit_plan_year(
                benefit_plan_year_id="",
                employer_id="empr_abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_hris(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.retrieve_hris(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerRetrieveHRISResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_hris(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.retrieve_hris(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerRetrieveHRISResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_hris(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.retrieve_hris(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerRetrieveHRISResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_hris(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.retrieve_hris(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_invoice_pdf(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.retrieve_invoice_pdf(
            invoice_id="INV-00042",
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployerRetrieveInvoicePdfResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_invoice_pdf(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.retrieve_invoice_pdf(
            invoice_id="INV-00042",
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerRetrieveInvoicePdfResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_invoice_pdf(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.retrieve_invoice_pdf(
            invoice_id="INV-00042",
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerRetrieveInvoicePdfResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_invoice_pdf(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.retrieve_invoice_pdf(
                invoice_id="INV-00042",
                employer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.employers.with_raw_response.retrieve_invoice_pdf(
                invoice_id="",
                employer_id="empr_abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_payroll_access_setup(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.retrieve_payroll_access_setup(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerRetrievePayrollAccessSetupResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_payroll_access_setup(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.retrieve_payroll_access_setup(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerRetrievePayrollAccessSetupResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_payroll_access_setup(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.retrieve_payroll_access_setup(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerRetrievePayrollAccessSetupResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_payroll_access_setup(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.retrieve_payroll_access_setup(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_census_sync(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.submit_census_sync(
            employer_id="empr_abc123def456",
            employees=[
                {
                    "date_of_birth": parse_date("1990-05-15"),
                    "email": "jane.doe@acme.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                },
                {
                    "date_of_birth": parse_date("1985-11-20"),
                    "email": "john.smith@acme.com",
                    "first_name": "John",
                    "last_name": "Smith",
                },
            ],
        )
        assert_matches_type(EmployerSubmitCensusSyncResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_census_sync(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.submit_census_sync(
            employer_id="empr_abc123def456",
            employees=[
                {
                    "date_of_birth": parse_date("1990-05-15"),
                    "email": "jane.doe@acme.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                },
                {
                    "date_of_birth": parse_date("1985-11-20"),
                    "email": "john.smith@acme.com",
                    "first_name": "John",
                    "last_name": "Smith",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerSubmitCensusSyncResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_census_sync(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.submit_census_sync(
            employer_id="empr_abc123def456",
            employees=[
                {
                    "date_of_birth": parse_date("1990-05-15"),
                    "email": "jane.doe@acme.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                },
                {
                    "date_of_birth": parse_date("1985-11-20"),
                    "email": "john.smith@acme.com",
                    "first_name": "John",
                    "last_name": "Smith",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerSubmitCensusSyncResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_census_sync(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.submit_census_sync(
                employer_id="",
                employees=[
                    {
                        "date_of_birth": parse_date("1990-05-15"),
                        "email": "jane.doe@acme.com",
                        "first_name": "Jane",
                        "last_name": "Doe",
                    },
                    {
                        "date_of_birth": parse_date("1985-11-20"),
                        "email": "john.smith@acme.com",
                        "first_name": "John",
                        "last_name": "Smith",
                    },
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_payroll_access_setup(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.submit_payroll_access_setup(
            employer_id="empr_abc123def456",
            access_method="SELF_SETUP",
            all_benefit_eligible_employees_present=True,
            classifications_accurate=True,
            employees_in_payroll_acknowledged=True,
            has_additional_payroll_system=True,
            is_controlled_group=True,
            payroll_data_impacts_eligibility_acknowledged=True,
        )
        assert_matches_type(EmployerSubmitPayrollAccessSetupResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_payroll_access_setup_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.submit_payroll_access_setup(
            employer_id="empr_abc123def456",
            access_method="SELF_SETUP",
            all_benefit_eligible_employees_present=True,
            classifications_accurate=True,
            employees_in_payroll_acknowledged=True,
            has_additional_payroll_system=True,
            is_controlled_group=True,
            payroll_data_impacts_eligibility_acknowledged=True,
            additional_access_method="SELF_SETUP",
            additional_integration_confirmed=True,
            additional_login_url="additional_login_url",
            additional_password="additional_password",
            additional_phone="additional_phone",
            additional_username="additional_username",
            classification_correction_source="ENTER_NAMES",
            integration_confirmed=True,
            login_url="login_url",
            misclassified_employee_names=["string"],
            missing_employee_resolution="EMAIL_CENSUS",
            password="password",
            phone="phone",
            remaining_employee_action="VITABLE_UPDATE",
            same_payroll_covers_other_eins=True,
            username="username",
        )
        assert_matches_type(EmployerSubmitPayrollAccessSetupResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_payroll_access_setup(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.submit_payroll_access_setup(
            employer_id="empr_abc123def456",
            access_method="SELF_SETUP",
            all_benefit_eligible_employees_present=True,
            classifications_accurate=True,
            employees_in_payroll_acknowledged=True,
            has_additional_payroll_system=True,
            is_controlled_group=True,
            payroll_data_impacts_eligibility_acknowledged=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerSubmitPayrollAccessSetupResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_payroll_access_setup(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.submit_payroll_access_setup(
            employer_id="empr_abc123def456",
            access_method="SELF_SETUP",
            all_benefit_eligible_employees_present=True,
            classifications_accurate=True,
            employees_in_payroll_acknowledged=True,
            has_additional_payroll_system=True,
            is_controlled_group=True,
            payroll_data_impacts_eligibility_acknowledged=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerSubmitPayrollAccessSetupResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_payroll_access_setup(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.submit_payroll_access_setup(
                employer_id="",
                access_method="SELF_SETUP",
                all_benefit_eligible_employees_present=True,
                classifications_accurate=True,
                employees_in_payroll_acknowledged=True,
                has_additional_payroll_system=True,
                is_controlled_group=True,
                payroll_data_impacts_eligibility_acknowledged=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_settings(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.update_settings(
            employer_id="empr_abc123def456",
            pay_frequency="bi_weekly",
        )
        assert_matches_type(EmployerUpdateSettingsResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.update_settings(
            employer_id="empr_abc123def456",
            pay_frequency="bi_weekly",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerUpdateSettingsResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.update_settings(
            employer_id="empr_abc123def456",
            pay_frequency="bi_weekly",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerUpdateSettingsResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_settings(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.update_settings(
                employer_id="",
                pay_frequency="bi_weekly",
            )
