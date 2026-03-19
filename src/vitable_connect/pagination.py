# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["PageNumberPagePagination", "SyncPageNumberPage", "AsyncPageNumberPage"]

_T = TypeVar("_T")


class PageNumberPagePagination(BaseModel):
    page: Optional[int] = None

    total_pages: Optional[int] = None


class SyncPageNumberPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[PageNumberPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.pagination is not None:
            if self.pagination.page is not None:
                current_page = self.pagination.page
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.pagination is not None:
            if self.pagination.total_pages is not None:
                total_pages = self.pagination.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncPageNumberPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[PageNumberPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.pagination is not None:
            if self.pagination.page is not None:
                current_page = self.pagination.page
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.pagination is not None:
            if self.pagination.total_pages is not None:
                total_pages = self.pagination.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})
