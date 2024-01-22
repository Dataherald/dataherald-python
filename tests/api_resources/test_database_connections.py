# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types import (
    DBConnectionResponse,
    DatabaseConnectionListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatabaseConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Dataherald) -> None:
        database_connection = client.database_connections.create()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dataherald) -> None:
        database_connection = client.database_connections.create(
            alias="string",
            connection_uri="string",
            credential_file_content={},
            llm_api_key="string",
            metadata={},
            ssh_settings={
                "db_name": "string",
                "host": "string",
                "username": "string",
                "password": "string",
                "remote_host": "string",
                "remote_db_name": "string",
                "remote_db_password": "string",
                "private_key_password": "string",
                "db_driver": "string",
            },
            use_ssh=True,
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dataherald) -> None:
        response = client.database_connections.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dataherald) -> None:
        with client.database_connections.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database_connection = response.parse()
            assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.database_connections.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database_connection = response.parse()
            assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.database_connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Dataherald) -> None:
        database_connection = client.database_connections.update(
            "string",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Dataherald) -> None:
        database_connection = client.database_connections.update(
            "string",
            alias="string",
            connection_uri="string",
            credential_file_content={},
            llm_api_key="string",
            metadata={},
            ssh_settings={
                "db_name": "string",
                "host": "string",
                "username": "string",
                "password": "string",
                "remote_host": "string",
                "remote_db_name": "string",
                "remote_db_password": "string",
                "private_key_password": "string",
                "db_driver": "string",
            },
            use_ssh=True,
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Dataherald) -> None:
        response = client.database_connections.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Dataherald) -> None:
        with client.database_connections.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database_connection = response.parse()
            assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Dataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.database_connections.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        database_connection = client.database_connections.list()
        assert_matches_type(DatabaseConnectionListResponse, database_connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.database_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = response.parse()
        assert_matches_type(DatabaseConnectionListResponse, database_connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dataherald) -> None:
        with client.database_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database_connection = response.parse()
            assert_matches_type(DatabaseConnectionListResponse, database_connection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatabaseConnections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDataherald) -> None:
        database_connection = await async_client.database_connections.create()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDataherald) -> None:
        database_connection = await async_client.database_connections.create(
            alias="string",
            connection_uri="string",
            credential_file_content={},
            llm_api_key="string",
            metadata={},
            ssh_settings={
                "db_name": "string",
                "host": "string",
                "username": "string",
                "password": "string",
                "remote_host": "string",
                "remote_db_name": "string",
                "remote_db_password": "string",
                "private_key_password": "string",
                "db_driver": "string",
            },
            use_ssh=True,
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDataherald) -> None:
        response = await async_client.database_connections.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = await response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDataherald) -> None:
        async with async_client.database_connections.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database_connection = await response.parse()
            assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDataherald) -> None:
        database_connection = await async_client.database_connections.retrieve(
            "string",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDataherald) -> None:
        response = await async_client.database_connections.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = await response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDataherald) -> None:
        async with async_client.database_connections.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database_connection = await response.parse()
            assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.database_connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDataherald) -> None:
        database_connection = await async_client.database_connections.update(
            "string",
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDataherald) -> None:
        database_connection = await async_client.database_connections.update(
            "string",
            alias="string",
            connection_uri="string",
            credential_file_content={},
            llm_api_key="string",
            metadata={},
            ssh_settings={
                "db_name": "string",
                "host": "string",
                "username": "string",
                "password": "string",
                "remote_host": "string",
                "remote_db_name": "string",
                "remote_db_password": "string",
                "private_key_password": "string",
                "db_driver": "string",
            },
            use_ssh=True,
        )
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDataherald) -> None:
        response = await async_client.database_connections.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = await response.parse()
        assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDataherald) -> None:
        async with async_client.database_connections.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database_connection = await response.parse()
            assert_matches_type(DBConnectionResponse, database_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDataherald) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.database_connections.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDataherald) -> None:
        database_connection = await async_client.database_connections.list()
        assert_matches_type(DatabaseConnectionListResponse, database_connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDataherald) -> None:
        response = await async_client.database_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database_connection = await response.parse()
        assert_matches_type(DatabaseConnectionListResponse, database_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDataherald) -> None:
        async with async_client.database_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database_connection = await response.parse()
            assert_matches_type(DatabaseConnectionListResponse, database_connection, path=["response"])

        assert cast(Any, response.is_closed) is True
