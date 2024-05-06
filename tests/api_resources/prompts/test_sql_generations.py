# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types.shared import NlGenerationResponse, SqlGenerationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSqlGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Dataherald) -> None:
        sql_generation = client.prompts.sql_generations.create(
            "string",
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dataherald) -> None:
        sql_generation = client.prompts.sql_generations.create(
            "string",
            evaluate=True,
            finetuning_id="string",
            low_latency_mode=True,
            metadata={},
            sql="string",
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dataherald) -> None:
        response = client.prompts.sql_generations.with_raw_response.create(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dataherald) -> None:
        with client.prompts.sql_generations.with_streaming_response.create(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = response.parse()
            assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.sql_generations.with_raw_response.create(
                "",
            )

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        sql_generation = client.prompts.sql_generations.retrieve(
            "string",
        )
        assert_matches_type(object, sql_generation, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Dataherald) -> None:
        sql_generation = client.prompts.sql_generations.retrieve(
            "string",
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(object, sql_generation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.prompts.sql_generations.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(object, sql_generation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.prompts.sql_generations.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = response.parse()
            assert_matches_type(object, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.sql_generations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_nl_generations(self, client: Dataherald) -> None:
        sql_generation = client.prompts.sql_generations.nl_generations(
            "string",
            sql_generation={},
        )
        assert_matches_type(NlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_method_nl_generations_with_all_params(self, client: Dataherald) -> None:
        sql_generation = client.prompts.sql_generations.nl_generations(
            "string",
            sql_generation={
                "finetuning_id": "string",
                "low_latency_mode": True,
                "evaluate": True,
                "sql": "string",
                "metadata": {},
            },
            max_rows=0,
            metadata={},
        )
        assert_matches_type(NlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_raw_response_nl_generations(self, client: Dataherald) -> None:
        response = client.prompts.sql_generations.with_raw_response.nl_generations(
            "string",
            sql_generation={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = response.parse()
        assert_matches_type(NlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    def test_streaming_response_nl_generations(self, client: Dataherald) -> None:
        with client.prompts.sql_generations.with_streaming_response.nl_generations(
            "string",
            sql_generation={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = response.parse()
            assert_matches_type(NlGenerationResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_nl_generations(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.sql_generations.with_raw_response.nl_generations(
                "",
                sql_generation={},
            )


class TestAsyncSqlGenerations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.prompts.sql_generations.create(
            "string",
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.prompts.sql_generations.create(
            "string",
            evaluate=True,
            finetuning_id="string",
            low_latency_mode=True,
            metadata={},
            sql="string",
        )
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDataherald) -> None:
        response = await async_client.prompts.sql_generations.with_raw_response.create(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = await response.parse()
        assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDataherald) -> None:
        async with async_client.prompts.sql_generations.with_streaming_response.create(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = await response.parse()
            assert_matches_type(SqlGenerationResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.sql_generations.with_raw_response.create(
                "",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.prompts.sql_generations.retrieve(
            "string",
        )
        assert_matches_type(object, sql_generation, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.prompts.sql_generations.retrieve(
            "string",
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(object, sql_generation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDataherald) -> None:
        response = await async_client.prompts.sql_generations.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = await response.parse()
        assert_matches_type(object, sql_generation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDataherald) -> None:
        async with async_client.prompts.sql_generations.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = await response.parse()
            assert_matches_type(object, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.sql_generations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_nl_generations(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.prompts.sql_generations.nl_generations(
            "string",
            sql_generation={},
        )
        assert_matches_type(NlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_method_nl_generations_with_all_params(self, async_client: AsyncDataherald) -> None:
        sql_generation = await async_client.prompts.sql_generations.nl_generations(
            "string",
            sql_generation={
                "finetuning_id": "string",
                "low_latency_mode": True,
                "evaluate": True,
                "sql": "string",
                "metadata": {},
            },
            max_rows=0,
            metadata={},
        )
        assert_matches_type(NlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_raw_response_nl_generations(self, async_client: AsyncDataherald) -> None:
        response = await async_client.prompts.sql_generations.with_raw_response.nl_generations(
            "string",
            sql_generation={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sql_generation = await response.parse()
        assert_matches_type(NlGenerationResponse, sql_generation, path=["response"])

    @parametrize
    async def test_streaming_response_nl_generations(self, async_client: AsyncDataherald) -> None:
        async with async_client.prompts.sql_generations.with_streaming_response.nl_generations(
            "string",
            sql_generation={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sql_generation = await response.parse()
            assert_matches_type(NlGenerationResponse, sql_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_nl_generations(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.sql_generations.with_raw_response.nl_generations(
                "",
                sql_generation={},
            )
