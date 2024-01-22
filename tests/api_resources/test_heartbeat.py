# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHeartbeat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Dataherald) -> None:
        heartbeat = client.heartbeat.retrieve()
        assert_matches_type(object, heartbeat, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dataherald) -> None:
        response = client.heartbeat.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        heartbeat = response.parse()
        assert_matches_type(object, heartbeat, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dataherald) -> None:
        with client.heartbeat.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            heartbeat = response.parse()
            assert_matches_type(object, heartbeat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHeartbeat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDataherald) -> None:
        heartbeat = await async_client.heartbeat.retrieve()
        assert_matches_type(object, heartbeat, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDataherald) -> None:
        response = await async_client.heartbeat.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        heartbeat = await response.parse()
        assert_matches_type(object, heartbeat, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDataherald) -> None:
        async with async_client.heartbeat.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            heartbeat = await response.parse()
            assert_matches_type(object, heartbeat, path=["response"])

        assert cast(Any, response.is_closed) is True
