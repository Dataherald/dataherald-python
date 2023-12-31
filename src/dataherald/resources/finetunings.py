# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

import httpx

from ..types import (
    FinetuningResponse,
    FinetuningListResponse,
    finetuning_list_params,
    finetuning_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["Finetunings", "AsyncFinetunings"]


class Finetunings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FinetuningsWithRawResponse:
        return FinetuningsWithRawResponse(self)

    def create(
        self,
        *,
        db_connection_id: str,
        alias: str | NotGiven = NOT_GIVEN,
        base_llm: finetuning_create_params.BaseLlm | NotGiven = NOT_GIVEN,
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
                    "db_connection_id": db_connection_id,
                    "alias": alias,
                    "base_llm": base_llm,
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

    def list(
        self,
        *,
        db_connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuningListResponse:
        """
        Get Finetuning Jobs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/finetunings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"db_connection_id": db_connection_id}, finetuning_list_params.FinetuningListParams
                ),
            ),
            cast_to=FinetuningListResponse,
        )


class AsyncFinetunings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFinetuningsWithRawResponse:
        return AsyncFinetuningsWithRawResponse(self)

    async def create(
        self,
        *,
        db_connection_id: str,
        alias: str | NotGiven = NOT_GIVEN,
        base_llm: finetuning_create_params.BaseLlm | NotGiven = NOT_GIVEN,
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
                    "db_connection_id": db_connection_id,
                    "alias": alias,
                    "base_llm": base_llm,
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

    async def list(
        self,
        *,
        db_connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuningListResponse:
        """
        Get Finetuning Jobs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/finetunings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"db_connection_id": db_connection_id}, finetuning_list_params.FinetuningListParams
                ),
            ),
            cast_to=FinetuningListResponse,
        )


class FinetuningsWithRawResponse:
    def __init__(self, finetunings: Finetunings) -> None:
        self.create = to_raw_response_wrapper(
            finetunings.create,
        )
        self.retrieve = to_raw_response_wrapper(
            finetunings.retrieve,
        )
        self.list = to_raw_response_wrapper(
            finetunings.list,
        )


class AsyncFinetuningsWithRawResponse:
    def __init__(self, finetunings: AsyncFinetunings) -> None:
        self.create = async_to_raw_response_wrapper(
            finetunings.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            finetunings.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            finetunings.list,
        )
