# Common Pitfalls When Moving from Testing to Data Science

## 1. Treating All Failures the Same

FAIL ≠ CRASH  
CRASH requires separate handling and metrics.

---

## 2. Ignoring Edge Cases

- Empty executions
- Partial runs
- Incomplete logs

Ignoring these leads to silent data corruption.

---

## 3. Overusing Automation Logic

Hardcoded logic breaks when scale increases.
Rule-based thinking must evolve into data-driven thinking.

---

## 4. Mixing Logic and Reporting

Analysis logic and reporting should be separated.
This improves maintainability and reuse.

---

## 5. Interview Perspective

> “Most data bugs come from assumptions, not code.”
