# Data Thinking for Test Engineers

## 1. What Is Data Thinking?

Data thinking means:
- Viewing executions as data points
- Treating failures as categories, not events
- Looking for trends, not individual outcomes

---

## 2. Why Testers Struggle with Data

Testing focuses on:
- Immediate correctness
- Binary outcomes

Data focuses on:
- Aggregates
- Distributions
- Trends over time

---

## 3. Mental Model

A single test failure is noise.  
Hundreds of executions reveal patterns.

---

## 4. Stability Testing Mapping

| Testing Concept | Data Representation |
|---------------|-------------------|
| Test run | Row |
| Iteration | Index / ID |
| Status | Categorical variable |
| Execution time | Numeric (float) |
| Crash | Separate failure class |

---

## 5. Common Mistakes

- Treating FAIL and CRASH as the same
- Ignoring execution time trends
- Overreacting to single failures

---

## 6. Interview Perspective

> “I approach testing data statistically, not emotionally.  
One failure means nothing; trends mean everything.”
