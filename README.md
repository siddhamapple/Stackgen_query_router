# 🧠 StackGen Query Router

> **A clean, extensible, agent-based query routing system that mimics how modern AI platforms dispatch user requests to the correct tools or agents.**

---

##  Overview

**StackGen Query Router** is a lightweight, CLI-based system designed to demonstrate the core logic of AI agent orchestration. It illustrates how user queries can be:

* **Understood** via intent classification.
* **Routed** to the correct domain agent.
* **Handled** by modular, isolated components.
* **Failed gracefully** when no suitable agent exists.

The project is intentionally simple yet architecturally sound, reflecting how AI-adjacent routing systems are designed in real production environments.

##  What Problem Does This Solve?
This project simulates that **decision layer**—the logic that determines *who* should answer the user before any API call is made.

---

## 🏗️ System Architecture

The system follows a linear routing flow:

```mermaid

graph TD
    A[User Query] --> B[Intent Classifier]
    B -->|Intent Label| C[Query Router]
    C -->|Select Agent| D[GitHubAgent]
    C -->|Select Agent| E[LinearAgent]
    C -->|No Match| F[Graceful Failure]
    D --> G[Mocked Response]
    E --> G
    F --> G[\"I cannot answer this question\"]

```

