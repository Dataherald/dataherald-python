# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import PromptResponse, PromptListResponse
from dataherald._client import Dataherald, AsyncDataherald

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestPrompts:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptResponse, prompt, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptResponse, prompt, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])


class TestAsyncPrompts:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncDataherald) -> None:
        prompt = await client.prompts.create(
            db_connection_id="string",
            text="string",
        )
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncDataherald) -> None:
        prompt = await client.prompts.create(
            db_connection_id="string",
            text="string",
            metadata={},
        )
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncDataherald) -> None:
        response = await client.prompts.with_raw_response.create(
            db_connection_id="string",
            text="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncDataherald) -> None:
        prompt = await client.prompts.retrieve(
            "string",
        )
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncDataherald) -> None:
        response = await client.prompts.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptResponse, prompt, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncDataherald) -> None:
        prompt = await client.prompts.list()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncDataherald) -> None:
        prompt = await client.prompts.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncDataherald) -> None:
        response = await client.prompts.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])
