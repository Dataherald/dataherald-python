# File generated from our OpenAPI spec by Stainless.

import httpx

RAW_RESPONSE_HEADER = "X-Stainless-Raw-Response"
OVERRIDE_CAST_TO_HEADER = "____stainless_override_cast_to"

# default timeout is 6.0200000000000005 minutes
DEFAULT_TIMEOUT = httpx.Timeout(timeout=361.0, connect=5.0)
DEFAULT_MAX_RETRIES = 0
DEFAULT_LIMITS = httpx.Limits(max_connections=100, max_keepalive_connections=20)

INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0
