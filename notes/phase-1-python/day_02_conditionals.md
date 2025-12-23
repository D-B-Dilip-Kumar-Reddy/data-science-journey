# Day 02 — Conditionals (Decision Logic)

## 1. What This Concept Is

Conditionals (`if / elif / else`) encode **decision logic**.
They allow software to choose different execution paths based on data.

In testing systems, conditionals translate **rules into actions**.

---

## 2. Why This Matters in Real Systems

Without conditionals:
- All failures look the same
- Crashes are mishandled
- Retry logic is impossible
- Automation pipelines become brittle

Conditionals control:
- Flow
- Error handling
- Data classification

---

## 3. Mental Model

Conditionals are **traffic signals for execution**.

Given a state:
- PASS → proceed
- FAIL → log and continue
- CRASH → stop and capture diagnostics

Only one path should execute at a time.

---

## 4. Application to Stability Testing

Typical decision states:
- PASS
- FAIL
- CRASH
- TIMEOUT
- UNKNOWN

Each requires **different handling**.

Example logic (conceptual):
- PASS → increment pass count
- FAIL → retry or log
- CRASH → halt execution and capture data
- UNKNOWN → flag data quality issue

---

## 5. Common Mistakes

- Missing `else` branches (silent failures)
- Treating FAIL and CRASH as identical
- Hardcoding logic instead of defining rules
- Case sensitivity issues in status values

---

## 6. Interview Perspective

> “Conditionals allow me to convert real-world testing rules into deterministic execution logic.  
I use them to control flow, classify outcomes, and enforce safety in pipelines.”
