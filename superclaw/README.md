<h1 align="center">Intel®AI SuperClaw</h1>

**Hybrid agentic AI for enterprises: local by default, cloud when it counts.**

SuperClaw is a hybrid agentic AI solution for AI PCs, workstations, agent computers, and edge devices. Built by Intel's AI Super Builder team, it helps enterprises scale intelligent agents while managing cloud compute cost, performance, and data security.

Agentic AI can automate complex work across tools, files, code, and business data, but cloud-only deployments can increase token costs and expose sensitive context to privacy and control risks.

SuperClaw addresses this with a local-first, cloud-assisted architecture: routine and sensitive work runs on-device or at the enterprise edge, while cloud models are reserved for advanced reasoning, planning, and external data retrieval.

For more detail, read Intel's article, [Solving the Agentic AI Trilemma: Cost, Scale, and Data Security](https://newsroom.intel.com/opinion/solving-the-agentic-ai-trilemma-cost-scale-and-data-security).

---

## Why SuperClaw

- **Reduce cloud compute token costs.** Route routine and sensitive work locally, and reserve cloud models for tasks that need them.
- **Help protect sensitive enterprise data.** Keep private data on-device or within the enterprise edge by default, with data minimization before cloud escalation.
- **Deliver practical agentic performance.** Send each workflow step to the right execution layer for the task.
- **Run on modern Intel platforms.** SuperClaw is designed for Intel AI PCs and workstations, including systems with Intel® Core™ Ultra processors and Intel® Arc™ Pro B-series GPUs.
- **Do real work, not just chat.** Specialized agents work with files, code, email, calendars, web research, and MCP-connected tools.
- **Scale automation safely.** Scheduling and agent collaboration help routine work run consistently across enterprise workflows.

---

## Release Configurations

The first SuperClaw release is designed for a two-system setup:

- **An AI PC companion device**, such as a Wildcat Lake 16GB system, where the SuperClaw desktop app runs.
- **A model-serving workstation** with four B70 cards, where Qwen3-Coder-Next-80B runs. Refer to the [User Guide](./superclaw-ctl/USER-GUIDE.md) for more details.

In this setup, users interact with SuperClaw on the AI PC while the heavier model workload runs on the B70 workstation. Based on Intel testing, this configuration provides the best user experience for the initial release.

A standalone version for PTL 64GB systems is coming in a later release.

---

## Agents

SuperClaw ships with purpose-built agents that can work independently or collaborate through coordinated workflows.

| Agent | What it does |
|-------|--------------|
| **Default Agent** | A generalist for answering questions, reading and editing files, running tools, and coordinating specialists for larger tasks. |
| **Hybrid Coding Agent** | A coding specialist for reading, writing, editing, debugging, running scripts, and handling git operations through explore, edit, and test loops. |
| **Deep Research Agent (Beta)** | Runs multi-step research by delegating focused subtasks to web-search and file specialists, then synthesizes a cited answer. Full capability is planned for an update release in about one month. |
| **Email & Calendar Agent** | Runs locally for security while listing, searching, summarizing, and prioritizing email; drafting replies; scheduling meetings; building daily plans; and tracking action items. |
| **Local File Agent** | Extracts and answers questions from documents such as PDF, CSV, Markdown, DOCX, XLSX, and PPTX using local models for precision and privacy. |
| **Web Search Agent** | Returns focused, factual answers with source citations for current information from the web. |
| **Protect File Agent** | Detects and masks sensitive information in a file before further processing so private data stays protected end to end. |

A complex request, such as analyzing a spreadsheet of customer records, can flow through a coordinated pipeline that prepares the data, detects and masks personal information, performs the analysis, and only escalates limited context to the cloud when needed.

---

## Auto Route

**Auto Route is SuperClaw's intelligent model router.** For every task, it decides whether work should run on a local model, an enterprise edge resource, or a cloud model.

- **Transparent.** Users see a single assistant response while SuperClaw handles the execution strategy behind the scenes.
- **Task-aware.** Lightweight, sensitive, and repetitive work stays local; demanding reasoning and planning can be routed to cloud models.
- **User-controlled.** Users can choose Auto Route, force a local model for on-device work, or select a cloud model directly when maximum capability is required.

To enable Auto Route, configure both a local model and at least one cloud model in Settings. If only local models are available, users can select a local model and work entirely offline.

---

## Settings and Extensibility

The **Advanced** area is where enterprises and users tailor SuperClaw to their hardware, providers, and workflows. It is organized into five sections:

### Model Routing

Connect cloud model providers with an API key and select the cloud model used by Auto Route, alongside your local model.

### Configuration

A single place for core operational settings:

- **Web Search** — Configure a [Tavily](https://www.tavily.com/) API key for higher-quality web search. Tavily offers 1,000 free searches with sign-in. If no key is configured, web search falls back to DuckDuckGo by default.
- **Gmail Credentials** — Upload Google OAuth credentials to authorize the Email & Calendar Agent. SuperClaw provides setup instructions when you ask it to access your email. If you need more guidance, follow this [Gmail API setup video](https://www.youtube.com/watch?v=RsY14ltDNFM).
- **Backend Lifecycle** — Control whether backend services keep running after the app closes. Keeping them running enables a faster next launch.
- **Workspace Cleanup** — Automatically remove agent-generated logs, temp files, and cache from the workspace after a configurable retention period. Your results and reports are never touched.
- **Appearance & Language** — Match the system theme or force light/dark mode, and choose the interface language.

### Scheduler

Create scheduled tasks for recurring work, or start from built-in templates for common automation workflows. For best results, provide clear and detailed instructions for what the agent should do.

### MCP

SuperClaw supports the **Model Context Protocol (MCP)**, an open standard for connecting AI agents to external tools and data sources. Current local MCP server support has a few setup requirements because SuperClaw's backend runs inside Docker on WSL2 while the UI runs on Windows.

For local MCP servers:

- Use **HTTP** or **SSE** transport. Stdio-based MCP servers are not supported in the current release.
- Start the MCP server on Windows and bind it to `0.0.0.0`, not `127.0.0.1` or `localhost`.
- In SuperClaw, connect to the server with `http://host.docker.internal:<port>/<endpoint>`.

Common endpoints are `/mcp` for streamable HTTP and `/sse` for SSE. For example, use `http://host.docker.internal:3000/mcp` or `http://host.docker.internal:3000/sse`, depending on your server.

### Channel

Deliver agent and scheduled-task results to your team's messaging tools. Slack is supported in the first release, with additional channels planned.

To configure Slack, go to [Slack API Apps](https://api.slack.com/apps), create a new app from scratch, and select your workspace. For a walkthrough, follow this [Slack app setup video](https://www.youtube.com/watch?v=eMN94wkwYME).

In Slack, open **Features > OAuth & Permissions > Bot Token Scopes** and add these recommended bot token (`xoxb`) scopes for full support:

```text
app_mentions:read
channels:history
channels:read
chat:write
chat:write.public
groups:history
groups:read
im:history
im:read
im:write
mpim:history
mpim:read
users:read
```

Minimal public-channel setup: `app_mentions:read`, `channels:read`, `chat:write`, and `users:read`. Add `channels:history` for channel context and [`chat:write.public`](https://docs.slack.dev/reference/scopes/chat:write.public) to send messages to public channels where @IntelSuperClaw is not a member. After installation, copy the bot token and app token into **Advanced > Channel > Slack**, then mention the bot in Slack to start using it.

---

## Known Issues
- **CPU virtualization is required to install WSL.** SuperClaw uses WSL, which requires CPU virtualization to be enabled in BIOS/UEFI. If installation fails, enable Intel Virtualization Technology, also called Intel VT-x, restart Windows, and run the installer again. On managed PCs, contact your IT administrator if the setting is locked or unavailable.
- **Restart Windows after installing WSL.** If WSL is installed during setup and Windows is not restarted, the SuperClaw installer may stop around 10%. Restart Windows, then run the installer again so the WSL components are fully available.
- **WSL repair may be needed if installation stops around 10%.** If `wsl.exe` reports `Wsl/CallMsi/Install/REGDB_E_CLASSNOTREG` or says WSL is corrupted, open PowerShell as Administrator, run `wsl --install --no-distribution`, restart Windows, and run the installer again. If needed, run `wsl --update` as Administrator, restart, and try again.
- **`owt.failed` can mean the backend is unreachable or loopback traffic is proxied.** If `http://127.0.0.1:8787/health` returns `403 Forbidden`, add `127.0.0.1,localhost,::1` to your user `NO_PROXY` setting, keeping any existing corporate entries, then stop SuperClaw and relaunch it from a new terminal. If it is still stuck, stop SuperClaw, run `wsl.exe --unregister superclaw-docker`, and relaunch.
- **Corporate networks may require proxy setup before installation.** If your corporate network requires a proxy for downloads, configure the required HTTP proxy before installing SuperClaw. On an open network, no proxy setup is needed. If you switch between a corporate network and an outside network, quit SuperClaw, run `wsl.exe --unregister superclaw-docker`, and reopen the app so the backend is recreated with the current network settings.
- **Proxy or VPN environments may require `networkingMode=mirrored` in `.wslconfig`.** If SuperClaw cannot reach the internet or your corporate proxy from within WSL2, add the following to `C:\Users\<username>\.wslconfig` (create the file if it does not exist):
  ```ini
  [wsl2]
  networkingMode=mirrored
  ```
  This makes WSL2 mirror your Windows network interfaces so that proxy and VPN routes are automatically inherited. After saving the file, run `wsl --shutdown` in PowerShell or Command Prompt to restart WSL2, then relaunch SuperClaw.
- **Uninstall does not remove local user data.** Data may remain under `C:\Users\<user_id>\AppData\Local\SuperClaw\scbms`.
- **Local MCP servers must use HTTP or SSE transport.** Stdio-based MCP servers are not supported in the current release.

