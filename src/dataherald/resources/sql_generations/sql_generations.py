# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...types import (
    SqlGenerationListResponse,
    SqlGenerationExecuteResponse,
    sql_generation_list_params,
    sql_generation_create_params,
    sql_generation_execute_params,
)
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
from ...types.shared import SqlGenerationResponse
from .nl_generations import (
    NlGenerations,
    AsyncNlGenerations,
    NlGenerationsWithRawResponse,
    AsyncNlGenerationsWithRawResponse,
    NlGenerationsWithStreamingResponse,
    AsyncNlGenerationsWithStreamingResponse,
)

__all__ = ["SqlGenerations", "AsyncSqlGenerations"]


class SqlGenerations(SyncAPIResource):
    @cached_property
    def nl_generations(self) -> NlGenerations:
        return NlGenerations(self._client)

    @cached_property
    def with_raw_response(self) -> SqlGenerationsWithRawResponse:
        return SqlGenerationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SqlGenerationsWithStreamingResponse:
        return SqlGenerationsWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: sql_generation_create_params.Prompt,
        evaluate: bool | NotGiven = NOT_GIVEN,
        finetuning_id: str | NotGiven = NOT_GIVEN,
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
        Create Prompt Sql Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/prompts/sql-generations",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "evaluate": evaluate,
                    "finetuning_id": finetuning_id,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SqlGenerationResponse:
        """
        Get Sql Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/sql-generations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SqlGenerationResponse,
        )

    def list(
        self,
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
    ) -> SqlGenerationListResponse:
        """
        Get Sql Generations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/sql-generations",
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
                    sql_generation_list_params.SqlGenerationListParams,
                ),
            ),
            cast_to=SqlGenerationListResponse,
        )

    def execute(
        self,
        id: str,
        *,
        max_rows: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SqlGenerationExecuteResponse:
        """
        Execute Sql Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/sql-generations/{id}/execute",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"max_rows": max_rows}, sql_generation_execute_params.SqlGenerationExecuteParams),
            ),
            cast_to=SqlGenerationExecuteResponse,
        )


class AsyncSqlGenerations(AsyncAPIResource):
    @cached_property
    def nl_generations(self) -> AsyncNlGenerations:
        return AsyncNlGenerations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSqlGenerationsWithRawResponse:
        return AsyncSqlGenerationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSqlGenerationsWithStreamingResponse:
        return AsyncSqlGenerationsWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: sql_generation_create_params.Prompt,
        evaluate: bool | NotGiven = NOT_GIVEN,
        finetuning_id: str | NotGiven = NOT_GIVEN,
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
        Create Prompt Sql Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/prompts/sql-generations",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "evaluate": evaluate,
                    "finetuning_id": finetuning_id,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SqlGenerationResponse:
        """
        Get Sql Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/sql-generations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SqlGenerationResponse,
        )

    async def list(
        self,
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
    ) -> SqlGenerationListResponse:
        """
        Get Sql Generations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/sql-generations",
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
                    sql_generation_list_params.SqlGenerationListParams,
                ),
            ),
            cast_to=SqlGenerationListResponse,
        )

    async def execute(
        self,
        id: str,
        *,
        max_rows: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SqlGenerationExecuteResponse:
        """
        Execute Sql Generation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/sql-generations/{id}/execute",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"max_rows": max_rows}, sql_generation_execute_params.SqlGenerationExecuteParams),
            ),
            cast_to=SqlGenerationExecuteResponse,
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
        self.list = to_raw_response_wrapper(
            sql_generations.list,
        )
        self.execute = to_raw_response_wrapper(
            sql_generations.execute,
        )

    @cached_property
    def nl_generations(self) -> NlGenerationsWithRawResponse:
        return NlGenerationsWithRawResponse(self._sql_generations.nl_generations)


class AsyncSqlGenerationsWithRawResponse:
    def __init__(self, sql_generations: AsyncSqlGenerations) -> None:
        self._sql_generations = sql_generations

        self.create = async_to_raw_response_wrapper(
            sql_generations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sql_generations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            sql_generations.list,
        )
        self.execute = async_to_raw_response_wrapper(
            sql_generations.execute,
        )

    @cached_property
    def nl_generations(self) -> AsyncNlGenerationsWithRawResponse:
        return AsyncNlGenerationsWithRawResponse(self._sql_generations.nl_generations)


class SqlGenerationsWithStreamingResponse:
    def __init__(self, sql_generations: SqlGenerations) -> None:
        self._sql_generations = sql_generations

        self.create = to_streamed_response_wrapper(
            sql_generations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sql_generations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            sql_generations.list,
        )
        self.execute = to_streamed_response_wrapper(
            sql_generations.execute,
        )

    @cached_property
    def nl_generations(self) -> NlGenerationsWithStreamingResponse:
        return NlGenerationsWithStreamingResponse(self._sql_generations.nl_generations)


class AsyncSqlGenerationsWithStreamingResponse:
    def __init__(self, sql_generations: AsyncSqlGenerations) -> None:
        self._sql_generations = sql_generations

        self.create = async_to_streamed_response_wrapper(
            sql_generations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sql_generations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            sql_generations.list,
        )
        self.execute = async_to_streamed_response_wrapper(
            sql_generations.execute,
        )

    @cached_property
    def nl_generations(self) -> AsyncNlGenerationsWithStreamingResponse:
        return AsyncNlGenerationsWithStreamingResponse(self._sql_generations.nl_generations)
