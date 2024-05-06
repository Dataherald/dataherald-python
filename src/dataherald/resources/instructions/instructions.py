# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .first import (
    FirstResource,
    AsyncFirstResource,
    FirstResourceWithRawResponse,
    AsyncFirstResourceWithRawResponse,
    FirstResourceWithStreamingResponse,
    AsyncFirstResourceWithStreamingResponse,
)
from ...types import instruction_list_params, instruction_create_params, instruction_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ...types.instruction_list_response import InstructionListResponse
from ...types.shared.instruction_response import InstructionResponse

__all__ = ["InstructionsResource", "AsyncInstructionsResource"]


class InstructionsResource(SyncAPIResource):
    @cached_property
    def first(self) -> FirstResource:
        return FirstResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstructionsResourceWithRawResponse:
        return InstructionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstructionsResourceWithStreamingResponse:
        return InstructionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        instruction: str,
        db_connection_id: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionResponse:
        """
        Api Add Instructions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/instructions",
            body=maybe_transform(
                {
                    "instruction": instruction,
                    "db_connection_id": db_connection_id,
                    "metadata": metadata,
                },
                instruction_create_params.InstructionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
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
    ) -> InstructionResponse:
        """
        Get Instruction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/instructions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
        )

    def update(
        self,
        id: str,
        *,
        instruction: str,
        db_connection_id: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionResponse:
        """
        Api Update Instruction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/api/instructions/{id}",
            body=maybe_transform(
                {
                    "instruction": instruction,
                    "db_connection_id": db_connection_id,
                    "metadata": metadata,
                },
                instruction_update_params.InstructionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
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
    ) -> InstructionListResponse:
        """
        Api Get Instructions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/instructions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"db_connection_id": db_connection_id}, instruction_list_params.InstructionListParams
                ),
            ),
            cast_to=InstructionListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Api Delete Instruction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/instructions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncInstructionsResource(AsyncAPIResource):
    @cached_property
    def first(self) -> AsyncFirstResource:
        return AsyncFirstResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstructionsResourceWithRawResponse:
        return AsyncInstructionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstructionsResourceWithStreamingResponse:
        return AsyncInstructionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        instruction: str,
        db_connection_id: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionResponse:
        """
        Api Add Instructions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/instructions",
            body=await async_maybe_transform(
                {
                    "instruction": instruction,
                    "db_connection_id": db_connection_id,
                    "metadata": metadata,
                },
                instruction_create_params.InstructionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
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
    ) -> InstructionResponse:
        """
        Get Instruction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/instructions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
        )

    async def update(
        self,
        id: str,
        *,
        instruction: str,
        db_connection_id: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstructionResponse:
        """
        Api Update Instruction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/api/instructions/{id}",
            body=await async_maybe_transform(
                {
                    "instruction": instruction,
                    "db_connection_id": db_connection_id,
                    "metadata": metadata,
                },
                instruction_update_params.InstructionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstructionResponse,
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
    ) -> InstructionListResponse:
        """
        Api Get Instructions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/instructions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"db_connection_id": db_connection_id}, instruction_list_params.InstructionListParams
                ),
            ),
            cast_to=InstructionListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Api Delete Instruction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/instructions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class InstructionsResourceWithRawResponse:
    def __init__(self, instructions: InstructionsResource) -> None:
        self._instructions = instructions

        self.create = to_raw_response_wrapper(
            instructions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            instructions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            instructions.update,
        )
        self.list = to_raw_response_wrapper(
            instructions.list,
        )
        self.delete = to_raw_response_wrapper(
            instructions.delete,
        )

    @cached_property
    def first(self) -> FirstResourceWithRawResponse:
        return FirstResourceWithRawResponse(self._instructions.first)


class AsyncInstructionsResourceWithRawResponse:
    def __init__(self, instructions: AsyncInstructionsResource) -> None:
        self._instructions = instructions

        self.create = async_to_raw_response_wrapper(
            instructions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            instructions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            instructions.update,
        )
        self.list = async_to_raw_response_wrapper(
            instructions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            instructions.delete,
        )

    @cached_property
    def first(self) -> AsyncFirstResourceWithRawResponse:
        return AsyncFirstResourceWithRawResponse(self._instructions.first)


class InstructionsResourceWithStreamingResponse:
    def __init__(self, instructions: InstructionsResource) -> None:
        self._instructions = instructions

        self.create = to_streamed_response_wrapper(
            instructions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            instructions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            instructions.update,
        )
        self.list = to_streamed_response_wrapper(
            instructions.list,
        )
        self.delete = to_streamed_response_wrapper(
            instructions.delete,
        )

    @cached_property
    def first(self) -> FirstResourceWithStreamingResponse:
        return FirstResourceWithStreamingResponse(self._instructions.first)


class AsyncInstructionsResourceWithStreamingResponse:
    def __init__(self, instructions: AsyncInstructionsResource) -> None:
        self._instructions = instructions

        self.create = async_to_streamed_response_wrapper(
            instructions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            instructions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            instructions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            instructions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            instructions.delete,
        )

    @cached_property
    def first(self) -> AsyncFirstResourceWithStreamingResponse:
        return AsyncFirstResourceWithStreamingResponse(self._instructions.first)
