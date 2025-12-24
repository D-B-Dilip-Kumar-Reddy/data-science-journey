# Environment and Tooling Decisions

## 1. Purpose of This Setup

The goal of this environment is to support:
- Reproducible data analysis
- Clean Python development
- Scalable transition from scripts to pipelines
- Long-term maintainability

This setup prioritizes **stability and clarity over convenience**.

---

## 2. Python Version Choice

Python 3.9+ is used because:
- Strong ecosystem support
- Compatibility with NumPy, Pandas, and ML libraries
- Stability across platforms

Using older versions limits library compatibility.

---

## 3. Environment Management Strategy

**Conda** is used for:
- Managing Python versions
- Handling native dependencies
- Creating isolated, reproducible environments

A `ds_env.yaml` file is committed to ensure anyone can recreate the environment reliably.

---

## 4. Tooling Overview

| Tool | Reason |
|----|------|
| VS Code | Lightweight, extensible |
| Jupyter | Exploration and validation |
| Git | Version control and history |
| GitHub | Collaboration and review |

Each tool is chosen for a specific purpose, not convenience.

---

## 5. Reproducibility Practices

- Environment defined via `ds_env.yaml`
- Dependencies explicitly listed
- No hidden global installs
- Environment validation scripts included

This reduces “works on my machine” issues.

---

## 6. Interview Perspective

> “I treat environment setup as part of the system design.  
Reproducibility is a feature, not an afterthought.”
