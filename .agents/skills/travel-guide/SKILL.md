---
name: travel-guide
description: Research, plan, audit, and revise personalized travel guides, especially international itineraries. Use for destination choices, day-by-day routes, visas and connectivity, multimodal transfers, payments, hotel/airfare comparison, cross-platform reviews, traveler interviews, or trip disruptions. 支持中英双语旅游攻略、海外实测与多平台评价对照。
---

# Travel Guide / 深度旅游攻略

Respond in the user's requested language or match the language of their request (English or Simplified Chinese). Produce a bilingual guide when requested. Keep local names and searchable addresses for navigation. Use local dates and times, and make time zones and date changes explicit on cross-border or overnight legs.

## Match the task

- **Choose a destination.** Compare a few candidates by interests, season, door-to-door cost and time, usable days, and material constraints. If dates are flexible, compare windows and sketch the leading route.
- **Plan a trip.** Lock booked flights, stays, tickets, and traveler constraints first. Separate requirements, priorities, and flexible extras. Identify origin, dates, travelers, budget scope, interests, and pace. Ask about passport nationality/type or residency only when it changes cross-border eligibility. Ask only for details that change the plan. Use explicit assumptions or conditional branches for the rest.
- **Audit or replan.** Keep valid commitments. Recompute downstream travel, costs, cancellations, and bookings after changes. During a disruption, lead with what to do now, the latest decision time, and a route back.

## Personalize before committing the route

Use the [traveler interview / 旅行需求访谈](references/traveler-interview.md) for personalized plans. Ask the few decision-changing questions that are ready now, then use the answers to choose the next round. For group trips, track each person's hard limits separately from preferences. Screen shared plans and backups for food allergies, activity restrictions and access needs. Keep unresolved safety constraints conditional and offer a workable fallback.

## Full international guides

Use [international field guide, EN](references/international-planning.en.md) or [出境旅行实务手册，中文](references/international-planning.md). Cover visas/transit, connectivity, every transport leg, payments and cash, area-first lodging, comparable airfare, food-first dining, and activities/packing/health. Apply this full scope when the user requests a complete overseas guide. For narrower questions, use only the relevant modules. Where a map shows no transit, continue with local operators, airport/port and tourism-board sources. Resolve scarce or unusual transfers before committing the route. Distinguish unknowns from verified facts and give a next step for each material gap.

## Research, plan, and check

1. For destination comparisons and full trips, run [destination discovery / 全球目的地排查](references/destination-discovery.md) before routing. Use the itinerary triggers even for countries absent from the examples. Proactively surface local experiences, logistics gaps, rules, hidden costs, and seasonal dependencies the traveler may have missed. Verify trip-breaking conditions first: entry and transit, permit eligibility, closures, ticket windows, and sparse return transport. Research current facts online. Prefer authorities and operators for rules and logistics. See [research and audit, EN](references/research-and-audit.en.md) or [核验与审查，中文](references/research-and-audit.md).
2. For consequential recommendations such as hotels, restaurants, and attractions, compare firsthand accounts for the **same venue or branch** across accessible platforms. Include destination forums, maps/reviews, and local-language sources where useful. Synthesize recurring strengths, recurring issues, and meaningful disagreements by traveler profile and visit conditions. Use the [community evidence protocol / 多平台评价规则](references/community-evidence.md), including fallback when sites are inaccessible.
3. Set arrival and departure gateways, lodging bases, and nights. Build around fixed bookings, operating hours, and daylight. Group stops geographically. Check each critical leg door to door, including walks, waits, queues, transfers, meals, and rest. Back-plan from last admission, reserved slots, and last departures. Prepare a reachable fallback with a clear switching trigger for vulnerable anchors.
4. Reconcile total and per-person costs, shared costs, paid vs. outstanding, currency, taxes, and quote dates. Order reservations by deadline and dependencies. Distinguish verified availability from confirmed bookings and future release windows. Planning is read-only; purchases, applications, bookings, and cancellations require explicit authorization.
5. Audit feasibility before delivery. Put unverified critical legs up front with a recheck deadline and an alternative. Use [deliverables, EN](references/deliverables.en.md) or [攻略交付模板，中文](references/deliverables.md). Match detail to the decision and keep the daily mobile card consistent with the full guide.
