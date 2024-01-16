# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import (
    GenerationResponse,
    GenerationListResponse,
)
from dataherald._client import Dataherald, AsyncDataherald
from dataherald.types.shared import NlGenerationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestGenerations:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Dataherald) -> None:
        generation = client.generations.create(
            "string",
        )
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dataherald) -> None:
        response = client.generations.with_raw_response.create(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dataherald) -> None:
        with client.generations.with_streaming_response.create(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generations.with_raw_response.create(
                "",
            )

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        generation = client.generations.retrieve(
            "string",
        )
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.generations.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.generations.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Dataherald) -> None:
        generation = client.generations.update(
            "string",
        )
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Dataherald) -> None:
        generation = client.generations.update(
            "string",
            generation_status="INITIALIZED",
            message="string",
        )
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Dataherald) -> None:
        response = client.generations.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Dataherald) -> None:
        with client.generations.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generations.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        generation = client.generations.list()
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dataherald) -> None:
        generation = client.generations.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.generations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dataherald) -> None:
        with client.generations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationListResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_nl_generation(self, client: Dataherald) -> None:
        generation = client.generations.nl_generation(
            "string",
        )
        assert_matches_type(NlGenerationResponse, generation, path=["response"])

    @parametrize
    def test_raw_response_nl_generation(self, client: Dataherald) -> None:
        response = client.generations.with_raw_response.nl_generation(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(NlGenerationResponse, generation, path=["response"])

    @parametrize
    def test_streaming_response_nl_generation(self, client: Dataherald) -> None:
        with client.generations.with_streaming_response.nl_generation(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(NlGenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_nl_generation(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generations.with_raw_response.nl_generation(
                "",
            )

    @parametrize
    def test_method_sql_generation(self, client: Dataherald) -> None:
        generation = client.generations.sql_generation(
            "string",
            sql="string",
        )
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    def test_raw_response_sql_generation(self, client: Dataherald) -> None:
        response = client.generations.with_raw_response.sql_generation(
            "string",
            sql="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    def test_streaming_response_sql_generation(self, client: Dataherald) -> None:
        with client.generations.with_streaming_response.sql_generation(
            "string",
            sql="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sql_generation(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generations.with_raw_response.sql_generation(
                "",
                sql="string",
            )


class TestAsyncGenerations:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncDataherald) -> None:
        generation = await client.generations.create(
            "string",
        )
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncDataherald) -> None:
        response = await client.generations.with_raw_response.create(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncDataherald) -> None:
        async with client.generations.with_streaming_response.create(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await client.generations.with_raw_response.create(
                "",
            )

    @parametrize
    async def test_method_retrieve(self, client: AsyncDataherald) -> None:
        generation = await client.generations.retrieve(
            "string",
        )
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncDataherald) -> None:
        response = await client.generations.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncDataherald) -> None:
        async with client.generations.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await client.generations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, client: AsyncDataherald) -> None:
        generation = await client.generations.update(
            "string",
        )
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncDataherald) -> None:
        generation = await client.generations.update(
            "string",
            generation_status="INITIALIZED",
            message="string",
        )
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncDataherald) -> None:
        response = await client.generations.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncDataherald) -> None:
        async with client.generations.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await client.generations.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncDataherald) -> None:
        generation = await client.generations.list()
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncDataherald) -> None:
        generation = await client.generations.list(
            ascend=True,
            order="string",
            page=0,
            page_size=0,
        )
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncDataherald) -> None:
        response = await client.generations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationListResponse, generation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncDataherald) -> None:
        async with client.generations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationListResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_nl_generation(self, client: AsyncDataherald) -> None:
        generation = await client.generations.nl_generation(
            "string",
        )
        assert_matches_type(NlGenerationResponse, generation, path=["response"])

    @parametrize
    async def test_raw_response_nl_generation(self, client: AsyncDataherald) -> None:
        response = await client.generations.with_raw_response.nl_generation(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(NlGenerationResponse, generation, path=["response"])

    @parametrize
    async def test_streaming_response_nl_generation(self, client: AsyncDataherald) -> None:
        async with client.generations.with_streaming_response.nl_generation(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(NlGenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_nl_generation(self, client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await client.generations.with_raw_response.nl_generation(
                "",
            )

    @parametrize
    async def test_method_sql_generation(self, client: AsyncDataherald) -> None:
        generation = await client.generations.sql_generation(
            "string",
            sql="string",
        )
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    async def test_raw_response_sql_generation(self, client: AsyncDataherald) -> None:
        response = await client.generations.with_raw_response.sql_generation(
            "string",
            sql="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationResponse, generation, path=["response"])

    @parametrize
    async def test_streaming_response_sql_generation(self, client: AsyncDataherald) -> None:
        async with client.generations.with_streaming_response.sql_generation(
            "string",
            sql="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sql_generation(self, client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await client.generations.with_raw_response.sql_generation(
                "",
                sql="string",
            )
