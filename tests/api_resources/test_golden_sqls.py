# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import (
    GoldenSqlListResponse,
    GoldenSqlUploadResponse,
)
from dataherald.types.shared import GoldenSqlResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGoldenSqls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(GoldenSqlResponse, golden_sql, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.golden_sqls.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            golden_sql = response.parse()
            assert_matches_type(GoldenSqlResponse, golden_sql, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.golden_sqls.with_raw_response.retrieve(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dataherald) -> None:
        with client.golden_sqls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            golden_sql = response.parse()
            assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(object, golden_sql, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Dataherald) -> None:
        with client.golden_sqls.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            golden_sql = response.parse()
            assert_matches_type(object, golden_sql, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.golden_sqls.with_raw_response.delete(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = response.parse()
        assert_matches_type(GoldenSqlUploadResponse, golden_sql, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Dataherald) -> None:
        with client.golden_sqls.with_streaming_response.upload(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            golden_sql = response.parse()
            assert_matches_type(GoldenSqlUploadResponse, golden_sql, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGoldenSqls:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDataherald) -> None:
        golden_sql = await async_client.golden_sqls.retrieve(
            "string",
        )
        assert_matches_type(GoldenSqlResponse, golden_sql, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDataherald) -> None:
        response = await async_client.golden_sqls.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = await response.parse()
        assert_matches_type(GoldenSqlResponse, golden_sql, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDataherald) -> None:
        async with async_client.golden_sqls.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            golden_sql = await response.parse()
            assert_matches_type(GoldenSqlResponse, golden_sql, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.golden_sqls.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDataherald) -> None:
        golden_sql = await async_client.golden_sqls.list()
        assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDataherald) -> None:
        golden_sql = await async_client.golden_sqls.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDataherald) -> None:
        response = await async_client.golden_sqls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = await response.parse()
        assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDataherald) -> None:
        async with async_client.golden_sqls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            golden_sql = await response.parse()
            assert_matches_type(GoldenSqlListResponse, golden_sql, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDataherald) -> None:
        golden_sql = await async_client.golden_sqls.delete(
            "string",
        )
        assert_matches_type(object, golden_sql, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDataherald) -> None:
        response = await async_client.golden_sqls.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = await response.parse()
        assert_matches_type(object, golden_sql, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDataherald) -> None:
        async with async_client.golden_sqls.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            golden_sql = await response.parse()
            assert_matches_type(object, golden_sql, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.golden_sqls.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncDataherald) -> None:
        golden_sql = await async_client.golden_sqls.upload(
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
    async def test_raw_response_upload(self, async_client: AsyncDataherald) -> None:
        response = await async_client.golden_sqls.with_raw_response.upload(
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        golden_sql = await response.parse()
        assert_matches_type(GoldenSqlUploadResponse, golden_sql, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncDataherald) -> None:
        async with async_client.golden_sqls.with_streaming_response.upload(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            golden_sql = await response.parse()
            assert_matches_type(GoldenSqlUploadResponse, golden_sql, path=["response"])

        assert cast(Any, response.is_closed) is True
