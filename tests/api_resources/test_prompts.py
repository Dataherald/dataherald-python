# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import PromptResponse, PromptListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Dataherald) -> None:
        prompt = client.prompts.create(
            db_connection_id="string",
            text="string",
        )
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dataherald) -> None:
        prompt = client.prompts.create(
            db_connection_id="string",
            text="string",
            metadata={},
        )
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dataherald) -> None:
        response = client.prompts.with_raw_response.create(
            db_connection_id="string",
            text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dataherald) -> None:
        with client.prompts.with_streaming_response.create(
            db_connection_id="string",
            text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        prompt = client.prompts.retrieve(
            "string",
        )
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.prompts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.prompts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        prompt = client.prompts.list()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dataherald) -> None:
        prompt = client.prompts.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.prompts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dataherald) -> None:
        with client.prompts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDataherald) -> None:
        prompt = await async_client.prompts.create(
            db_connection_id="string",
            text="string",
        )
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDataherald) -> None:
        prompt = await async_client.prompts.create(
            db_connection_id="string",
            text="string",
            metadata={},
        )
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDataherald) -> None:
        response = await async_client.prompts.with_raw_response.create(
            db_connection_id="string",
            text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDataherald) -> None:
        async with async_client.prompts.with_streaming_response.create(
            db_connection_id="string",
            text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDataherald) -> None:
        prompt = await async_client.prompts.retrieve(
            "string",
        )
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDataherald) -> None:
        response = await async_client.prompts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDataherald) -> None:
        async with async_client.prompts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDataherald) -> None:
        prompt = await async_client.prompts.list()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDataherald) -> None:
        prompt = await async_client.prompts.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDataherald) -> None:
        response = await async_client.prompts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDataherald) -> None:
        async with async_client.prompts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True
