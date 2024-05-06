# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import (
    TableDescriptionResponse,
    TableDescriptionListResponse,
    TableDescriptionSyncSchemasResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTableDescriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        table_description = client.table_descriptions.retrieve(
            "string",
        )
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.table_descriptions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.table_descriptions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table_description = response.parse()
            assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.table_descriptions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Dataherald) -> None:
        table_description = client.table_descriptions.update(
            "string",
        )
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Dataherald) -> None:
        table_description = client.table_descriptions.update(
            "string",
            columns=[
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "foreign_key": {},
                },
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "foreign_key": {},
                },
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "foreign_key": {},
                },
            ],
            description="string",
            examples=[{}, {}, {}],
            metadata={},
        )
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Dataherald) -> None:
        response = client.table_descriptions.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Dataherald) -> None:
        with client.table_descriptions.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table_description = response.parse()
            assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.table_descriptions.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        table_description = client.table_descriptions.list(
            db_connection_id="string",
        )
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dataherald) -> None:
        table_description = client.table_descriptions.list(
            db_connection_id="string",
            table_name="string",
        )
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.table_descriptions.with_raw_response.list(
            db_connection_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dataherald) -> None:
        with client.table_descriptions.with_streaming_response.list(
            db_connection_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table_description = response.parse()
            assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_sync_schemas(self, client: Dataherald) -> None:
        table_description = client.table_descriptions.sync_schemas(
            body=[{"db_connection_id": "string"}, {"db_connection_id": "string"}, {"db_connection_id": "string"}],
        )
        assert_matches_type(TableDescriptionSyncSchemasResponse, table_description, path=["response"])

    @parametrize
    def test_raw_response_sync_schemas(self, client: Dataherald) -> None:
        response = client.table_descriptions.with_raw_response.sync_schemas(
            body=[{"db_connection_id": "string"}, {"db_connection_id": "string"}, {"db_connection_id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(TableDescriptionSyncSchemasResponse, table_description, path=["response"])

    @parametrize
    def test_streaming_response_sync_schemas(self, client: Dataherald) -> None:
        with client.table_descriptions.with_streaming_response.sync_schemas(
            body=[{"db_connection_id": "string"}, {"db_connection_id": "string"}, {"db_connection_id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table_description = response.parse()
            assert_matches_type(TableDescriptionSyncSchemasResponse, table_description, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTableDescriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDataherald) -> None:
        table_description = await async_client.table_descriptions.retrieve(
            "string",
        )
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDataherald) -> None:
        response = await async_client.table_descriptions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = await response.parse()
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDataherald) -> None:
        async with async_client.table_descriptions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table_description = await response.parse()
            assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.table_descriptions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDataherald) -> None:
        table_description = await async_client.table_descriptions.update(
            "string",
        )
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDataherald) -> None:
        table_description = await async_client.table_descriptions.update(
            "string",
            columns=[
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "foreign_key": {},
                },
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "foreign_key": {},
                },
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "foreign_key": {},
                },
            ],
            description="string",
            examples=[{}, {}, {}],
            metadata={},
        )
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDataherald) -> None:
        response = await async_client.table_descriptions.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = await response.parse()
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDataherald) -> None:
        async with async_client.table_descriptions.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table_description = await response.parse()
            assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.table_descriptions.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDataherald) -> None:
        table_description = await async_client.table_descriptions.list(
            db_connection_id="string",
        )
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDataherald) -> None:
        table_description = await async_client.table_descriptions.list(
            db_connection_id="string",
            table_name="string",
        )
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDataherald) -> None:
        response = await async_client.table_descriptions.with_raw_response.list(
            db_connection_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = await response.parse()
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDataherald) -> None:
        async with async_client.table_descriptions.with_streaming_response.list(
            db_connection_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table_description = await response.parse()
            assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_sync_schemas(self, async_client: AsyncDataherald) -> None:
        table_description = await async_client.table_descriptions.sync_schemas(
            body=[{"db_connection_id": "string"}, {"db_connection_id": "string"}, {"db_connection_id": "string"}],
        )
        assert_matches_type(TableDescriptionSyncSchemasResponse, table_description, path=["response"])

    @parametrize
    async def test_raw_response_sync_schemas(self, async_client: AsyncDataherald) -> None:
        response = await async_client.table_descriptions.with_raw_response.sync_schemas(
            body=[{"db_connection_id": "string"}, {"db_connection_id": "string"}, {"db_connection_id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = await response.parse()
        assert_matches_type(TableDescriptionSyncSchemasResponse, table_description, path=["response"])

    @parametrize
    async def test_streaming_response_sync_schemas(self, async_client: AsyncDataherald) -> None:
        async with async_client.table_descriptions.with_streaming_response.sync_schemas(
            body=[{"db_connection_id": "string"}, {"db_connection_id": "string"}, {"db_connection_id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table_description = await response.parse()
            assert_matches_type(TableDescriptionSyncSchemasResponse, table_description, path=["response"])

        assert cast(Any, response.is_closed) is True
