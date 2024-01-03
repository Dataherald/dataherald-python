# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import (
    InstructionListResponse,
)
from dataherald._client import Dataherald, AsyncDataherald
from dataherald.types.shared import InstructionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestInstructions:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Dataherald) -> None:
        instruction = client.instructions.create(
            instruction="string",
        )
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dataherald) -> None:
        instruction = client.instructions.create(
            instruction="string",
            db_connection_id="string",
            metadata={},
        )
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dataherald) -> None:
        response = client.instructions.with_raw_response.create(
            instruction="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    def test_method_update(self, client: Dataherald) -> None:
        instruction = client.instructions.update(
            "string",
            instruction="string",
        )
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Dataherald) -> None:
        instruction = client.instructions.update(
            "string",
            instruction="string",
            db_connection_id="string",
            metadata={},
        )
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Dataherald) -> None:
        response = client.instructions.with_raw_response.update(
            "string",
            instruction="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        instruction = client.instructions.list(
            db_connection_id="string",
        )
        assert_matches_type(InstructionListResponse, instruction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.instructions.with_raw_response.list(
            db_connection_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(InstructionListResponse, instruction, path=["response"])

    @parametrize
    def test_method_delete(self, client: Dataherald) -> None:
        instruction = client.instructions.delete(
            "string",
        )
        assert_matches_type(object, instruction, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Dataherald) -> None:
        response = client.instructions.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(object, instruction, path=["response"])


class TestAsyncInstructions:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncDataherald) -> None:
        instruction = await client.instructions.create(
            instruction="string",
        )
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncDataherald) -> None:
        instruction = await client.instructions.create(
            instruction="string",
            db_connection_id="string",
            metadata={},
        )
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncDataherald) -> None:
        response = await client.instructions.with_raw_response.create(
            instruction="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncDataherald) -> None:
        instruction = await client.instructions.update(
            "string",
            instruction="string",
        )
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncDataherald) -> None:
        instruction = await client.instructions.update(
            "string",
            instruction="string",
            db_connection_id="string",
            metadata={},
        )
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncDataherald) -> None:
        response = await client.instructions.with_raw_response.update(
            "string",
            instruction="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(InstructionResponse, instruction, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncDataherald) -> None:
        instruction = await client.instructions.list(
            db_connection_id="string",
        )
        assert_matches_type(InstructionListResponse, instruction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncDataherald) -> None:
        response = await client.instructions.with_raw_response.list(
            db_connection_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(InstructionListResponse, instruction, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncDataherald) -> None:
        instruction = await client.instructions.delete(
            "string",
        )
        assert_matches_type(object, instruction, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncDataherald) -> None:
        response = await client.instructions.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(object, instruction, path=["response"])
