# Common Testing Pitfalls  
(Applied to Automotive Center-Stack Stability Testing)

## 1. Treating Stability as PASS / FAIL

### The Pitfall
Reducing all outcomes to PASS or FAIL.

### Why This Is Wrong
Center-stack stability failures are **multi-layer signals**:
- ANR ≠ Tombstone ≠ Reboot
- UI freeze ≠ Memory leak
- QNX crash ≠ Android app crash

Collapsing them into FAIL destroys severity, causality, and trend visibility.

### Correct Thinking
Separate:
- Execution status (PASS / FAIL / TIMEOUT)
- Failure type (ANR, Tombstone, QNX crash, etc.)

---

## 2. Treating All Crashes the Same

### The Pitfall
Handling ANRs, tombstones, logcat crashes, and QNX crashes identically.

### Why This Is Dangerous
Each crash originates from a **different layer**:
- ANR → responsiveness / scheduling
- Tombstone → native crash
- Guest crash → application-level
- QNX crash → system-level instability

Treating them the same leads to wrong conclusions and incorrect recovery actions.

### Correct Thinking
Model crash type explicitly and escalate based on severity.

---

## 3. Ignoring Time and Uptime

### The Pitfall
Analyzing failures without considering:
- Iteration number
- Uptime
- Order of execution

### Why This Fails
Most stability issues are **temporal**:
- Memory grows slowly
- Process duplication accumulates
- Crashes appear only after long uptime

Without time, patterns look random.

### Correct Thinking
Treat every execution as a time-series data point.

---

## 4. Overreacting to Single Failures

### The Pitfall
Stopping tests or escalating after one failure.

### Why This Is Inefficient
- Stability systems produce noise
- One ANR may be acceptable
- Patterns matter more than events

### Correct Thinking
Look for:
- Frequency
- Clustering
- Trend acceleration

---

## 5. Ignoring Resource Signals Until a Crash Occurs

### The Pitfall
Only investigating after a crash.

### Why This Is Wrong
Crashes are **late signals**.
Root causes often appear earlier:
- Memory growth
- CPU spikes
- Process duplication
- Rendering load

### Correct Thinking
Track resource metrics continuously and correlate them with failures.

---

## 6. Treating UI Issues as Cosmetic

### The Pitfall
Downplaying:
- Black screens
- Frozen UI
- UI mismatches after changes

### Why This Is Dangerous
UI issues often indicate:
- Rendering deadlocks
- Thread starvation
- Lifecycle mismanagement

These frequently precede ANRs or crashes.

### Correct Thinking
Treat UI anomalies as **early stability signals**, not cosmetic bugs.

---

## 7. Ignoring Boot Count and Reboot Patterns

### The Pitfall
Detecting reboots but not tracking frequency.

### Why This Misses Root Causes
A single reboot may be expected.
Repeated or unexpected reboots indicate:
- Watchdog triggers
- Kernel panics
- Critical system instability

### Correct Thinking
Track boot count as a metric and analyze changes over time.

---

## 8. Blind Retry Logic

### The Pitfall
Retrying failures without understanding why they occurred.

### Why This Is Risky
- Masks real instability
- Inflates PASS rates
- Hides degradation patterns

Retrying an ANR is different from retrying a UI glitch.
Retrying after a reboot may be unsafe.

### Correct Thinking
Retry based on:
- Failure type
- Severity
- Historical behavior

---

## 9. Mixing Data Collection, Decisions, and Reporting

### The Pitfall
One script that:
- Collects data
- Makes decisions
- Prints results

### Why This Does Not Scale
- Hard to test
- Hard to debug
- Hard to reuse

### Correct Thinking
Separate:
- Data collection
- Classification
- Decision logic
- Aggregation
- Reporting

This mirrors production systems.

---

## 10. Jumping to ML Too Early

### The Pitfall
Applying ML before:
- Structuring data
- Understanding failure signals
- Establishing baselines

### Why This Fails
ML amplifies data quality issues.
Bad signal modeling leads to confident but wrong predictions.

### Correct Thinking
Start with:
- Correct data types
- Explicit failure categories
- Aggregated metrics

Use ML only when rules and analysis are insufficient.

---

## 11. Interview Perspective

> “Most stability testing pitfalls come from treating complex system signals as
simple failures. In automotive center-stack testing, understanding failure
taxonomy, time-based behavior, and resource degradation is critical before any
advanced analysis.”
