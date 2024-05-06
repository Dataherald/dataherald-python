# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dataherald import Dataherald, AsyncDataherald
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEngine:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_heartbeat(self, client: Dataherald) -> None:
        engine = client.engine.heartbeat()
        assert_matches_type(object, engine, path=["response"])

    @parametrize
    def test_raw_response_heartbeat(self, client: Dataherald) -> None:
        response = client.engine.with_raw_response.heartbeat()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(object, engine, path=["response"])

    @parametrize
    def test_streaming_response_heartbeat(self, client: Dataherald) -> None:
        with client.engine.with_streaming_response.heartbeat() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(object, engine, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEngine:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_heartbeat(self, async_client: AsyncDataherald) -> None:
        engine = await async_client.engine.heartbeat()
        assert_matches_type(object, engine, path=["response"])

    @parametrize
    async def test_raw_response_heartbeat(self, async_client: AsyncDataherald) -> None:
        response = await async_client.engine.with_raw_response.heartbeat()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(object, engine, path=["response"])

    @parametrize
    async def test_streaming_response_heartbeat(self, async_client: AsyncDataherald) -> None:
        async with async_client.engine.with_streaming_response.heartbeat() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(object, engine, path=["response"])

        assert cast(Any, response.is_closed) is True
