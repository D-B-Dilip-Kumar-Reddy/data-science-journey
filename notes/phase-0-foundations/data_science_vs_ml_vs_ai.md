# Data Science vs Machine Learning vs Artificial Intelligence

## 1. What These Terms Mean

**Data Science**
- Extracting insights from data
- Cleaning, analyzing, summarizing, and visualizing data
- Often descriptive and diagnostic

**Machine Learning**
- Subset of Data Science
- Uses data to learn patterns automatically
- Focuses on prediction and generalization

**Artificial Intelligence**
- Broad umbrella
- Systems that mimic intelligent behavior
- ML is one way to build AI systems

---

## 2. Why This Distinction Matters

Confusing these terms leads to:
- Overengineering simple problems
- Using ML where simple analysis is enough
- Poor problem framing

Most real-world problems start as **Data Science problems**, not ML problems.

---

## 3. Mental Model

- Data Science → *Understand what happened*
- Machine Learning → *Predict what will happen*
- AI → *Act intelligently based on predictions*

---

## 4. Application to Stability Testing

| Problem | Correct Approach |
|------|----------------|
| Crash frequency over time | Data Science |
| Flaky test detection | Data Science + rules |
| Predict next failure | Machine Learning |
| Auto-healing test pipelines | AI system |

---

## 5. Common Mistakes

- Jumping to ML without understanding data
- Treating analytics dashboards as ML
- Assuming AI is required for automation

---

## 6. Interview Perspective

> “Most testing problems are data science problems first.  
I only consider ML after establishing stable patterns and clean data.”
