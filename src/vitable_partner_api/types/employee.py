# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .member import Member
from .._models import BaseModel
from .dependent import Dependent

__all__ = ["Employee"]


class Employee(BaseModel):
    id: str

    active: bool

    employer_id: str

    member: Member

    start_date: date

    dependents: Optional[List[Dependent]] = None

    terminated_at: Optional[datetime] = None
