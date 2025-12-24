![Phase](https://img.shields.io/badge/Phase-0%20Complete-brightgreen)

# 📊 Data Science Journey  
**From Stability Testing to Data Science & Machine Learning**

## Overview

This repository documents my **structured transition from stability testing / test engineering** into **Data Science and Machine Learning**, with a strong emphasis on:

- Core Python fundamentals
- Data thinking and decision logic
- Clean, maintainable, professional code
- Real-world problem mapping from testing to data science

This is **not a tutorial dump**.  
It is a **learning + portfolio repository**, designed to reflect **how I think and build systems**, not just what I study.

---

## 🎯 Goals of This Repository

- Build **strong Python foundations** suitable for data pipelines
- Translate **testing problems** into **data problems**
- Apply concepts incrementally through **practice and mini-projects**
- Follow **professional project structure and Git discipline**
- Create artifacts that a **senior engineer can review and understand quickly**

---

## 🧠 Learning Philosophy

### 1️⃣ Concepts before tools  
I prioritize understanding **why something is needed** before using libraries or frameworks.

### 2️⃣ Notes and practice are separated  
- **Notes (`notes/`)** explain reasoning, mental models, and decisions  
- **Practice code (`practice/`)** is executable, modular, and testable

### 3️⃣ Real-world domain mapping  
All examples are grounded in **stability testing scenarios**:
- Test executions
- PASS / FAIL / CRASH states
- Retries and thresholds
- Metrics and trends over time  

(No toy or unrelated examples.)

---

## About This Repository

This repository reflects my structured learning journey as I transition from
automotive center-stack stability testing into Data Science and Machine Learning.

I used a combination of hands-on experience, structured learning, and modern
learning tools (including AI-assisted guidance) to organize concepts, validate
my understanding, and build clean, testable code.

All examples, decisions, and explanations are grounded in my real-world
experience with long-run automotive infotainment stability testing.
The goal of this repository is not originality of wording, but clarity of
thinking, correctness of concepts, and professional engineering practices.

---

## How Data Science, Machine Learning, and AI Relate

    Artificial Intelligence (AI)
    ┌─────────────────────────┐
    │     Machine Learning    │
    │     ┌─────────────┐     │
    │     │  Data       │     │
    │     │  Science    │     │
    │     └─────────────┘     │
    └─────────────────────────┘


**Key takeaways**
- Machine Learning sits at the intersection of **AI and Data Science**
- Most real-world problems start as **Data Science problems**
- ML and AI are introduced only when necessary

---

## 🗂️ Repository Structure

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


---

## 📘 Learning Phases

### 🟢 Phase 0 — Foundations
- Data Science vs ML vs AI
- Data Analytics vs Data Science
- Data thinking for testers
- Environment and tooling decisions

### 🟡 Phase 1 — Python for Data Science
- Variables and data types
- Conditionals and decision logic
- Loops and execution flow
- Collections and functions
- Unit-tested, modular code

### 🔵 Phase 2 — Data Analysis (Upcoming)
- NumPy
- Pandas
- Data cleaning
- Exploratory Data Analysis

### 🔴 Phase 3 — Machine Learning (Upcoming)
- Feature engineering
- Classical ML models
- Evaluation and validation
- Practical ML pipelines

---

## 🧪 Mini Projects

### Stability Testing Analysis

A realistic mini project using **synthetic stability execution data** to demonstrate:
- Parsing execution data
- Classifying failures and crashes
- Computing stability metrics
- Identifying flaky behavior
- Visualizing trends across iterations

---

## 🛠️ How to Run

```bash
conda env create -f ds_env.yaml
conda activate ds-env
```
---

## Testing

Basic unit tests are included to validate core logic:
```bash
pytest tests/
```
---
