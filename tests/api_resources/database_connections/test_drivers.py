# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald.types.database_connections import DriverListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDrivers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        driver = client.database_connections.drivers.list()
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.database_connections.drivers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = response.parse()
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dataherald) -> None:
        with client.database_connections.drivers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = response.parse()
            assert_matches_type(DriverListResponse, driver, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDrivers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncDataherald) -> None:
        driver = await async_client.database_connections.drivers.list()
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDataherald) -> None:
        response = await async_client.database_connections.drivers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = await response.parse()
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDataherald) -> None:
        async with async_client.database_connections.drivers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = await response.parse()
            assert_matches_type(DriverListResponse, driver, path=["response"])

        assert cast(Any, response.is_closed) is True
