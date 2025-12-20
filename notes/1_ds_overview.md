# Data Science Overview

## 1. What is Data Science?
Data Science is the discipline of converting raw data into meaningful insights by applying data analysis, statistics, visualization, and programming.  
Its primary purpose is to understand what is happening in the data, why it is happening, and how this understanding can support better decisions in systems, products, or processes.

Data Science may use Machine Learning, but it does not depend on it.

---

## 2. Data Science vs Machine Learning vs Artificial Intelligence

### Artificial Intelligence (AI)
Artificial Intelligence is the broad goal of making machines behave intelligently.  
It focuses on decision-making, reasoning, and automated actions.  
AI systems may be rule-based or learning-based.

### Machine Learning (ML)
Machine Learning is a subset of AI that focuses on learning patterns from historical data.  
ML models are used to make predictions, classifications, or recommendations without being explicitly programmed for every scenario.

### Data Science (DS)
Data Science is the practical process of analyzing data to extract insights.  
It uses statistics, visualization, domain knowledge, and sometimes ML to explain patterns and trends in data.

### Relationship
AI is the overall goal.  
ML is one way to achieve AI.  
Data Science is the practice that uses ML as a tool when prediction or automation is required.

---

## 3. Data Science Workflow
1. Data collection  
2. Data cleaning and preprocessing  
3. Exploratory Data Analysis (EDA)  
4. Modeling (optional – includes ML)  
5. Insight generation and decision support  

Not every Data Science problem requires Machine Learning.

---

## 4. Key Characteristics of Data Science
- Strong focus on understanding data
- Emphasis on explaining patterns and trends
- Heavy use of statistics and visualization
- Machine Learning used only when necessary
- Output is usually insights, reports, or recommendations

---

## 5. Mapping Data Science to Testing and Automation

| Testing Concept | Data Science Equivalent |
|----------------|------------------------|
| Test logs | Dataset |
| Test iteration | Data point |
| Failure / crash | Label or outcome |
| Execution time | Numeric feature |
| Pass / Fail | Binary classification |
| Flaky tests | Anomalies |
| Long-run trends | Time-series analysis |
| Failure similarity | Clustering |

---

## 6. Relevance to My Work
My testing work involves executing long-duration tests, collecting logs, failures, crashes, and performance metrics across iterations and systems.  
This data naturally fits into Data Science workflows.

By applying Data Science:
- Failure patterns can be identified
- Trends across iterations can be visualized
- Root causes can be correlated with system conditions
- Future failures can eventually be predicted using ML

This makes Data Science a natural extension of test automation and analysis.

---

## 7. Simple Mental Model
- Data Science explains what is happening and why  
- Machine Learning predicts what will happen next  
- Artificial Intelligence takes actions based on predictions
