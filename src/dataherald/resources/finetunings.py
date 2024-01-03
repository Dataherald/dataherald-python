# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List

import httpx

from ..types import FinetuningResponse, finetuning_create_params
from .._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    NotGiven,
)
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import (
    make_request_options,
)

if TYPE_CHECKING:
    from .._client import Dataherald, AsyncDataherald

__all__ = ["Finetunings", "AsyncFinetunings"]


class Finetunings(SyncAPIResource):
    with_raw_response: FinetuningsWithRawResponse

    def __init__(self, client: Dataherald) -> None:
        super().__init__(client)
        self.with_raw_response = FinetuningsWithRawResponse(self)

    def create(
        self,
        *,
        base_llm: finetuning_create_params.BaseLlm,
        db_connection_id: str,
        golden_records: List[str] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuningResponse:
        """
        Api Create Api Finetuning Job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/finetunings",
            body=maybe_transform(
                {
                    "base_llm": base_llm,
                    "db_connection_id": db_connection_id,
                    "golden_records": golden_records,
                    "metadata": metadata,
                },
                finetuning_create_params.FinetuningCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuningResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuningResponse:
        """
        Api Get Finetuning Job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/finetunings/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuningResponse,
        )


class AsyncFinetunings(AsyncAPIResource):
    with_raw_response: AsyncFinetuningsWithRawResponse

    def __init__(self, client: AsyncDataherald) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncFinetuningsWithRawResponse(self)

    async def create(
        self,
        *,
        base_llm: finetuning_create_params.BaseLlm,
        db_connection_id: str,
        golden_records: List[str] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuningResponse:
        """
        Api Create Api Finetuning Job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/finetunings",
            body=maybe_transform(
                {
                    "base_llm": base_llm,
                    "db_connection_id": db_connection_id,
                    "golden_records": golden_records,
                    "metadata": metadata,
                },
                finetuning_create_params.FinetuningCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuningResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuningResponse:
        """
        Api Get Finetuning Job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/finetunings/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuningResponse,
        )


class FinetuningsWithRawResponse:
    def __init__(self, finetunings: Finetunings) -> None:
        self.create = to_raw_response_wrapper(
            finetunings.create,
        )
        self.retrieve = to_raw_response_wrapper(
            finetunings.retrieve,
        )


class AsyncFinetuningsWithRawResponse:
    def __init__(self, finetunings: AsyncFinetunings) -> None:
        self.create = async_to_raw_response_wrapper(
            finetunings.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            finetunings.retrieve,
        )
