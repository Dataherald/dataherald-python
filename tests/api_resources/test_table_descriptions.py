# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import TableDescriptionResponse, TableDescriptionListResponse
from dataherald._client import Dataherald, AsyncDataherald

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestTableDescriptions:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

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
                    "forengin_key": {},
                },
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "forengin_key": {},
                },
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "forengin_key": {},
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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        table_description = client.table_descriptions.list()
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dataherald) -> None:
        table_description = client.table_descriptions.list(
            table_name="string",
        )
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.table_descriptions.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    def test_method_sync_schemas(self, client: Dataherald) -> None:
        table_description = client.table_descriptions.sync_schemas(
            db_connection_id="string",
        )
        assert_matches_type(object, table_description, path=["response"])

    @parametrize
    def test_method_sync_schemas_with_all_params(self, client: Dataherald) -> None:
        table_description = client.table_descriptions.sync_schemas(
            db_connection_id="string",
            table_names=["string", "string", "string"],
        )
        assert_matches_type(object, table_description, path=["response"])

    @parametrize
    def test_raw_response_sync_schemas(self, client: Dataherald) -> None:
        response = client.table_descriptions.with_raw_response.sync_schemas(
            db_connection_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(object, table_description, path=["response"])


class TestAsyncTableDescriptions:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncDataherald) -> None:
        table_description = await client.table_descriptions.retrieve(
            "string",
        )
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncDataherald) -> None:
        response = await client.table_descriptions.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncDataherald) -> None:
        table_description = await client.table_descriptions.update(
            "string",
        )
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncDataherald) -> None:
        table_description = await client.table_descriptions.update(
            "string",
            columns=[
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "forengin_key": {},
                },
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "forengin_key": {},
                },
                {
                    "name": "string",
                    "description": "string",
                    "is_primary_key": True,
                    "data_type": "string",
                    "low_cardinality": True,
                    "categories": ["string", "string", "string"],
                    "forengin_key": {},
                },
            ],
            description="string",
            examples=[{}, {}, {}],
            metadata={},
        )
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncDataherald) -> None:
        response = await client.table_descriptions.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(TableDescriptionResponse, table_description, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncDataherald) -> None:
        table_description = await client.table_descriptions.list()
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncDataherald) -> None:
        table_description = await client.table_descriptions.list(
            table_name="string",
        )
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncDataherald) -> None:
        response = await client.table_descriptions.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(TableDescriptionListResponse, table_description, path=["response"])

    @parametrize
    async def test_method_sync_schemas(self, client: AsyncDataherald) -> None:
        table_description = await client.table_descriptions.sync_schemas(
            db_connection_id="string",
        )
        assert_matches_type(object, table_description, path=["response"])

    @parametrize
    async def test_method_sync_schemas_with_all_params(self, client: AsyncDataherald) -> None:
        table_description = await client.table_descriptions.sync_schemas(
            db_connection_id="string",
            table_names=["string", "string", "string"],
        )
        assert_matches_type(object, table_description, path=["response"])

    @parametrize
    async def test_raw_response_sync_schemas(self, client: AsyncDataherald) -> None:
        response = await client.table_descriptions.with_raw_response.sync_schemas(
            db_connection_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table_description = response.parse()
        assert_matches_type(object, table_description, path=["response"])
