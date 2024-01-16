# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import NlGenerationListResponse
from dataherald._client import Dataherald, AsyncDataherald
from dataherald.types.shared import NlGenerationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestNlGenerations:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Dataherald) -> None:
        nl_generation = client.nl_generations.create(
            sql_generation={
                "prompt": {
                    "text": "string",
                    "db_connection_id": "string",
                }
            },
        )
        assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dataherald) -> None:
        nl_generation = client.nl_generations.create(
            sql_generation={
                "finetuning_id": "string",
                "evaluate": True,
                "sql": "string",
                "metadata": {},
                "prompt": {
                    "text": "string",
                    "db_connection_id": "string",
                    "metadata": {},
                },
            },
            max_rows=0,
            metadata={},
        )
        assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dataherald) -> None:
        response = client.nl_generations.with_raw_response.create(
            sql_generation={
                "prompt": {
                    "text": "string",
                    "db_connection_id": "string",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nl_generation = response.parse()
        assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dataherald) -> None:
        with client.nl_generations.with_streaming_response.create(
            sql_generation={
                "prompt": {
                    "text": "string",
                    "db_connection_id": "string",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nl_generation = response.parse()
            assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        nl_generation = client.nl_generations.retrieve(
            "string",
        )
        assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.nl_generations.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nl_generation = response.parse()
        assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.nl_generations.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nl_generation = response.parse()
            assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.nl_generations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        nl_generation = client.nl_generations.list()
        assert_matches_type(NlGenerationListResponse, nl_generation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dataherald) -> None:
        nl_generation = client.nl_generations.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(NlGenerationListResponse, nl_generation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.nl_generations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nl_generation = response.parse()
        assert_matches_type(NlGenerationListResponse, nl_generation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dataherald) -> None:
        with client.nl_generations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nl_generation = response.parse()
            assert_matches_type(NlGenerationListResponse, nl_generation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNlGenerations:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncDataherald) -> None:
        nl_generation = await client.nl_generations.create(
            sql_generation={
                "prompt": {
                    "text": "string",
                    "db_connection_id": "string",
                }
            },
        )
        assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncDataherald) -> None:
        nl_generation = await client.nl_generations.create(
            sql_generation={
                "finetuning_id": "string",
                "evaluate": True,
                "sql": "string",
                "metadata": {},
                "prompt": {
                    "text": "string",
                    "db_connection_id": "string",
                    "metadata": {},
                },
            },
            max_rows=0,
            metadata={},
        )
        assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncDataherald) -> None:
        response = await client.nl_generations.with_raw_response.create(
            sql_generation={
                "prompt": {
                    "text": "string",
                    "db_connection_id": "string",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nl_generation = await response.parse()
        assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncDataherald) -> None:
        async with client.nl_generations.with_streaming_response.create(
            sql_generation={
                "prompt": {
                    "text": "string",
                    "db_connection_id": "string",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nl_generation = await response.parse()
            assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncDataherald) -> None:
        nl_generation = await client.nl_generations.retrieve(
            "string",
        )
        assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncDataherald) -> None:
        response = await client.nl_generations.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nl_generation = await response.parse()
        assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncDataherald) -> None:
        async with client.nl_generations.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nl_generation = await response.parse()
            assert_matches_type(NlGenerationResponse, nl_generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await client.nl_generations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncDataherald) -> None:
        nl_generation = await client.nl_generations.list()
        assert_matches_type(NlGenerationListResponse, nl_generation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncDataherald) -> None:
        nl_generation = await client.nl_generations.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(NlGenerationListResponse, nl_generation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncDataherald) -> None:
        response = await client.nl_generations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nl_generation = await response.parse()
        assert_matches_type(NlGenerationListResponse, nl_generation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncDataherald) -> None:
        async with client.nl_generations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nl_generation = await response.parse()
            assert_matches_type(NlGenerationListResponse, nl_generation, path=["response"])

        assert cast(Any, response.is_closed) is True
