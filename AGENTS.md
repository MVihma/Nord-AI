# Nord AI v5 — Agent Configuration

## Project Overview
Nord AI is an autonomous multi-agent system with 8 specialized agents, 54 modules, Theory of Mind, WASI sandbox, parallel reasoning, cognitive memory, and 8 international security standards.

## Tech Stack
- **Backend**: Python 3.12+, FastAPI, SQLite (WAL mode)
- **Frontend**: HTML + Tailwind CSS (CDN)
- **LLM**: Provider-agnostic API
- **Security**: Fernet encryption, HMAC audit, JWT auth, capability sandbox
- **Testing**: pytest

## Commands
| Command | Purpose |
|---------|---------|
| `pip install -r requirements.txt` | Install dependencies |
| `python main.py` | Start the server |
| `pytest tests/` | Run all tests |
| `docker-compose up -d` | Start with Docker |

## Architecture
- Orchestrator pattern: Lead agent routes to specialists with Confidence Router
- Cognitive memory: Episodic (WHEN/WHERE/WHY) + Semantic + Knowledge Graph + Theory of Mind
- WASI sandbox: Capability-based permissions + leak detection
- Audit-first design: HMAC-signed chain logging
- Parallel reasoning: 6 tracks (INDUCT/ANALOG/COMMON/META/SIM/DIV)
- Self-evolving: Tournament-style memory strategy evolution
- Failure attribution: Multi-perspective debugging

## Security Standards
OWASP Top 10, GDPR (EU 2016/679), EU AI Act (2024/1689), ISO 27001, SOC 2, NIST CSF, NIST AI RMF, CIS Controls v8

## Key Modules (54)
- `backend/main.py` — FastAPI server (all endpoints)
- `backend/config.yaml` — Model and security configuration
- `backend/agents/` — 8 agents (orchestrator, researcher, coder, analyzer, security, writer, devops, reviewer)
- `backend/security/` — Auth, rate limiting, PII, encryption, GDPR/AI Act
- `backend/memory/` — Episodic + semantic memory with RRIF scoring
- `backend/ironclaw_sandbox/` — Capability-based permissions, leak detection
- `backend/wasi_sandbox/` — Token budget, time-travel debug, human-in-loop
- `backend/theory_of_mind/` — Theory of Mind agents (ToM/Domain/Response)
- `backend/parallel_reasoning/` — 6 parallel reasoning tracks
- `backend/episodic_memory/` — WHEN/WHERE/WHY + 9-step workflow
- `backend/meta_evolution/` — Self-evolving memory strategies
- `backend/workspace_isolation/` — Isolated workspaces per user
- `backend/benchmark/` — 6-dimension security evaluation
- `backend/failure_attribution/` — Multi-perspective debugging
- `backend/board/` — C-Suite board review (8 roles)
- `backend/auth/` — JWT multi-user authentication
- `backend/pricing/` — Free/Pro/Enterprise tiers
- `backend/scheduler/` — CRON scheduling
- `backend/voice/` — Speech-to-text voice input (99 languages)
- `backend/finance/` — 8 financial analysis skills
- `backend/research_loop/` — Autonomous experiment loop
- `backend/video/` — AI video generation pipeline
- `backend/browser/` — Playwright browser automation
- `backend/browser_use/` — Browser automation integration
- `backend/knowledge_graph/` — Entity-relation graph
- `backend/skills/` — 18 built-in + custom skill creator
- `backend/tasks/` — Project checklist + milestones
- `backend/compliance/` — Audit log + cost tracker
- `backend/sandbox/` — Python code sandbox
- `backend/cognitive_memory/` — Memory/Narrative/Identity agents
- `backend/security_bench/` — Security testing
- `backend/legal/` — EU + Nordic + Swedish law
- `backend/always_learn/` — Permanent learning system
- `backend/evolving_memory/` — Self-evolving instincts
- `backend/persistent_sandbox/` — Sleep/wake sandbox
- `backend/mcp_integration/` — MCP tool integration
- `backend/team_collab/` — Multi-user collaboration
- `backend/observability/` — Span-based tracing
- `backend/code_feedback/` — Code execution feedback loop
- `backend/browser_automation/` — Browser automation
- `backend/trivy_scanner/` — Security scanning
- `backend/version_memory/` — Version-controlled memory
- `backend/multi_arch/` — 5 agent architectures
- `backend/internet_access/` — Web scraping, RSS
- `backend/self_healing/` — Self-healing agent graphs
- `backend/guardrails/` — 4-layer prompt injection defense
- `backend/agent_handoffs/` — Agent-to-agent communication
- `backend/security_bench_eval/` — Cybersecurity benchmark
- `backend/offensive_security/` — Penetration testing
- `backend/bug_bounty/` — Bug bounty reporting
- `backend/rag_pipeline/` — Retrieval-augmented generation
- `backend/agent_testing/` — Agent testing framework
- `backend/event_mesh/` — Event-driven orchestration
- `backend/tests/` — 40+ unit tests
- `frontend/index.html` — Dark-mode dashboard (8 modes)
- `site/` — Landing page, documentation, blog post
- `sdk/` — Python + JavaScript SDK
