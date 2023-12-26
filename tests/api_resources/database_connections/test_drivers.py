# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald._client import Dataherald, AsyncDataherald
from dataherald.types.database_connections import DriverListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestDrivers:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Dataherald) -> None:
        driver = client.database_connections.drivers.list()
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dataherald) -> None:
        response = client.database_connections.drivers.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = response.parse()
        assert_matches_type(DriverListResponse, driver, path=["response"])


class TestAsyncDrivers:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncDataherald) -> None:
        driver = await client.database_connections.drivers.list()
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncDataherald) -> None:
        response = await client.database_connections.drivers.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = response.parse()
        assert_matches_type(DriverListResponse, driver, path=["response"])
