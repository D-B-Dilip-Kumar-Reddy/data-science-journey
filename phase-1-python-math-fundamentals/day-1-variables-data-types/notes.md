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

## 8. Mental Models for Data Types (How to Choose Correctly)

| Data Type | Mental Model | Think of it as | When to Use (Real/Test Scenarios) | When NOT to Use |
|----------|-------------|---------------|----------------------------------|-----------------|
| int | Counter | A tally | Iteration count, retry count, failure count | For measurements with decimals |
| float | Measurement | Approximate value | Execution time, CPU usage, memory usage | Exact comparisons or IDs |
| str | Label | Human-readable tag | Test result ("PASS"), error message, test name | Numeric operations |
| bool | Switch | Yes / No flag | Crash occurred, retry needed, test enabled | Multiple states |
| list | Timeline | Ordered sequence | Execution results per iteration, ordered logs | When uniqueness matters |
| tuple | Fixed config | Locked group | Resolution, constant settings | Data that may change |
| set | Uniqueness filter | Deduplicator | Unique failure types, distinct errors | Ordered data |
| dict | Structured record | Labeled container | Aggregated results, metrics, reports | Simple sequences |

---

### Decision Shortcuts (Very Important)

- **Do I care about order?** → `list`
- **Must values never change?** → `tuple`
- **Do I need uniqueness only?** → `set`
- **Do I need labels + values?** → `dict`
- **Am I counting?** → `int`
- **Am I measuring?** → `float`
- **Am I labeling?** → `str`
- **Is it a yes/no decision?** → `bool`

---

### Interview-Level Rule
> Choosing the right data type shows **data thinking**, not just coding ability.

## 9. Common Mistakes Testers Make When Choosing Data Types

Choosing the wrong data type often leads to incorrect analysis, hidden bugs, and poor scalability.
Below are the most common mistakes seen in real test and execution data.

---

### 1. Using `list` When `dict` Is Required

**Mistake**
```python
results = ["PASS", "FAIL", "CRASH"]
```

**Problem**
- No counts
- No structure
- Hard to generate reports

**Correct**
```python
summary = {"PASS": 10, "FAIL": 2, "CRASH": 1}
```

**Rule**
> If data needs labels or aggregation, use a `dict`.

---

### 2. Comparing Floats Using `==`

**Mistake**
```python
if execution_time == 0.3:
    pass
```

**Problem**
- Float precision errors
- False failures in analysis

**Correct**
```python
if abs(execution_time - 0.3) < 0.01::
    pass
```

**Rule**
> Floats represent measurements, not exact values.

---

### 3. Using `str` for Numeric Values

**Mistake**
```python
iteration = '100'
```

**Problem**
- Cannot perform math
- Sorting behaves incorrectly

**Correct**
```python
iteration = 100
```

**Rule**
> Numbers should be numeric, not strings.

---

### 4. Using `list` Instead of `set` for Uniqueness

**Mistake**
```python
errors = ["TIMEOUT", "TIMEOUT", "MEMORY_LEAK"]
```

**Problem**
- Duplicate data
- Extra cleanup required

**Correct**
```python
errors = {"TIMEOUT", "MEMORY_LEAK"}
```

**Rule**
> If duplicates have no meaning, use a `set`.

---

### 5. Accidental Mutation of Shared Objects

**Mistake**
```python
a = []
b = a
b.append("FAIL")
```

**Problem**
- Hidden side effects
- Difficult debugging

**Correct**
```python
b = a.copy()
```

**Rule**
> Be careful with mutable objects (`list`, `dict`, `set`).

---

### 6. Using `tuple` for Data That Changes

**Mistake**
```python
config = (1920, 1080)
config[0] = 1280
```

**Problem**
- Raises errors
- Wrong mental model

**Correct**
```python
config = [1920, 1080]
```

**Rule**
> Use `tuple` only for fixed, unchanging data.

---

### 7. Using `bool` for Multiple States

**Mistake**
```python
status = True
```

**Problem**
- Meaning is unclear
- Cannot represent multiple outcomes

**Correct**
```python
status = "FAIL"
```

**Rule**
> Use `bool` only for yes/no decisions.

---

### 8. Storing Structured Data Without Structure

**Mistake**
```python
data = [101, "FAIL", 4.6]
```

**Problem**
- Meaning depends on position
- Hard to read and maintain

**Correct**
```python
data = {
    "iteration": 101,
    "status": "FAIL",
    "duration": 4.6
}
```

**Rule**
> If data has meaning, give it labels using a `dict`.

---

### 9. Overusing a Single Data Type Everywhere

**Mistake**
- Everything stored as `list`
- Everything stored as `dict`

**Problem**
- Poor design
- Harder analysis and maintenance

**Correct**
- Combine data types based on behavior

**Rule**
> Data behavior should drive data type choice.

---

### Interview-Level Insight

Choosing the right data type shows **data thinking**, not just coding ability.
It is a design decision, not an implementation detail.

## 10. Quick Decision Cheat Sheet — Choosing the Right Data Type

Use this sheet when you are unsure which data type to choose.

---

### Core Questions → Data Type

- **Am I counting something?** → `int`
- **Am I measuring something?** → `float`
- **Is this a human-readable label or message?** → `str`
- **Is this a yes / no decision?** → `bool`
- **Does order matter?** → `list`
- **Must the data never change?** → `tuple`
- **Do I only care about uniqueness?** → `set`
- **Do I need labels mapped to values?** → `dict`

---

### Common Test Data Scenarios

| Scenario | Correct Type | Why |
|--------|--------------|-----|
| Iteration number | `int` | Counting executions |
| Execution time | `float` | Measurement with tolerance |
| Test result | `str` | Multiple possible outcomes |
| Crash occurred | `bool` | Binary decision |
| Execution history | `list` | Order matters |
| Fixed configuration | `tuple` | Prevents mutation |
| Unique failure types | `set` | Removes duplicates |
| Aggregated results | `dict` | Labeled metrics |

---

### Fast Elimination Rules

- If **order matters** → never use `set`
- If **values must not change** → avoid `list`
- If **you need aggregation** → avoid `list`, use `dict`
- If **precision matters** → never compare `float` using `==`
- If **data has meaning** → avoid positional lists

---

### One-Line Rule (Interview Gold)

> Choose the data type based on **how the data behaves**, not how it looks.
