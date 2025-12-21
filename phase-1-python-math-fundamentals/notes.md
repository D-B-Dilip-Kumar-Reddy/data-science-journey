# Day 1 — Variables, Data Types & Mental Model

## 1. Variables (Correct Mental Model)
A variable is a **name that references an object in memory**, not a container.

```python
a = "FAIL"
b = a
```

Both `a` and `b` reference the same object.

### Why this matters
- Explains shared-state bugs
- Important when using lists and dictionaries
- Critical for parsing and aggregating stability test data

---

## 2. Core Data Types

| Type  | Example | Stability Testing Usage |
|------|--------|-------------------------|
| int  | 120    | iteration count |
| float | 4.67  | execution time |
| str  | "CRASH" | result, error message |
| bool | True   | flags and decisions |

---

## 3. Container Data Types

### list
- Ordered
- Allows duplicates

```python
results = ["PASS", "FAIL", "PASS"]
```

**Use for:**
- Iteration timelines
- Ordered execution results

---

### tuple
- Ordered
- Immutable

```python
resolution = (1920, 1080)
```

**Use for:**
- Fixed configuration values

---

### set
- Unordered
- Stores only unique values

```python
unique_errors = {"TIMEOUT", "MEMORY_LEAK"}
```

**Use for:**
- Deduplicating failures
- Identifying unique error types

---

### dict
- Key–value structure
- Most important structure in Data Science

```python
summary = {"PASS": 10, "FAIL": 2}
```

**Use for:**
- Result aggregation
- Metrics
- Reports
- JSON / CSV data

---

## 4. Mutability

| Type | Mutable |
|----|----|
| int, float, str, tuple | No |
| list, set, dict | Yes |

Mutable objects can change in place and cause hidden bugs if shared.

---

## 5. Why Floats Are Approximate

Floats are stored in binary format.  
Many decimal values cannot be represented exactly.

```python
0.1 + 0.2
```

Output

```python
0.30000000000000004
```

### Rules
- ❌ Never compare floats using `==`
- ✅ Always use thresholds or rounding

---

## 6. Result Aggregation

Result aggregation means converting raw execution data into summaries.

### Raw data
```python
["PASS", "FAIL", "PASS"]
```

### Aggregated data
```python
{"PASS": 2, "FAIL": 1}
```
Aggregation turns logs into insights.

## 7. Why Dicts Are the Backbone of Data Science

- Real-world data is key–value based
- Natural fit for metrics and reports
- Enables easy aggregation
- Powers Pandas, JSON, and ML configurations
