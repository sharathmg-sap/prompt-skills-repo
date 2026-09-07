# GitHub MCP Agent: Instructions and Procedure

This guide explains how to configure an agent prompt to use the available
GitHub MCP server for public, read-only demonstrations. It does not contain or
require credentials.

## 1. Agent instructions

Load [github_mcp_demonstrator.md](../agents/github_mcp_demonstrator.md) as the
agent's role prompt. The agent must:

1. Convert the user request into one GitHub operation.
2. Select the smallest matching MCP tool.
3. Validate required arguments.
4. Invoke the tool with structured JSON arguments.
5. Summarize the result and show a sanitized invocation trace.

The agent must not invent a result when the MCP server is unavailable, and must
not perform write operations without explicit confirmation.

## 2. Procedure for an agent invocation

### Step 1: Parse the request

Identify:

- operation: search, list, retrieve, or inspect;
- target: repository, owner, branch, issue, pull request, or commit;
- filters: query text, state, branch, or path;
- output fields needed by the user.

Ask for missing repository identifiers instead of guessing them.

### Step 2: Select the MCP tool

Use the most specific available tool:

| Operation | Example tool |
| --- | --- |
| Repository search | `github-mcp-server-search_repositories` |
| Code search | `github-mcp-server-search_code` |
| File retrieval | `github-mcp-server-get_file_contents` |
| Repository listing | `github-mcp-server-list_*` |
| Issue or pull request inspection | `github-mcp-server-issue_read` or `github-mcp-server-pull_request_read` |
| Commit inspection | `github-mcp-server-get_commit` |

Prefer minimal fields and bounded page sizes for demonstrations.

### Step 3: Invoke with structured arguments

Example: search public repositories for MCP servers:

```text
github-mcp-server-search_repositories({
  "query": "model context protocol server",
  "minimal_output": true,
  "perPage": 5
})
```

Example: retrieve a public README:

```text
github-mcp-server-get_file_contents({
  "owner": "modelcontextprotocol",
  "repo": "servers",
  "path": "README.md",
  "ref": "main"
})
```

The exact function-call envelope is supplied by the MCP client. The important
parts are the selected tool name and its JSON arguments.

### Step 4: Validate the result

Check that:

- the tool returned successfully;
- the result matches the requested owner, repository, and operation;
- pagination or incomplete-result flags are reported;
- links and identifiers are preserved where useful;
- no sensitive values are echoed.

### Step 5: Explain the use

Return a short trace:

```text
Tool: github-mcp-server-search_repositories
Purpose: Find public repositories matching the requested topic.
Arguments: query="model context protocol server", minimal_output=true, perPage=5
Result: Returned five public repository records.
```

## 3. Read-only demonstration boundaries

The demonstration should use public reads such as repository search, public file
retrieval, branch listing, or issue inspection. Do not use create/update/delete,
comment, merge, or review tools unless the user explicitly requests the action,
the exact target and payload are known, and confirmation has been obtained.

Never place tokens or other secrets in prompts, arguments, logs, or examples.

## 4. Troubleshooting

| Situation | Agent behavior |
| --- | --- |
| MCP tool is not available | Say so; show a non-executed example invocation |
| Required owner/repository is missing | Ask for the missing identifier |
| Search returns no results | Report zero results; do not broaden silently |
| Results are truncated | Report pagination and offer the next page |
| Tool returns an error | Report the error category and stop; do not claim success |

## 5. Verification checklist

- [ ] The selected tool matches the operation.
- [ ] Arguments are valid and non-sensitive.
- [ ] The invocation actually returned a result.
- [ ] The response distinguishes execution from an example.
- [ ] Read-only boundaries were respected.
