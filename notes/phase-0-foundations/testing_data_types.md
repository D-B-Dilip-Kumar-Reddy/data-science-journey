# Testing Data Types and Their Meaning

## 1. Why Data Types Matter

Incorrect data types lead to:
- Wrong aggregations
- Broken comparisons
- Invalid conclusions

---

## 2. Common Testing Data Types

| Data | Correct Type | Reason |
|----|-------------|------|
| Test status | String / Enum | Categories |
| Execution time | Float | Precision |
| Iteration count | Integer | Discrete |
| Crash count | Integer | Aggregation |
| Log message | Text | Unstructured |

---

## 3. Mental Model

Data types define:
- What operations are allowed
- What conclusions are valid

---

## 4. Stability Testing Example

Execution time must be a float.
Storing it as a string breaks:
- Threshold checks
- Averages
- Trend analysis

---

## 5. Common Mistakes

- Comparing floats using equality
- Using lists where dictionaries are needed
- Encoding numeric values as strings

---

## 6. Interview Perspective

> “Choosing the correct data type is the first step toward correct analysis.”
