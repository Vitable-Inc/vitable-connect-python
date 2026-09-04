# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemberListQualifyingLifeEventsResponse"]


class MemberListQualifyingLifeEventsResponse(BaseModel):
    id: str
    """Opaque qualifying life event identifier"""

    event_type: Literal[
        "lost_job_based_coverage",
        "aged_off_parent_plan",
        "lost_medicaid_chip_medicare",
        "lost_decertified_individual_plan",
        "married",
        "divorced",
        "had_baby",
        "adopted_child",
        "foster_care_placement",
        "death_of_spouse_or_dependent",
        "court_ordered",
        "moved_to_new_coverage_area",
        "moved_to_us",
        "moved_to_or_from_school_housing",
        "moved_to_or_from_seasonal_work_housing",
        "became_us_citizen",
        "left_incarceration",
        "gained_tribal_status",
        "started_or_ended_americorps_service",
        "new_child",
        "other",
    ]
    """
    - `lost_job_based_coverage` - lost_job_based_coverage
    - `aged_off_parent_plan` - aged_off_parent_plan
    - `lost_medicaid_chip_medicare` - lost_medicaid_chip_medicare
    - `lost_decertified_individual_plan` - lost_decertified_individual_plan
    - `married` - married
    - `divorced` - divorced
    - `had_baby` - had_baby
    - `adopted_child` - adopted_child
    - `foster_care_placement` - foster_care_placement
    - `death_of_spouse_or_dependent` - death_of_spouse_or_dependent
    - `court_ordered` - court_ordered
    - `moved_to_new_coverage_area` - moved_to_new_coverage_area
    - `moved_to_us` - moved_to_us
    - `moved_to_or_from_school_housing` - moved_to_or_from_school_housing
    - `moved_to_or_from_seasonal_work_housing` -
      moved_to_or_from_seasonal_work_housing
    - `became_us_citizen` - became_us_citizen
    - `left_incarceration` - left_incarceration
    - `gained_tribal_status` - gained_tribal_status
    - `started_or_ended_americorps_service` - started_or_ended_americorps_service
    - `new_child` - new_child
    - `other` - other
    """

    event_type_label: str
    """Human-readable label for event_type"""

    other_event: Optional[str] = None
    """Custom event description when event_type is Other; otherwise normally null"""

    status: Literal["pending", "approved", "denied"]
    """
    - `pending` - Pending
    - `approved` - Approved
    - `denied` - Denied
    """

    submitted_at: datetime
    """When the member submitted the event"""
