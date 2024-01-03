# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import (
    DBConnectionResponse,
    DatabaseConnectionListResponse,
)
from dataherald._client import Dataherald, AsyncDataherald

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestDatabaseConnections:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Dataherald) -> None:
        database_connection = client.database_connections.create(
            db_connection_request_json="string",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dataherald) -> None:
        database_connection = client.database_connections.create(
            db_connection_request_json="string",
            file=b"raw file contents",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dataherald) -> None:
        response = client.database_connections.with_raw_response.create(
            db_connection_request_json="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        database_connection = client.database_connections.retrieve(
            "string",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.database_connections.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_method_update(self, client: Dataherald) -> None:
        database_connection = client.database_connections.update(
            "string",
            db_connection_request_json="string",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Dataherald) -> None:
        database_connection = client.database_connections.update(
            "string",
            db_connection_request_json="string",
            file=b"raw file contents",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Dataherald) -> None:
        response = client.database_connections.with_raw_response.update(
            "string",
            db_connection_request_json="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        database_connection = client.database_connections.list()
        assert_matches_type(DatabaseConnectionListResponse, database_connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.database_connections.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DatabaseConnectionListResponse, database_connection, path=["response"])


class TestAsyncDatabaseConnections:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncDataherald) -> None:
        database_connection = await client.database_connections.create(
            db_connection_request_json="string",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncDataherald) -> None:
        database_connection = await client.database_connections.create(
            db_connection_request_json="string",
            file=b"raw file contents",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncDataherald) -> None:
        response = await client.database_connections.with_raw_response.create(
            db_connection_request_json="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncDataherald) -> None:
        database_connection = await client.database_connections.retrieve(
            "string",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncDataherald) -> None:
        response = await client.database_connections.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncDataherald) -> None:
        database_connection = await client.database_connections.update(
            "string",
            db_connection_request_json="string",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncDataherald) -> None:
        database_connection = await client.database_connections.update(
            "string",
            db_connection_request_json="string",
            file=b"raw file contents",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncDataherald) -> None:
        response = await client.database_connections.with_raw_response.update(
            "string",
            db_connection_request_json="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncDataherald) -> None:
        database_connection = await client.database_connections.list()
        assert_matches_type(DatabaseConnectionListResponse, database_connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncDataherald) -> None:
        response = await client.database_connections.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DatabaseConnectionListResponse, database_connection, path=["response"])
