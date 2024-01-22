# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...types import PromptResponse, PromptListResponse, prompt_list_params, prompt_create_params
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
from .sql_generations import (
    SqlGenerations,
    AsyncSqlGenerations,
    SqlGenerationsWithRawResponse,
    AsyncSqlGenerationsWithRawResponse,
    SqlGenerationsWithStreamingResponse,
    AsyncSqlGenerationsWithStreamingResponse,
)

__all__ = ["Prompts", "AsyncPrompts"]


class Prompts(SyncAPIResource):
    @cached_property
    def sql_generations(self) -> SqlGenerations:
        return SqlGenerations(self._client)

    @cached_property
    def with_raw_response(self) -> PromptsWithRawResponse:
        return PromptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptsWithStreamingResponse:
        return PromptsWithStreamingResponse(self)

    def create(
        self,
        *,
        db_connection_id: str,
        text: str,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptResponse:
        """
        Create Prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/prompts",
            body=maybe_transform(
                {
                    "db_connection_id": db_connection_id,
                    "text": text,
                    "metadata": metadata,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptResponse,
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
    ) -> PromptResponse:
        """
        Get Prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/prompts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptResponse,
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
    ) -> PromptListResponse:
        """
        Get Prompts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/prompts",
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
                    prompt_list_params.PromptListParams,
                ),
            ),
            cast_to=PromptListResponse,
        )


class AsyncPrompts(AsyncAPIResource):
    @cached_property
    def sql_generations(self) -> AsyncSqlGenerations:
        return AsyncSqlGenerations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPromptsWithRawResponse:
        return AsyncPromptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptsWithStreamingResponse:
        return AsyncPromptsWithStreamingResponse(self)

    async def create(
        self,
        *,
        db_connection_id: str,
        text: str,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptResponse:
        """
        Create Prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/prompts",
            body=maybe_transform(
                {
                    "db_connection_id": db_connection_id,
                    "text": text,
                    "metadata": metadata,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptResponse,
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
    ) -> PromptResponse:
        """
        Get Prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/prompts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptResponse,
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
    ) -> PromptListResponse:
        """
        Get Prompts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/prompts",
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
                    prompt_list_params.PromptListParams,
                ),
            ),
            cast_to=PromptListResponse,
        )


class PromptsWithRawResponse:
    def __init__(self, prompts: Prompts) -> None:
        self._prompts = prompts

        self.create = to_raw_response_wrapper(
            prompts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            prompts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            prompts.list,
        )

    @cached_property
    def sql_generations(self) -> SqlGenerationsWithRawResponse:
        return SqlGenerationsWithRawResponse(self._prompts.sql_generations)


class AsyncPromptsWithRawResponse:
    def __init__(self, prompts: AsyncPrompts) -> None:
        self._prompts = prompts

        self.create = async_to_raw_response_wrapper(
            prompts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            prompts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            prompts.list,
        )

    @cached_property
    def sql_generations(self) -> AsyncSqlGenerationsWithRawResponse:
        return AsyncSqlGenerationsWithRawResponse(self._prompts.sql_generations)


class PromptsWithStreamingResponse:
    def __init__(self, prompts: Prompts) -> None:
        self._prompts = prompts

        self.create = to_streamed_response_wrapper(
            prompts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            prompts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            prompts.list,
        )

    @cached_property
    def sql_generations(self) -> SqlGenerationsWithStreamingResponse:
        return SqlGenerationsWithStreamingResponse(self._prompts.sql_generations)


class AsyncPromptsWithStreamingResponse:
    def __init__(self, prompts: AsyncPrompts) -> None:
        self._prompts = prompts

        self.create = async_to_streamed_response_wrapper(
            prompts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            prompts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            prompts.list,
        )

    @cached_property
    def sql_generations(self) -> AsyncSqlGenerationsWithStreamingResponse:
        return AsyncSqlGenerationsWithStreamingResponse(self._prompts.sql_generations)
