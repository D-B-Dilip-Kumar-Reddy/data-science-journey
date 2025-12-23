![Phase](https://img.shields.io/badge/Phase-0%20Complete-brightgreen)

# Data Science Journey

From Stability Testing to Data Science & ML

## Overview

This repository documents my **structured transition from stability testing / test engineering** into **Data Science and Machine Learning**, with a strong emphasis on:
 - Core Python fundamentals
 - Data thinking and decision logic
 - Clean, maintainable, professional code
 - Real-world problem mapping from testing to data science

This is not a tutorial dump.
It is a learning + portfolio repository.

---

## Goals of This Repository

- Build strong Python foundations suitable for data pipelines
- Translate testing problems into data problems
- Apply concepts incrementally through practice and mini-projects
- Follow professional project structure and Git discipline
- Create artifacts that a senior engineer can review and understand quickly

---

## Learning Philosophy

### 1️⃣ Concepts before tools

I prioritize understanding why something is needed before using libraries or frameworks.

### 2️⃣ Notes and practice are separated

Notes (notes/) explain reasoning, mental models, and decisions

Practice code (practice/) is executable, modular, and structured

### 3️⃣ Real-world domain mapping
All examples are grounded in stability testing scenarios:
- Test executions
- PASS / FAIL / CRASH states
- Retries and thresholds
- Metrics and trends over time

(No toy or unrelated examples.)

---

## Repository Structure

data-science-journey/

│

├── README.md

│

├── notes/

│   ├── phase_0_setup/

│   │   └── environment_and_tooling.md

│   │

│   ├── phase_1_python/

│   │   ├── day_01_variables_data_types.md

│   │   ├── day_02_conditionals.md

│   │   ├── day_03_loops.md

│   │   └── common_mistakes.md

│

├── practice/

│   ├── phase_0_setup/

│   │   └── env_validation.py

│   │

│   ├── phase_1_python/

│   │   ├── day_01_data_types/

│   │   ├── day_02_conditionals/

│   │   └── day_03_loops/

│

├── mini_projects/

│   └── stability_testing_analysis/

│       ├── README.md

│       ├── data/

│       ├── src/

│       └── notebooks/

│

├── tests/

│

├── utils/

│

├── requirements.txt

├── ds_env.yaml

└── .gitignore


---

## Learning Phases

### 🟢 Phase 0 — Foundations & Setup

Focus:

- Environment setup
- Git & GitHub workflow
- Data Science vs ML vs Analytics
- Data thinking for testers

📂 Location
- notes/phase_0_setup/
- practice/phase_0_setup/

### 🟡 Phase 1 — Python for Data Science

Focus:

- Variables and data types
- Conditionals and decision logic
- Loops and execution flow
- Collections (lists, dicts, sets)
- Functions and modular code

Each day includes:

- Concept notes
- Practice scripts
- Edge case handling
- Testing-aligned examples

📂 Location
- notes/phase_1_python/
- practice/phase_1_python/

### 🔵 Phase 2 — Data Analysis (Upcoming)

Focus:

- NumPy
- Pandas
- Data cleaning
- Aggregations
- Exploratory Data Analysis (EDA)

### 🔴 Phase 3 — Machine Learning (Upcoming)

Focus:

- Feature engineering
- Classical ML algorithms
- Model evaluation
- Practical ML pipelines

---

### Mini Projects

**Stability Testing Analysis**

A realistic mini project built using synthetic test execution data to demonstrate:

- Parsing execution data and logs
- Classifying failures and crashes
- Computing stability metrics
- Identifying flaky behavior
- Visualizing trends across iterations

📂 Location

- mini_projects/stability_testing_analysis/

This project exists to show end-to-end application, not isolated scripts.

---

## How to Run the Code

Conda environment
```
conda env create -f ds_env.yaml
conda activate ds-env
```

Run a practice script
```
python practice/phase_1_python/day_02_conditionals/status_classifier.py
```

---

## Testing

Basic unit tests are included to validate core logic:

pytest tests/

---
