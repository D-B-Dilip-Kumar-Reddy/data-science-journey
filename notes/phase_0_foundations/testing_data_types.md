# Testing Data Types  
(Applied to Automotive Center-Stack Stability Testing)

## 1. Why Data Types Matter in Stability Testing

In stability testing, data types are **system design decisions**, not coding details.

Incorrect data types:
- Do not usually crash scripts
- Quietly corrupt analysis
- Produce misleading trends
- Hide root causes

In long-run automotive testing, **silent data corruption is more dangerous than test failures**.

---

## 2. Core Principle

> **Data types define what questions you are allowed to ask of the system.**

If data types are wrong:
- Aggregation becomes invalid
- Correlation becomes impossible
- Trends become misleading
- ML (if used later) becomes meaningless

---

## 3. Stability Failures as Typed Signals

Center-stack stability issues are **not generic failures**.
Each represents a **different signal category** and must be typed correctly.

### Failure Signal Categories

| Category | Examples |
|------|--------|
| Execution-level | PASS, FAIL, TIMEOUT |
| System crashes | ANR, Tombstone, Logcat crash, QNX crash |
| Resource degradation | Memory growth, process duplication |
| UX / behavioral | Black screen, frozen UI, UI mismatch |
| Lifecycle | Unexpected reboot, boot count increase |

Each category has **different data-type requirements**.

---

## 4. Recommended Data Types (Real Stability Context)

| Signal | Correct Data Type | Why |
|----|------------------|----|
| Test status | Categorical (string / enum) | Finite states |
| Failure type | Categorical (string / enum) | ANR ≠ Tombstone ≠ Reboot |
| Crash source | Categorical | Android / Guest / QNX |
| Process name | String | Identifier |
| Memory usage (MB) | Float | Trend & threshold analysis |
| CPU usage (%) | Float | Correlation with freezes |
| Process count | Integer | Detect duplication |
| UI state | Categorical | BLACK / FROZEN / RESPONSIVE |
| Boot count | Integer | Detect unexpected restarts |
| Reboot detected | Boolean | Critical lifecycle signal |
| Timestamp | Datetime | Time-series analysis |
| Iteration number | Integer | Execution ordering |
| Log snippet | String (text) | Unstructured evidence |

---

## 5. Mental Model for Choosing Data Types

Before choosing a data type, ask:

1. Will this value **increase/decrease over time**?
2. Will I **count occurrences** of this?
3. Will I **compare it against thresholds**?
4. Will I **group or classify** by this?
5. Is this **evidence**, not a metric?

Your answers dictate the correct type.

---

## 6. Examples From Real Stability Issues

### Example 1: Memory Growth

❌ Wrong  
- `"850 MB"` (string)

Problems:
- Cannot compute growth rate
- Cannot compare thresholds
- Cannot detect leaks

✅ Correct  
- `850.0` (float, MB)

---

### Example 2: Failure Classification

❌ Wrong  
- `FAIL` for everything

Problems:
- ANR and reboot appear identical
- Severity is lost

✅ Correct  
- `status = FAIL`
- `failure_type = ANR`

---

### Example 3: Boot Tracking

❌ Wrong  
- Boolean reboot flag only

Problems:
- Cannot detect repeated reboots

✅ Correct  
- `boot_count` as integer
- Compare across iterations

---

## 7. Common Data-Type Mistakes in Stability Testing

- Storing numeric metrics as strings
- Mixing failure type with execution status
- Treating all crashes the same
- Ignoring time as a data dimension
- Overloading a single variable with multiple meanings

These mistakes scale badly in long-run systems.

---

## 8. How Correct Data Types Enable Advanced Analysis

Correct data typing enables:
- Memory leak detection
- ANR frequency over uptime
- Crash clustering
- Correlation between UI freezes and resource usage
- Reboot root-cause analysis

Without correct data types, none of these are reliable.

---

## 9. Relationship to Data Science & ML

Machine Learning **does not fix bad data types**.

ML assumes:
- Consistent types
- Meaningful categories
- Correct numeric representations

In stability testing:
> **Data typing comes before aggregation, visualization, or modeling.**

---

## 10. Interview Perspective

> “In automotive center-stack stability testing, choosing correct data types is a
design decision. Each failure signal — ANR, tombstone, reboot, or UI freeze —
must be represented distinctly to enable accurate trend and root-cause analysis.”
