# Nord AI v5 — Autonomous Agent System

![Nord AI](logo.svg)

[Read this in Swedish](README.sv.md)

## What is Nord AI?

Nord AI is an autonomous multi-agent system with 8 specialized agents, 88 modules, cognitive memory, Theory of Mind, WASI sandbox, parallel reasoning, self-evolving memory, trading engine, social media automation, legal AI, and security according to 8 international standards. Fully provider-agnostic.

## 8 Specialized Agents
| Agent | Role |
|---|---|
| Orchestrator | Leader — routing, synthesis, Confidence Router |
| Researcher | Research — information gathering, analysis |
| Coder | Code — write, debug, k=3 candidates, auto-correct, self-test |
| Analyzer | Analysis — Chain-of-Thought, Tree-of-Thought |
| Security | Security — OWASP, GDPR, AI Act review |
| Writer | Content — documentation, reports, communication |
| DevOps | Infrastructure — Docker, CI/CD, deployment |
| Reviewer | Quality — code review, test suggestions, scoring |

## 88 Modules

| Category | Modules |
|---|---|
| Core | agents, memory, sandbox, security, compliance, skills, knowledge_graph, tasks |
| Security | ironclaw_sandbox, wasi_sandbox, guardrails, trivy_scanner, offensive_security, bug_bounty, auth, moral_guardrails |
| Cognition | theory_of_mind, meta_evolution, episodic_memory, parallel_reasoning, cognitive_memory, workspace_isolation, evolving_memory |
| Production | model_router, test_framework, benchmark, scheduler, pricing, analytics_dashboard, cache, docker_sandbox |
| Orchestration | multi_arch, agent_handoffs, event_mesh, self_healing, batch_processing, workflow_builder, streaming_tools |
| Features | voice, finance, research_loop, video, board, browser, browser_use, rag_pipeline, embeddings, notifications, social_media, content_factory, web_search, image_gen |
| Legal | legal, legal_drafter, compliance |
| Learning | always_learn, agent_testing, skill_marketplace, version_memory |
| Access | internet_access, persistent_sandbox, team_collab, observability, mcp_integration, enterprise_sso, collections, artifacts, leadership |
| Trading | trading, strategies, exchange, portfolio, backtesting, training |
| Frontend | index.html, manifest.json, sw.js |

## Security (8 Standards)
OWASP Top 10, GDPR (EU 2016/679), EU AI Act (2024/1689), ISO 27001, SOC 2, NIST CSF, NIST AI RMF, CIS Controls v8

## Legal
EU AI Act, GDPR, eIDAS 2.0, CRA, Data Act, Brottsbalken, Försäkringsavtalslagen, Socialförsäkringsbalken, Nordic compliance (SE/NO/DK/FI/IS)

## Quick Start

```bash
# Docker
docker-compose up -d

# Manual
cd backend
pip install -r requirements.txt
cp ../.env.example .env
python main.py

# Fix language (translate Swedish to English in code)
python fix_language.py
```

## Provider-agnostic
No LLM brand names. Configure PROVIDER_A_KEY, PROVIDER_B_KEY, LOCAL_URL in .env

## 100+ Endpoints
Chat, Code, Elite, Multi, Streaming, Pipeline, Security, GDPR, AI Act, Legal, Finance, Voice, Video, Board, Tasks, Memory, Skills, Knowledge Graph, Auth, Pricing, Scheduler, Always-Learn, Browser, MCP, Models, Observability, Team, Persistent Sandbox, RAG, Testing, Swarms, Guardrails, Handoffs, Offensive Security, Bug Bounty, Social Media, Content Factory, Meeting-to-Tasks, Report Generator, Legal Drafter, Workflow Builder, Image Generation, Exchange, Portfolio, Backtesting, Training, Moral Guardrails

## SDK

### Python
```python
from nordai import NordAI
ai = NordAI('http://localhost:8000', 'api-key')
response = ai.chat('Hello!')
```

### JavaScript
```javascript
import { NordAI } from './nordai.js';
const ai = new NordAI('http://localhost:8000', 'api-key');
const response = await ai.chat('Hello!');
```

## Final Stats
- 124 files
- 13383 lines of Python
- 88 modules
- 100+ endpoints
- 201 tests
- 0 bugs
- 0 project references
- 0 LLM brand names

## License
CC0-1.0
