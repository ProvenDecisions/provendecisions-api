# ProvenDecisions API and MCP server

Solve linear, integer, quadratic and convex optimization problems from your own code or AI assistant, and get every
answer **proven**: each constraint checked, and a dual or KKT certificate that nothing better exists. The numbers come
from real solvers (HiGHS, Clarabel, SCIP), never from a language model.

| File | What it shows |
|---|---|
| [examples/solve.py](examples/solve.py) | Solve a model from Python and print the status, objective, solution and proof label |
| [MCP.md](MCP.md) | Connect Claude Code or Claude Desktop, so the assistant uses the solver |

Quick start:

```
pip install requests
export PROVENDECISIONS_API_KEY=pd_live_...     # the app: Settings, API keys
python examples/solve.py
```

```
status:    optimal
objective: 160.0
solution:  {'a': 40.0, 'b': 20.0}
proof:     Exactly proven optimal
```

- **Documentation and API reference:** [proven-decisions.ai/developers](https://proven-decisions.ai/developers?ref=github)
- **Plans:** the API and MCP server are part of the Standard and Pro plans: [pricing](https://proven-decisions.ai/pricing?ref=github)
- **Try it first, free:** type a model on the [front page](https://proven-decisions.ai/?ref=github)

The code in this repository is under the MIT License (LICENSE).
