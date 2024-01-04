# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import (
    GoldenSqlListResponse,
    GoldenSqlUploadResponse,
)
from dataherald._client import Dataherald, AsyncDataherald
from dataherald.types.shared import GoldenSqlResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestGoldenSqls:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        golden_sql = client.golden_sqls.retrieve(
            "string",
        )
        assert_matches_type(GoldenSqlResponse, golden_sql, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.golden_sqls.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(GoldenSqlResponse, golden_sql, path=["response"])

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        golden_sql = client.golden_sqls.list()
        assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dataherald) -> None:
        golden_sql = client.golden_sqls.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.golden_sqls.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

    @parametrize
    def test_method_delete(self, client: Dataherald) -> None:
        golden_sql = client.golden_sqls.delete(
            "string",
        )
        assert_matches_type(object, golden_sql, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Dataherald) -> None:
        response = client.golden_sqls.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(object, golden_sql, path=["response"])

    @parametrize
    def test_method_upload(self, client: Dataherald) -> None:
        golden_sql = client.golden_sqls.upload(
            body=[
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
            ],
        )
        assert_matches_type(GoldenSqlUploadResponse, golden_sql, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Dataherald) -> None:
        response = client.golden_sqls.with_raw_response.upload(
            body=[
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
            ],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(GoldenSqlUploadResponse, golden_sql, path=["response"])


class TestAsyncGoldenSqls:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncDataherald) -> None:
        golden_sql = await client.golden_sqls.retrieve(
            "string",
        )
        assert_matches_type(GoldenSqlResponse, golden_sql, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncDataherald) -> None:
        response = await client.golden_sqls.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(GoldenSqlResponse, golden_sql, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncDataherald) -> None:
        golden_sql = await client.golden_sqls.list()
        assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncDataherald) -> None:
        golden_sql = await client.golden_sqls.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncDataherald) -> None:
        response = await client.golden_sqls.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncDataherald) -> None:
        golden_sql = await client.golden_sqls.delete(
            "string",
        )
        assert_matches_type(object, golden_sql, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncDataherald) -> None:
        response = await client.golden_sqls.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(object, golden_sql, path=["response"])

    @parametrize
    async def test_method_upload(self, client: AsyncDataherald) -> None:
        golden_sql = await client.golden_sqls.upload(
            body=[
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
            ],
        )
        assert_matches_type(GoldenSqlUploadResponse, golden_sql, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, client: AsyncDataherald) -> None:
        response = await client.golden_sqls.with_raw_response.upload(
            body=[
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
                {
                    "db_connection_id": "string",
                    "prompt_text": "string",
                    "sql": "string",
                },
            ],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(GoldenSqlUploadResponse, golden_sql, path=["response"])
