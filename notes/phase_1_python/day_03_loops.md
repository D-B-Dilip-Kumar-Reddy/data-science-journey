# Day 03 — Loops  
(Batch Execution, Retries, Aggregation Over Time)

## 1. What This Concept Is

Loops allow a system to **repeat execution in a controlled way**.

In stability testing, loops are not about repetition for convenience.
They represent:
- Time progression
- System evolution
- Continuous data generation

Without loops, stability testing cannot exist.

---

## 2. Why Loops Matter in Center-Stack Stability Testing

Automotive center-stack stability testing typically involves:
- Hundreds or thousands of iterations
- Long uptime (24–72 hours)
- Gradual degradation
- Intermittent failures

Loops make it possible to:
- Observe trends
- Detect degradation
- Aggregate metrics
- Apply controlled retries

---

## 3. Mental Model

**One loop iteration = one system snapshot**

Each iteration contributes:
- A status (PASS / FAIL / CRASH)
- Execution context
- A new data point

The goal is not “run until failure” but “observe behavior over time”.

---

## 4. Batch Execution

Batch execution means running the **same logical test repeatedly** while:
- Preserving execution order
- Recording every result
- Building a dataset incrementally

Batch execution converts tests into data.

---

## 5. Retries Are Loops With Rules

### Incorrect (Blind Retry)
- Retry every failure
- No retry limit
- Masks instability

### Correct (Controlled Retry)
Retries depend on:
- Failure type
- Retry count
- Severity

CRASH should never be retried.
FAIL and TIMEOUT may be retried with limits.

---

## 6. Aggregation Over Time

Loops enable aggregation such as:
- PASS / FAIL / CRASH counts
- Failure rate
- Retry frequency
- Stability trends

Aggregation is incremental — data is **accumulated**, not overwritten.

---

## 7. Common Mistakes

- Breaking the loop on first failure
- Infinite retries
- Overwriting metrics instead of aggregating
- Mixing execution, decision logic, and reporting

These mistakes eliminate long-run insight.

---

## 8. Interview Perspective

> “In automotive center-stack stability testing, loops represent time and system
evolution. I use them to collect data, enforce retry rules, and analyze stability
trends across long-run executions.”
