---
name: travel-guide
description: Research, plan, audit, and revise personalized travel itineraries. Use for destination comparisons, international trip logistics, budgets, reservations, travel disruptions, or editable itinerary mind maps. 支持中文与英文旅行规划。
---

# Travel Guide / 深度旅游攻略

Match the user's language and requested scope. Keep local names searchable and use local dates, time zones and overnight date changes explicitly.

## Choose the mode and load only what it needs

| Request | Read first | Add when relevant |
| --- | --- | --- |
| Compare destinations | [Discovery](references/destination-discovery.md), [budget/value](references/budget-and-value.md) | [Community evidence](references/community-evidence.md) for consequential picks |
| Full itinerary | [Ordered workflow](references/planning-workflow.md), [interview](references/traveler-interview.md) | [International field guide](references/international-planning.md) or [English](references/international-planning.en.md) for overseas trips |
| Continue or combine past plans | [Continuity and privacy](references/continuity-and-long-routes.md) | Workflow stages affected by the changes |
| Audit or disruption | [Research/audit](references/research-and-audit.md) or [English](references/research-and-audit.en.md) | Relevant transport, budget and booking dependencies |
| Deliver files or revise an artifact | [File delivery](references/file-delivery.md) | [Mind-map standard](references/mind-map.md) only when a map is requested |

Use the linked references as task-specific procedures, not a checklist to load in full for every question. Narrow questions need only relevant modules.

## Personalization boundary

Treat this as a general-purpose skill for different travelers. Discover interests in the interview; no activity, equipment, travel style, destination or spending tier is a default personal profile. Load specialized activity guidance only when the current traveler requests it or the chosen route requires it. Missing interests stay unknown. Prior answers belong only to that traveler and trip.

Repository maintenance publishes reusable procedures, not the owner's preferences, chat-derived examples or completed itineraries. Do not turn private trip details into templates, fixtures, evaluation prompts, documentation, PR descriptions or commit messages. Use independently constructed synthetic cases.

## Decision rules

1. Restore booked commitments and the latest explicit user decisions. Separate hard constraints, preferences, exclusions and unresolved conditions; do not transfer assumptions between trips. Ask only questions that change the decision, using conditional options for remaining gaps. Check each traveler's relevant food, activity and access limits.
2. Check trip-breaking entry/transit, safety, permits, seasonal closures and scarce connections before detailed routing. Research current facts from authorities and operators. Distinguish verified fact, estimate, experience lead, pending confirmation, available inventory and booked order. Every consequential unknown needs an impact, verification route and recheck trigger.
3. For full routes, discover local opportunities and hidden costs before committing. Compare door-to-door alternatives within the budget; include walking, queues, baggage, transfers, meals and rest. Give every night a location, protect core experiences, and back-plan from hard deadlines. Unknown map routes require local operator/airport/port research.
4. For key venues, compare the same place/branch across accessible firsthand sources using [community evidence](references/community-evidence.md). Preserve meaningful disagreement and use accessible fallbacks. Rules and live logistics still need authoritative evidence.
5. Reconcile original currency, units, shared costs, taxes, quote dates, paid/outstanding and contingency. Use [budget/value](references/budget-and-value.md) and [price pitfalls](references/price-pitfalls.md). Redesign an over-budget route around core experiences before merely reducing comfort.
6. Preserve exclusions in main and fallback plans. A fallback needs a switching trigger, latest decision time, reachable route and downstream order/cost effects. In a disruption lead with the immediate action and return path.

## Output contract

Use [Chinese deliverables](references/deliverables.md) or [English deliverables](references/deliverables.en.md). Scale detail to the request. Full plans include a decision brief, daily route, transport/lodging decisions, reproducible budget, booking/recheck dependencies and operational fallbacks. Mark unresolved critical dependencies as a research-stage plan.

Keep summary, daily cards and files consistent through stable record IDs. Create itinerary files only when requested. When revising an identified artifact, read the user's latest source and preserve unrelated edits. Maps use separately editable nodes, activity-adjacent prices, exterior connector routing, and both clickable draw.io and HTML entries; apply the detailed mind-map standard.

Research does not authorize purchases, applications, bookings or cancellations. Keep real trip records, exact future movements, health/identity information and orders private; public improvements contain generic methods or synthetic cases. Never report an artifact or booking as delivered unless it actually exists.

## Maintaining this skill

Run `python3 scripts/validate_skill.py` from the repository root after structural changes. Use the synthetic scenarios in `evals/scenarios.md` for behavioral reviews; static validation does not establish itinerary feasibility or model quality.
