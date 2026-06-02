# SolveWorks Company Brain Brief

A pre-call briefing asset for prospects who are exploring practical AI agents for their business.

## Download

- [SolveWorks Company Brain Brief PDF](assets/solveworks-company-brain-brief.pdf)

## What this brief explains

Most businesses do not need another chatbot. They need an agent that starts with the right operating context: the sources, rules, approvals, tools, QA checks, and correction loops that make work safe and repeatable.

This brief introduces the SolveWorks approach:

- **Company Brain** — the context and source-truth layer around the agent.
- **Skillset Packs** — reusable workflow rules, prompts, runbooks, QA checks, examples, and tool commands.
- **Execution Surfaces** — briefs, dashboards, follow-up drafts, watchdogs, approval queues, research packets, and working outputs.
- **Safety + Receipts** — read-only/draft-first launches, permission ladders, QA checks, logs, and proof before expanded action.

## Brief bio

SolveWorks builds practical AI agents for real business workflows. We help owner-led companies turn scattered knowledge, repeated decisions, and manual follow-through into agent-assisted operating systems.

We are not here to sell generic automation. We build the working layer that makes agents useful, trusted, and improvable inside daily operations.

## Intended use

Send this PDF before a discovery call. It is designed to frame the conversation around the workflow, source systems, approval boundaries, and first useful pilot — not to replace a tailored proposal.

Pricing and implementation scope are intentionally not included in this pre-call brief.

## QA status

Final PDF QA completed:

- PDF opens successfully.
- 14 intentional, more spacious pages.
- No blank/orphan pages in contact-sheet QA.
- No obvious cut-off text, crowding, or spacing collisions after spacious rebuild.
- No browser header/footer artifacts in text-layer scan.
- No pricing leakage.
- Visual QA passed after Opus 4.8 copy edits, SolveWorks bio addition, and the final spacious 14-page rebuild.

## Repository contents

- `assets/solveworks-company-brain-brief.pdf` — final sendable PDF.
- `source/make_company_brain_pdf.py` — ReportLab source generator.
- `source/solveworks-company-brain-brief-copy.md` — extracted text copy for review/editing.
- `qa/contact-sheet.jpg` — visual QA contact sheet.
- `qa/opus-4-8-copy-review.md` — OpenRouter Opus 4.8 red-team copy review.

## Publishing

If you have GitHub CLI auth configured, publish with:

```bash
gh repo create solveworks-company-brain-brief --public --source . --push --description "SolveWorks Company Brain pre-call prospecting brief"
```

For a private sharing repo, use `--private` instead of `--public`.
