# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald._client import Dataherald, AsyncDataherald

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestEngine:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_heartbeat(self, client: Dataherald) -> None:
        engine = client.engine.heartbeat()
        assert_matches_type(object, engine, path=["response"])

    @parametrize
    def test_raw_response_heartbeat(self, client: Dataherald) -> None:
        response = client.engine.with_raw_response.heartbeat()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(object, engine, path=["response"])


class TestAsyncEngine:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_heartbeat(self, client: AsyncDataherald) -> None:
        engine = await client.engine.heartbeat()
        assert_matches_type(object, engine, path=["response"])

    @parametrize
    async def test_raw_response_heartbeat(self, client: AsyncDataherald) -> None:
        response = await client.engine.with_raw_response.heartbeat()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(object, engine, path=["response"])
