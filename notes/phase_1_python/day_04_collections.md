# Day 04 — Collections  
(Dicts, Sets, and Structured Metrics)

## 1. What This Concept Is

Collections are data structures that allow you to:
- Group related data
- Aggregate results
- Enforce uniqueness
- Model real-world systems

In stability testing, collections are not optional —
they are the **foundation of metrics, analysis, and reporting**.

---

## 2. Why Collections Matter in Center-Stack Stability Testing

Automotive center-stack stability testing produces:
- Thousands of iterations
- Multiple failure types
- Repeated issues
- Long-run trends

Without proper collections:
- Metrics become fragile
- Data becomes inconsistent
- Analysis becomes impossible

Collections turn raw executions into **structured, meaningful data**.

---

## 3. Mental Model for Core Collections

### Lists
- Ordered sequence
- Allows duplicates
- Use for raw execution streams

Example:
- Sequence of test statuses over time

---

### Sets
- Unordered
- Enforces uniqueness
- Use for identifying unique failures

Example:
- Unique failure signatures observed in a run

---

### Dictionaries
- Key–value mapping
- Fast lookup and aggregation
- Backbone of metrics systems

Example:
- PASS / FAIL / CRASH counts
- Failure-type frequency

---

## 4. Choosing the Right Collection

| Problem | Collection |
|------|-----------|
| Track execution order | List |
| Count occurrences | Dictionary |
| Identify unique failures | Set |
| Nested metrics | Dictionary of dictionaries |

Wrong choice = fragile system.

---

## 5. Center-Stack Stability Examples

### Example 1: Status Aggregation
- Use a dictionary to count PASS / FAIL / CRASH
- Increment counts per iteration

---

### Example 2: Unique Failures
- Use a set to track unique failure reasons
- Prevent duplicate reporting

---

### Example 3: Combined Metrics
- Dictionary for counts
- Set for unique issues
- Both updated per iteration

This mirrors real stability dashboards.

---

## 6. Common Mistakes Testers Make

- Using lists for counts
- Using dictionaries without defaults
- Forgetting to initialize keys
- Mixing raw data with aggregated data
- Overwriting metrics instead of accumulating

These mistakes scale poorly.

---

## 7. How Collections Enable Advanced Systems

Correct collection usage enables:
- Reliable metrics
- Flakiness detection
- Trend analysis
- CSV / log parsing pipelines
- Visualization and ML later

Collections are the **bridge from execution to data science**.

---

## 8. Interview Perspective

> “In automotive center-stack stability testing, I use lists to preserve execution
order, dictionaries to aggregate metrics, and sets to track unique failures.
Choosing the right collection is a design decision, not a coding detail.”
