# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import FinetuningResponse
from dataherald._client import Dataherald, AsyncDataherald

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestFinetunings:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Dataherald) -> None:
        finetuning = client.finetunings.create(
            base_llm={},
            db_connection_id="string",
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dataherald) -> None:
        finetuning = client.finetunings.create(
            base_llm={
                "_model_provider": "string",
                "_model_name": "string",
                "_model_parameters": {"foo": "string"},
            },
            db_connection_id="string",
            golden_records=["string", "string", "string"],
            metadata={},
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dataherald) -> None:
        response = client.finetunings.with_raw_response.create(
            base_llm={},
            db_connection_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = response.parse()
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        finetuning = client.finetunings.retrieve(
            "string",
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.finetunings.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = response.parse()
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])


class TestAsyncFinetunings:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncDataherald) -> None:
        finetuning = await client.finetunings.create(
            base_llm={},
            db_connection_id="string",
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncDataherald) -> None:
        finetuning = await client.finetunings.create(
            base_llm={
                "_model_provider": "string",
                "_model_name": "string",
                "_model_parameters": {"foo": "string"},
            },
            db_connection_id="string",
            golden_records=["string", "string", "string"],
            metadata={},
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncDataherald) -> None:
        response = await client.finetunings.with_raw_response.create(
            base_llm={},
            db_connection_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = response.parse()
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncDataherald) -> None:
        finetuning = await client.finetunings.retrieve(
            "string",
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncDataherald) -> None:
        response = await client.finetunings.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = response.parse()
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])
