# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import (
    SqlGenerationListResponse,
    SqlGenerationExecuteResponse,
)
from dataherald.types.shared import SqlGenerationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSqlGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dataherald) -> None:
        with client.sql_generations.with_streaming_response.create(
            prompt={
                "text": "string",
                "db_connection_id": "string",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = response.parse()
            assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.sql_generations.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = response.parse()
            assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sql_generations.with_raw_response.retrieve(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dataherald) -> None:
        with client.sql_generations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = response.parse()
            assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_execute(self, client: Dataherald) -> None:
        sql_generation = client.sql_generations.execute(
            "string",
        )
        assert_matches_type(SqlGenerationExecuteResponse, sql_generation, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Dataherald) -> None:
        sql_generation = client.sql_generations.execute(
            "string",
            max_rows=0,
        )
        assert_matches_type(SqlGenerationExecuteResponse, sql_generation, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Dataherald) -> None:
        response = client.sql_generations.with_raw_response.execute(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationExecuteResponse, sql_generation, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Dataherald) -> None:
        with client.sql_generations.with_streaming_response.execute(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = response.parse()
            assert_matches_type(SqlGenerationExecuteResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sql_generations.with_raw_response.execute(
                "",
            )


class TestAsyncSqlGenerations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.sql_generations.create(
            prompt={
                "text": "string",
                "db_connection_id": "string",
            },
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.sql_generations.create(
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
    async def test_raw_response_create(self, async_client: AsyncDataherald) -> None:
        response = await async_client.sql_generations.with_raw_response.create(
            prompt={
                "text": "string",
                "db_connection_id": "string",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = await response.parse()
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDataherald) -> None:
        async with async_client.sql_generations.with_streaming_response.create(
            prompt={
                "text": "string",
                "db_connection_id": "string",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = await response.parse()
            assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.sql_generations.retrieve(
            "string",
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDataherald) -> None:
        response = await async_client.sql_generations.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = await response.parse()
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDataherald) -> None:
        async with async_client.sql_generations.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = await response.parse()
            assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sql_generations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.sql_generations.list()
        assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.sql_generations.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDataherald) -> None:
        response = await async_client.sql_generations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = await response.parse()
        assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDataherald) -> None:
        async with async_client.sql_generations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = await response.parse()
            assert_matches_type(SqlGenerationListResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_execute(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.sql_generations.execute(
            "string",
        )
        assert_matches_type(SqlGenerationExecuteResponse, sql_generation, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.sql_generations.execute(
            "string",
            max_rows=0,
        )
        assert_matches_type(SqlGenerationExecuteResponse, sql_generation, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncDataherald) -> None:
        response = await async_client.sql_generations.with_raw_response.execute(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = await response.parse()
        assert_matches_type(SqlGenerationExecuteResponse, sql_generation, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncDataherald) -> None:
        async with async_client.sql_generations.with_streaming_response.execute(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = await response.parse()
            assert_matches_type(SqlGenerationExecuteResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sql_generations.with_raw_response.execute(
                "",
            )
