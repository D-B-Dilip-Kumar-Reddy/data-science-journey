# Common Testing Pitfalls  
(Applied to Automotive Center-Stack Stability Testing)

## 1. Treating Stability Failures as Isolated Events

### The Pitfall
Analyzing each failure independently without considering historical context.

### Why This Is Wrong
Center-stack stability issues often:
- Build up slowly
- Appear intermittently
- Manifest only after long uptime

A single failure rarely represents the real problem.

### Correct Data-Thinking Approach
- Analyze failures across iterations
- Look for frequency, clustering, and trends
- Correlate failures with uptime and workload

---

## 2. Treating FAIL and CRASH as the Same Outcome

### The Pitfall
Grouping all non-PASS results into a single category.

### Why This Is Dangerous
- FAIL often indicates functional or timing issues
- CRASH indicates system instability or resource exhaustion

Mixing them hides severity and misguides analysis.

### Correct Approach
- Model FAIL and CRASH as separate categories
- Track crash rate independently
- Escalate crashes differently in reports and automation

---

## 3. Ignoring Time and Execution Order

### The Pitfall
Analyzing test results without considering:
- Execution order
- Elapsed time
- System uptime

### Why This Is Wrong
Many center-stack issues are **time-dependent**:
- UI lag after hours
- Memory leaks
- Service degradation

Ignoring time removes the most important signal.

### Correct Approach
- Treat executions as time-series data
- Track metrics against uptime
- Analyze degradation patterns

---

## 4. Overreacting to Single Failures

### The Pitfall
Stopping tests or escalating immediately after one failure.

### Why This Is Inefficient
- Long-run systems naturally produce noise
- One failure does not indicate instability
- Early termination loses valuable data

### Correct Approach
- Define thresholds (e.g., failure rate over time)
- Look for repeated patterns
- Continue execution unless severity demands otherwise

---

## 5. Using Incorrect Data Types

### The Pitfall
- Storing execution time as strings
- Comparing floats using equality
- Using lists where dictionaries are required

### Why This Breaks Analysis
Incorrect data types lead to:
- Broken aggregations
- Invalid comparisons
- Incorrect trends

### Correct Approach
- Use floats for timings
- Use integers for counts
- Use categorical values for statuses
- Choose data types deliberately

---

## 6. Mixing Data Collection, Logic, and Reporting

### The Pitfall
Writing scripts that:
- Collect data
- Make decisions
- Generate reports  
all in one place.

### Why This Doesn’t Scale
- Hard to debug
- Hard to test
- Hard to reuse

### Correct Approach
Separate:
- Data collection
- Decision logic
- Reporting and visualization

This mirrors real production systems.

---

## 7. Blind Retry Logic

### The Pitfall
Retrying failures without understanding why they occurred.

### Why This Is Risky
- Masks real stability issues
- Inflates PASS rates artificially
- Produces misleading reports

### Correct Approach
- Retry based on failure type
- Limit retry counts
- Log retries separately
- Treat repeated retries as signals

---

## 8. Ignoring Resource Metrics

### The Pitfall
Focusing only on PASS / FAIL and ignoring:
- Memory usage
- CPU load
- UI responsiveness

### Why This Misses Root Causes
Many center-stack issues are **resource-driven**, not functional.

### Correct Approach
Correlate failures with:
- Memory growth
- CPU spikes
- UI latency increases

---

## 9. Jumping to Machine Learning Too Early

### The Pitfall
Attempting ML without:
- Clean data
- Stable metrics
- Clear problem definition

### Why This Fails
ML amplifies data quality issues.
Bad data leads to bad models.

### Correct Approach
- Start with aggregation and rules
- Introduce ML only when rules fail
- Use ML for prediction, not basic analysis

---

## 10. Interview Perspective

> “Most stability testing failures are not single events but patterns over time.  
The biggest pitfalls come from ignoring trends, time, and data quality rather than from missing tools or models.”
