# Day 02 — Conditionals (Decision Logic)  
(Applied to Automotive Center-Stack Stability Testing)

## 1. What This Concept Is

Conditionals (`if / elif / else`) encode **decision logic**.

They allow a system to:
- Inspect data
- Choose one execution path
- Enforce rules consistently

In stability testing, conditionals translate **testing rules into deterministic system behavior**.

---

## 2. Why This Matters in Real Systems

Without clear conditional logic:

- FAIL and CRASH are handled the same
- Retry logic becomes blind and unsafe
- Automation pipelines behave unpredictably
- Data corruption happens silently

In long-run center-stack stability testing, **decision logic controls safety and reliability**, not just flow.

---

## 3. Mental Model

Think of conditionals as **traffic signals for execution pipelines**.

Given a system state:
- PASS → continue execution
- FAIL → retry or log
- CRASH → halt and collect diagnostics
- UNKNOWN → flag data quality issue

Only **one path** should execute for a given state.

---

## 4. Conditionals in Center-Stack Stability Testing

Typical execution states in infotainment stability testing:

- PASS
- FAIL
- CRASH
- TIMEOUT
- UNKNOWN

Each state requires **different handling**, not just different labels.

Example (conceptual, not code):
- PASS → increment success metrics
- FAIL → retry within limits
- CRASH → stop test and preserve logs
- TIMEOUT → retry with escalation
- UNKNOWN → flag input data issue

---

## 5. Decision Logic vs Retry Logic

### Blind Retry (Incorrect)

- Retry every failure
- No distinction between failure types
- Masks real stability issues

### Decision-Driven Retry (Correct)

Retries depend on:
- Failure category
- Frequency
- Historical patterns

Conditionals enforce **controlled retries**, not blind loops.

---

## 6. Common Mistakes Testers Make

- Missing `else` branches (silent failures)
- Treating FAIL and CRASH as equivalent
- Hardcoding decisions instead of defining rules
- Case-sensitive status comparisons
- Mixing decision logic with logging or reporting

These mistakes scale poorly in long-run tests.

---

## 7. How Conditionals Enable Scalable Systems

Clear conditional logic is the foundation for:

- Failure classification
- Retry limits
- Metrics aggregation
- Auto-healing decision engines
- Predictive stability systems (later)

Machine Learning and AI **depend on correct decision logic**, they do not replace it.

---

## 8. Stability Testing Example (End-to-End Thinking)

In a 48-hour center-stack stability run:

- Occasional FAIL → acceptable noise
- Repeated FAIL → degradation
- Single CRASH → critical signal
- Repeated CRASH → systemic instability

Conditionals encode these distinctions so the system behaves **predictably and safely**.

---

## 9. Interview Perspective

> “In automotive center-stack stability testing, I use conditionals to encode
decision logic — not just control flow.  
They allow me to handle PASS, FAIL, CRASH, and unknown states deterministically,
which is critical for long-run execution safety and reliable data analysis.”
