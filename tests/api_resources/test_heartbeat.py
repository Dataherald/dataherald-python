# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type
from dataherald._client import Dataherald, AsyncDataherald

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestHeartbeat:
    strict_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Dataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        heartbeat = client.heartbeat.retrieve()
        assert_matches_type(object, heartbeat, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.heartbeat.with_raw_response.retrieve()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        heartbeat = response.parse()
        assert_matches_type(object, heartbeat, path=["response"])


class TestAsyncHeartbeat:
    strict_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncDataherald(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncDataherald) -> None:
        heartbeat = await client.heartbeat.retrieve()
        assert_matches_type(object, heartbeat, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncDataherald) -> None:
        response = await client.heartbeat.with_raw_response.retrieve()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        heartbeat = response.parse()
        assert_matches_type(object, heartbeat, path=["response"])
