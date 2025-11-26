# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Plan"]


class Plan(BaseModel):
    id: str

    plan_name: str
    """Plan name (e.g., MEC, MEC Plus)"""
