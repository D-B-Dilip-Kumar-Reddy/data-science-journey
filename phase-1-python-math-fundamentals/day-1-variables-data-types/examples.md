# Day 1 — Examples

## Variable Reference
```python
a = "PASS"
b = a
print(a, b)
```

---

## Float Precision
```python
print(0.1 + 0.2)
```

---

## Mutable vs Immutable Example
```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

---

## List Example
```python
results = ["PASS", "FAIL", "CRASH"]
```

---

## Tuple Example
```python
resolution = (1920, 1080)
```

---

## Set Example
```python
errors = {"TIMEOUT", "DISCONNECT"}
```

---

## Dict Example
```python
summary = {
    "PASS": 120,
    "FAIL": 5,
    "CRASH": 2
}
```

---

## Type Checking
```python
isinstance(results, list)
isinstance(summary, dict)
```