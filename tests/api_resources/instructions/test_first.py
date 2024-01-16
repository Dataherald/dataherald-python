# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald._client import Dataherald, AsyncDataherald
from dataherald.types.shared import InstructionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestFirst:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        first = client.instructions.first.retrieve()
        assert_matches_type(InstructionResponse, first, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.instructions.first.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        first = response.parse()
        assert_matches_type(InstructionResponse, first, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.instructions.first.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            first = response.parse()
            assert_matches_type(InstructionResponse, first, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFirst:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncDataherald) -> None:
        first = await client.instructions.first.retrieve()
        assert_matches_type(InstructionResponse, first, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncDataherald) -> None:
        response = await client.instructions.first.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        first = await response.parse()
        assert_matches_type(InstructionResponse, first, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncDataherald) -> None:
        async with client.instructions.first.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            first = await response.parse()
            assert_matches_type(InstructionResponse, first, path=["response"])

        assert cast(Any, response.is_closed) is True
