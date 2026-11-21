# Use ProvenDecisions from Claude and other AI assistants (MCP)

The MCP server gives an assistant the solver's tools, so it quotes a solver's checked numbers instead of guessing. It
is part of the Standard and Pro plans. Full reference: https://proven-decisions.ai/developers?ref=github

## Claude Code

Signs you in through your browser (choose **Allow**):

```
claude mcp add --transport http --scope user proven-decisions https://proven-decisions.ai/mcp
```

Or with an API key (for example on a server with no browser; create the key in the app under Settings, API keys):

```
claude mcp add --transport http --scope user proven-decisions https://proven-decisions.ai/mcp \
  --header "Authorization: Bearer $PD_KEY"
```

## Claude Desktop

Add this to `claude_desktop_config.json` (Settings, Developer, Edit config; it uses the `mcp-remote` bridge, so
Node.js is needed), then restart Claude:

```json
{
  "mcpServers": {
    "provendecisions": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://proven-decisions.ai/mcp", "--header", "Authorization:${AUTH_HEADER}"],
      "env": {"AUTH_HEADER": "Bearer pd_live_..."}
    }
  }
}
```

## Tools

`solve`, `dual`, `kkt` and `explain` (the walkthrough as text at a depth you choose), and for the site's content
`search_content`, `get_content` and `list_content`.
