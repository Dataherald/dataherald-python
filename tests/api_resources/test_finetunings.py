# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import (
    FinetuningResponse,
    FinetuningListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFinetunings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Dataherald) -> None:
        finetuning = client.finetunings.create(
            db_connection_id="string",
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dataherald) -> None:
        finetuning = client.finetunings.create(
            db_connection_id="string",
            alias="string",
            base_llm={
                "model_provider": "string",
                "model_name": "string",
                "model_parameters": {"foo": "string"},
            },
            golden_sqls=["string", "string", "string"],
            metadata={},
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dataherald) -> None:
        response = client.finetunings.with_raw_response.create(
            db_connection_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = response.parse()
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dataherald) -> None:
        with client.finetunings.with_streaming_response.create(
            db_connection_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetuning = response.parse()
            assert_matches_type(FinetuningResponse, finetuning, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = response.parse()
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.finetunings.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetuning = response.parse()
            assert_matches_type(FinetuningResponse, finetuning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.finetunings.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        finetuning = client.finetunings.list(
            db_connection_id="string",
        )
        assert_matches_type(FinetuningListResponse, finetuning, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.finetunings.with_raw_response.list(
            db_connection_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = response.parse()
        assert_matches_type(FinetuningListResponse, finetuning, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dataherald) -> None:
        with client.finetunings.with_streaming_response.list(
            db_connection_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetuning = response.parse()
            assert_matches_type(FinetuningListResponse, finetuning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Dataherald) -> None:
        finetuning = client.finetunings.cancel(
            "string",
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Dataherald) -> None:
        response = client.finetunings.with_raw_response.cancel(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = response.parse()
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Dataherald) -> None:
        with client.finetunings.with_streaming_response.cancel(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetuning = response.parse()
            assert_matches_type(FinetuningResponse, finetuning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.finetunings.with_raw_response.cancel(
                "",
            )


class TestAsyncFinetunings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDataherald) -> None:
        finetuning = await async_client.finetunings.create(
            db_connection_id="string",
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDataherald) -> None:
        finetuning = await async_client.finetunings.create(
            db_connection_id="string",
            alias="string",
            base_llm={
                "model_provider": "string",
                "model_name": "string",
                "model_parameters": {"foo": "string"},
            },
            golden_sqls=["string", "string", "string"],
            metadata={},
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDataherald) -> None:
        response = await async_client.finetunings.with_raw_response.create(
            db_connection_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = await response.parse()
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDataherald) -> None:
        async with async_client.finetunings.with_streaming_response.create(
            db_connection_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetuning = await response.parse()
            assert_matches_type(FinetuningResponse, finetuning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDataherald) -> None:
        finetuning = await async_client.finetunings.retrieve(
            "string",
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDataherald) -> None:
        response = await async_client.finetunings.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = await response.parse()
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDataherald) -> None:
        async with async_client.finetunings.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetuning = await response.parse()
            assert_matches_type(FinetuningResponse, finetuning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.finetunings.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDataherald) -> None:
        finetuning = await async_client.finetunings.list(
            db_connection_id="string",
        )
        assert_matches_type(FinetuningListResponse, finetuning, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDataherald) -> None:
        response = await async_client.finetunings.with_raw_response.list(
            db_connection_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = await response.parse()
        assert_matches_type(FinetuningListResponse, finetuning, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDataherald) -> None:
        async with async_client.finetunings.with_streaming_response.list(
            db_connection_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetuning = await response.parse()
            assert_matches_type(FinetuningListResponse, finetuning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncDataherald) -> None:
        finetuning = await async_client.finetunings.cancel(
            "string",
        )
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncDataherald) -> None:
        response = await async_client.finetunings.with_raw_response.cancel(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetuning = await response.parse()
        assert_matches_type(FinetuningResponse, finetuning, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncDataherald) -> None:
        async with async_client.finetunings.with_streaming_response.cancel(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetuning = await response.parse()
            assert_matches_type(FinetuningResponse, finetuning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.finetunings.with_raw_response.cancel(
                "",
            )
