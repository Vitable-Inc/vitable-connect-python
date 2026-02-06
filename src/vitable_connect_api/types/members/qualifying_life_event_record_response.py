# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .qualifying_life_event import QualifyingLifeEvent

__all__ = ["QualifyingLifeEventRecordResponse"]


class QualifyingLifeEventRecordResponse(BaseModel):
    """Response containing a single qualifying life event resource."""

    data: QualifyingLifeEvent
    """Serializer for Qualifying Life Event entity in public API responses.

    QLEs are significant life changes (marriage, birth, adoption, loss of coverage)
    that allow employees to modify benefit elections outside of open enrollment.
    """
