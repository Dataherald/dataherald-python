# Shared Types

```python
from dataherald.types import (
    GoldenSqlResponse,
    InstructionResponse,
    NlGenerationResponse,
    SqlGenerationResponse,
)
```

# DatabaseConnections

Types:

```python
from dataherald.types import DBConnectionResponse, DatabaseConnectionListResponse
```

Methods:

- <code title="post /api/database-connections">client.database_connections.<a href="./src/dataherald/resources/database_connections/database_connections.py">create</a>(\*\*<a href="src/dataherald/types/database_connection_create_params.py">params</a>) -> <a href="./src/dataherald/types/db_connection_response.py">DBConnectionResponse</a></code>
- <code title="get /api/database-connections/{id}">client.database_connections.<a href="./src/dataherald/resources/database_connections/database_connections.py">retrieve</a>(id) -> <a href="./src/dataherald/types/db_connection_response.py">DBConnectionResponse</a></code>
- <code title="put /api/database-connections/{id}">client.database_connections.<a href="./src/dataherald/resources/database_connections/database_connections.py">update</a>(id, \*\*<a href="src/dataherald/types/database_connection_update_params.py">params</a>) -> <a href="./src/dataherald/types/db_connection_response.py">DBConnectionResponse</a></code>
- <code title="get /api/database-connections">client.database_connections.<a href="./src/dataherald/resources/database_connections/database_connections.py">list</a>() -> <a href="./src/dataherald/types/database_connection_list_response.py">DatabaseConnectionListResponse</a></code>

## Drivers

Types:

```python
from dataherald.types.database_connections import DriverResponse, DriverListResponse
```

Methods:

- <code title="get /api/database-connections/drivers">client.database_connections.drivers.<a href="./src/dataherald/resources/database_connections/drivers.py">list</a>() -> <a href="./src/dataherald/types/database_connections/driver_list_response.py">DriverListResponse</a></code>

# Finetunings

Types:

```python
from dataherald.types import FinetuningResponse
```

Methods:

- <code title="post /api/finetunings">client.finetunings.<a href="./src/dataherald/resources/finetunings.py">create</a>(\*\*<a href="src/dataherald/types/finetuning_create_params.py">params</a>) -> <a href="./src/dataherald/types/finetuning_response.py">FinetuningResponse</a></code>
- <code title="get /api/finetunings/{id}">client.finetunings.<a href="./src/dataherald/resources/finetunings.py">retrieve</a>(id) -> <a href="./src/dataherald/types/finetuning_response.py">FinetuningResponse</a></code>

# GoldenSqls

Types:

```python
from dataherald.types import (
    AdminConsoleGoldenSqlResponse,
    GoldenSqlListResponse,
    GoldenSqlDeleteResponse,
)
```

Methods:

- <code title="get /api/golden-sqls/{id}">client.golden_sqls.<a href="./src/dataherald/resources/golden_sqls.py">retrieve</a>(id) -> <a href="./src/dataherald/types/shared/golden_sql_response.py">GoldenSqlResponse</a></code>
- <code title="get /api/golden-sqls">client.golden_sqls.<a href="./src/dataherald/resources/golden_sqls.py">list</a>(\*\*<a href="src/dataherald/types/golden_sql_list_params.py">params</a>) -> <a href="./src/dataherald/types/golden_sql_list_response.py">GoldenSqlListResponse</a></code>
- <code title="delete /api/golden-sqls/{id}">client.golden_sqls.<a href="./src/dataherald/resources/golden_sqls.py">delete</a>(id) -> <a href="./src/dataherald/types/golden_sql_delete_response.py">object</a></code>

# Instructions

Types:

```python
from dataherald.types import InstructionListResponse, InstructionDeleteResponse
```

Methods:

- <code title="post /api/instructions">client.instructions.<a href="./src/dataherald/resources/instructions/instructions.py">create</a>(\*\*<a href="src/dataherald/types/instruction_create_params.py">params</a>) -> <a href="./src/dataherald/types/shared/instruction_response.py">InstructionResponse</a></code>
- <code title="put /api/instructions/{id}">client.instructions.<a href="./src/dataherald/resources/instructions/instructions.py">update</a>(id, \*\*<a href="src/dataherald/types/instruction_update_params.py">params</a>) -> <a href="./src/dataherald/types/shared/instruction_response.py">InstructionResponse</a></code>
- <code title="get /api/instructions">client.instructions.<a href="./src/dataherald/resources/instructions/instructions.py">list</a>(\*\*<a href="src/dataherald/types/instruction_list_params.py">params</a>) -> <a href="./src/dataherald/types/instruction_list_response.py">InstructionListResponse</a></code>
- <code title="delete /api/instructions/{id}">client.instructions.<a href="./src/dataherald/resources/instructions/instructions.py">delete</a>(id) -> <a href="./src/dataherald/types/instruction_delete_response.py">object</a></code>

## First

Methods:

- <code title="get /api/instructions/first">client.instructions.first.<a href="./src/dataherald/resources/instructions/first.py">retrieve</a>() -> <a href="./src/dataherald/types/shared/instruction_response.py">InstructionResponse</a></code>

# Generations

Types:

```python
from dataherald.types import GenerationListItem, GenerationResponse, GenerationListResponse
```

Methods:

- <code title="post /api/generations/{id}">client.generations.<a href="./src/dataherald/resources/generations.py">create</a>(id) -> <a href="./src/dataherald/types/generation_response.py">GenerationResponse</a></code>
- <code title="get /api/generations/{id}">client.generations.<a href="./src/dataherald/resources/generations.py">retrieve</a>(id) -> <a href="./src/dataherald/types/generation_response.py">GenerationResponse</a></code>
- <code title="put /api/generations/{id}">client.generations.<a href="./src/dataherald/resources/generations.py">update</a>(id, \*\*<a href="src/dataherald/types/generation_update_params.py">params</a>) -> <a href="./src/dataherald/types/generation_response.py">GenerationResponse</a></code>
- <code title="get /api/generations">client.generations.<a href="./src/dataherald/resources/generations.py">list</a>(\*\*<a href="src/dataherald/types/generation_list_params.py">params</a>) -> <a href="./src/dataherald/types/generation_list_response.py">GenerationListResponse</a></code>
- <code title="post /api/generations/{id}/nl-generation">client.generations.<a href="./src/dataherald/resources/generations.py">nl_generation</a>(id) -> <a href="./src/dataherald/types/shared/nl_generation_response.py">NlGenerationResponse</a></code>
- <code title="post /api/generations/{id}/sql-generation">client.generations.<a href="./src/dataherald/resources/generations.py">sql_generation</a>(id, \*\*<a href="src/dataherald/types/generation_sql_generation_params.py">params</a>) -> <a href="./src/dataherald/types/generation_response.py">GenerationResponse</a></code>

# Prompts

Types:

```python
from dataherald.types import PromptResponse, PromptListResponse
```

Methods:

- <code title="post /api/prompts">client.prompts.<a href="./src/dataherald/resources/prompts/prompts.py">create</a>(\*\*<a href="src/dataherald/types/prompt_create_params.py">params</a>) -> <a href="./src/dataherald/types/prompt_response.py">PromptResponse</a></code>
- <code title="get /api/prompts/{id}">client.prompts.<a href="./src/dataherald/resources/prompts/prompts.py">retrieve</a>(id) -> <a href="./src/dataherald/types/prompt_response.py">PromptResponse</a></code>
- <code title="get /api/prompts">client.prompts.<a href="./src/dataherald/resources/prompts/prompts.py">list</a>(\*\*<a href="src/dataherald/types/prompt_list_params.py">params</a>) -> <a href="./src/dataherald/types/prompt_list_response.py">PromptListResponse</a></code>

## SqlGenerations

Types:

```python
from dataherald.types.prompts import SqlGenerationRetrieveResponse
```

Methods:

- <code title="post /api/prompts/{id}/sql-generations">client.prompts.sql_generations.<a href="./src/dataherald/resources/prompts/sql_generations.py">create</a>(id, \*\*<a href="src/dataherald/types/prompts/sql_generation_create_params.py">params</a>) -> <a href="./src/dataherald/types/shared/sql_generation_response.py">SqlGenerationResponse</a></code>
- <code title="get /api/prompts/{id}/sql-generations">client.prompts.sql_generations.<a href="./src/dataherald/resources/prompts/sql_generations.py">retrieve</a>(id, \*\*<a href="src/dataherald/types/prompts/sql_generation_retrieve_params.py">params</a>) -> <a href="./src/dataherald/types/prompts/sql_generation_retrieve_response.py">object</a></code>
- <code title="post /api/prompts/{id}/sql-generations/nl-generations">client.prompts.sql_generations.<a href="./src/dataherald/resources/prompts/sql_generations.py">nl_generations</a>(id, \*\*<a href="src/dataherald/types/prompts/sql_generation_nl_generations_params.py">params</a>) -> <a href="./src/dataherald/types/shared/nl_generation_response.py">NlGenerationResponse</a></code>

# SqlGenerations

Types:

```python
from dataherald.types import SqlGenerationListResponse, SqlGenerationExecuteResponse
```

Methods:

- <code title="post /api/prompts/sql-generations">client.sql_generations.<a href="./src/dataherald/resources/sql_generations/sql_generations.py">create</a>(\*\*<a href="src/dataherald/types/sql_generation_create_params.py">params</a>) -> <a href="./src/dataherald/types/shared/sql_generation_response.py">SqlGenerationResponse</a></code>
- <code title="get /api/sql-generations/{id}">client.sql_generations.<a href="./src/dataherald/resources/sql_generations/sql_generations.py">retrieve</a>(id) -> <a href="./src/dataherald/types/shared/sql_generation_response.py">SqlGenerationResponse</a></code>
- <code title="get /api/sql-generations">client.sql_generations.<a href="./src/dataherald/resources/sql_generations/sql_generations.py">list</a>(\*\*<a href="src/dataherald/types/sql_generation_list_params.py">params</a>) -> <a href="./src/dataherald/types/sql_generation_list_response.py">SqlGenerationListResponse</a></code>
- <code title="post /api/sql-generations/{id}/execute">client.sql_generations.<a href="./src/dataherald/resources/sql_generations/sql_generations.py">execute</a>(id, \*\*<a href="src/dataherald/types/sql_generation_execute_params.py">params</a>) -> <a href="./src/dataherald/types/sql_generation_execute_response.py">SqlGenerationExecuteResponse</a></code>

## NlGenerations

Types:

```python
from dataherald.types.sql_generations import NlGenerationRetrieveResponse
```

Methods:

- <code title="post /api/sql-generations/{id}/nl-generations">client.sql_generations.nl_generations.<a href="./src/dataherald/resources/sql_generations/nl_generations.py">create</a>(id, \*\*<a href="src/dataherald/types/sql_generations/nl_generation_create_params.py">params</a>) -> <a href="./src/dataherald/types/shared/nl_generation_response.py">NlGenerationResponse</a></code>
- <code title="get /api/sql-generations/{id}/nl-generations">client.sql_generations.nl_generations.<a href="./src/dataherald/resources/sql_generations/nl_generations.py">retrieve</a>(id, \*\*<a href="src/dataherald/types/sql_generations/nl_generation_retrieve_params.py">params</a>) -> <a href="./src/dataherald/types/sql_generations/nl_generation_retrieve_response.py">object</a></code>

# NlGenerations

Types:

```python
from dataherald.types import NlGenerationListResponse
```

Methods:

- <code title="get /api/nl-generations/{id}">client.nl_generations.<a href="./src/dataherald/resources/nl_generations.py">retrieve</a>(id) -> <a href="./src/dataherald/types/shared/nl_generation_response.py">NlGenerationResponse</a></code>
- <code title="get /api/nl-generations">client.nl_generations.<a href="./src/dataherald/resources/nl_generations.py">list</a>(\*\*<a href="src/dataherald/types/nl_generation_list_params.py">params</a>) -> <a href="./src/dataherald/types/nl_generation_list_response.py">NlGenerationListResponse</a></code>

# TableDescriptions

Types:

```python
from dataherald.types import (
    TableDescriptionResponse,
    TableDescriptionListResponse,
    TableDescriptionSyncSchemasResponse,
)
```

Methods:

- <code title="get /api/table-descriptions/{id}">client.table_descriptions.<a href="./src/dataherald/resources/table_descriptions.py">retrieve</a>(id) -> <a href="./src/dataherald/types/table_description_response.py">TableDescriptionResponse</a></code>
- <code title="put /api/table-descriptions/{id}">client.table_descriptions.<a href="./src/dataherald/resources/table_descriptions.py">update</a>(id, \*\*<a href="src/dataherald/types/table_description_update_params.py">params</a>) -> <a href="./src/dataherald/types/table_description_response.py">TableDescriptionResponse</a></code>
- <code title="get /api/table-descriptions">client.table_descriptions.<a href="./src/dataherald/resources/table_descriptions.py">list</a>(\*\*<a href="src/dataherald/types/table_description_list_params.py">params</a>) -> <a href="./src/dataherald/types/table_description_list_response.py">TableDescriptionListResponse</a></code>
- <code title="post /api/table-descriptions/sync-schemas">client.table_descriptions.<a href="./src/dataherald/resources/table_descriptions.py">sync_schemas</a>(\*\*<a href="src/dataherald/types/table_description_sync_schemas_params.py">params</a>) -> <a href="./src/dataherald/types/table_description_sync_schemas_response.py">object</a></code>

# Heartbeat

Types:

```python
from dataherald.types import HeartbeatRetrieveResponse
```

Methods:

- <code title="get /heartbeat">client.heartbeat.<a href="./src/dataherald/resources/heartbeat.py">retrieve</a>() -> <a href="./src/dataherald/types/heartbeat_retrieve_response.py">object</a></code>

# Engine

Types:

```python
from dataherald.types import EngineHeartbeatResponse
```

Methods:

- <code title="get /engine/heartbeat">client.engine.<a href="./src/dataherald/resources/engine.py">heartbeat</a>() -> <a href="./src/dataherald/types/engine_heartbeat_response.py">object</a></code>
