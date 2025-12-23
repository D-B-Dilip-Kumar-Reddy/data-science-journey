# Day 01 — Variables and Data Types

## 1. What This Concept Is

Variables are named references to data in memory.  
Data types define what kind of data is stored and what operations are valid on it.

Together, they form the foundation of all data processing systems.

---

## 2. Why This Matters in Real Systems

Incorrect data types cause:
- Invalid comparisons
- Broken aggregations
- Incorrect metrics
- Silent data corruption

In data systems, **wrong data types are more dangerous than syntax errors**, because they often go unnoticed.

---

## 3. Mental Model

- Variable → labeled container
- Data type → contract that defines allowed operations

Choosing a data type is a **design decision**, not a syntax detail.

---

## 4. Application to Stability Testing

| Testing Artifact | Correct Data Type | Reason |
|------------------|------------------|--------|
| Test ID | String | Identifier |
| Iteration number | Integer | Discrete count |
| Execution time | Float | Precision |
| Test status | String / Enum | Categorical |
| Crash count | Integer | Aggregation |
| Log output | String (text) | Unstructured |

Incorrect types break downstream analysis.

---

## 5. Common Mistakes

- Storing numeric values as strings
- Comparing floats using equality
- Using lists instead of dictionaries for metrics
- Mixing multiple meanings in a single variable

---

## 6. Interview Perspective

> “Data type selection is a core design decision.  
If data types are wrong, no amount of analysis can fix the results.”
