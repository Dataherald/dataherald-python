# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import SqlGenerationListResponse
from dataherald._client import Dataherald, AsyncDataherald
from dataherald.types.shared import SqlGenerationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestSqlGenerations:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Dataherald) -> None:
        sql_generation = client.sql_generations.create(
            prompt={
                "text": "string",
                "db_connection_id": "string",
            },
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dataherald) -> None:
        sql_generation = client.sql_generations.create(
            prompt={
                "text": "string",
                "db_connection_id": "string",
                "metadata": {},
            },
            evaluate=True,
            finetuning_id="string",
            metadata={},
            sql="string",
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dataherald) -> None:
        response = client.sql_generations.with_raw_response.create(
            prompt={
                "text": "string",
                "db_connection_id": "string",
            },
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        sql_generation = client.sql_generations.retrieve(
            "string",
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.sql_generations.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        sql_generation = client.sql_generations.list()
        assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dataherald) -> None:
        sql_generation = client.sql_generations.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.sql_generations.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])


class TestAsyncSqlGenerations:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncDataherald) -> None:
        sql_generation = await client.sql_generations.create(
            prompt={
                "text": "string",
                "db_connection_id": "string",
            },
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncDataherald) -> None:
        sql_generation = await client.sql_generations.create(
            prompt={
                "text": "string",
                "db_connection_id": "string",
                "metadata": {},
            },
            evaluate=True,
            finetuning_id="string",
            metadata={},
            sql="string",
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncDataherald) -> None:
        response = await client.sql_generations.with_raw_response.create(
            prompt={
                "text": "string",
                "db_connection_id": "string",
            },
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncDataherald) -> None:
        sql_generation = await client.sql_generations.retrieve(
            "string",
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncDataherald) -> None:
        response = await client.sql_generations.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncDataherald) -> None:
        sql_generation = await client.sql_generations.list()
        assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncDataherald) -> None:
        sql_generation = await client.sql_generations.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncDataherald) -> None:
        response = await client.sql_generations.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])
