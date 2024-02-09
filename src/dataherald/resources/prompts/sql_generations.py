# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.shared import NlGenerationResponse, SqlGenerationResponse
from ...types.prompts import (
    sql_generation_create_params,
    sql_generation_retrieve_params,
    sql_generation_nl_generations_params,
)

__all__ = ["SqlGenerations", "AsyncSqlGenerations"]


class SqlGenerations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SqlGenerationsWithRawResponse:
        return SqlGenerationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SqlGenerationsWithStreamingResponse:
        return SqlGenerationsWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        evaluate: bool | NotGiven = NOT_GIVEN,
        finetuning_id: str | NotGiven = NOT_GIVEN,
        low_latency_mode: bool | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        sql: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SqlGenerationResponse:
        """
        Create Sql Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/prompts/{id}/sql-generations",
            body=maybe_transform(
                {
                    "evaluate": evaluate,
                    "finetuning_id": finetuning_id,
                    "low_latency_mode": low_latency_mode,
                    "metadata": metadata,
                    "sql": sql,
                },
                sql_generation_create_params.SqlGenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SqlGenerationResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        ascend: bool | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Sql Generations By Prompt Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/prompts/{id}/sql-generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ascend": ascend,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                    },
                    sql_generation_retrieve_params.SqlGenerationRetrieveParams,
                ),
            ),
            cast_to=object,
        )

    def nl_generations(
        self,
        id: str,
        *,
        sql_generation: sql_generation_nl_generations_params.SqlGeneration,
        max_rows: int | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NlGenerationResponse:
        """
        Create Sql Nl Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/prompts/{id}/sql-generations/nl-generations",
            body=maybe_transform(
                {
                    "sql_generation": sql_generation,
                    "max_rows": max_rows,
                    "metadata": metadata,
                },
                sql_generation_nl_generations_params.SqlGenerationNlGenerationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NlGenerationResponse,
        )


class AsyncSqlGenerations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSqlGenerationsWithRawResponse:
        return AsyncSqlGenerationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSqlGenerationsWithStreamingResponse:
        return AsyncSqlGenerationsWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        evaluate: bool | NotGiven = NOT_GIVEN,
        finetuning_id: str | NotGiven = NOT_GIVEN,
        low_latency_mode: bool | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        sql: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SqlGenerationResponse:
        """
        Create Sql Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/prompts/{id}/sql-generations",
            body=maybe_transform(
                {
                    "evaluate": evaluate,
                    "finetuning_id": finetuning_id,
                    "low_latency_mode": low_latency_mode,
                    "metadata": metadata,
                    "sql": sql,
                },
                sql_generation_create_params.SqlGenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SqlGenerationResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        ascend: bool | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Sql Generations By Prompt Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/prompts/{id}/sql-generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ascend": ascend,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                    },
                    sql_generation_retrieve_params.SqlGenerationRetrieveParams,
                ),
            ),
            cast_to=object,
        )

    async def nl_generations(
        self,
        id: str,
        *,
        sql_generation: sql_generation_nl_generations_params.SqlGeneration,
        max_rows: int | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NlGenerationResponse:
        """
        Create Sql Nl Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/prompts/{id}/sql-generations/nl-generations",
            body=maybe_transform(
                {
                    "sql_generation": sql_generation,
                    "max_rows": max_rows,
                    "metadata": metadata,
                },
                sql_generation_nl_generations_params.SqlGenerationNlGenerationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NlGenerationResponse,
        )


class SqlGenerationsWithRawResponse:
    def __init__(self, sql_generations: SqlGenerations) -> None:
        self._sql_generations = sql_generations

        self.create = to_raw_response_wrapper(
            sql_generations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sql_generations.retrieve,
        )
        self.nl_generations = to_raw_response_wrapper(
            sql_generations.nl_generations,
        )


class AsyncSqlGenerationsWithRawResponse:
    def __init__(self, sql_generations: AsyncSqlGenerations) -> None:
        self._sql_generations = sql_generations

        self.create = async_to_raw_response_wrapper(
            sql_generations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sql_generations.retrieve,
        )
        self.nl_generations = async_to_raw_response_wrapper(
            sql_generations.nl_generations,
        )


class SqlGenerationsWithStreamingResponse:
    def __init__(self, sql_generations: SqlGenerations) -> None:
        self._sql_generations = sql_generations

        self.create = to_streamed_response_wrapper(
            sql_generations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sql_generations.retrieve,
        )
        self.nl_generations = to_streamed_response_wrapper(
            sql_generations.nl_generations,
        )


class AsyncSqlGenerationsWithStreamingResponse:
    def __init__(self, sql_generations: AsyncSqlGenerations) -> None:
        self._sql_generations = sql_generations

        self.create = async_to_streamed_response_wrapper(
            sql_generations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sql_generations.retrieve,
        )
        self.nl_generations = async_to_streamed_response_wrapper(
            sql_generations.nl_generations,
        )
