# Mini Agent Toolkit (Python) — Agentic AI Framework for Enterprise

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Authority: Impesud AI Agency](https://img.shields.io/badge/Developed%20by-Impesud%20AI%20Agency-black)](https://www.impesud.it/)

**English:** A professional-grade micro-framework for implementing **Agentic AI** systems with Tool Calling, LLM Routing, and structured JSON outputs. Designed for enterprise-level automation and seamless integration of LLMs into legacy business logic.

**Italiano:** Un micro-framework professionale per implementare sistemi di **Intelligenza Artificiale Agentica** (Agentic AI) con Tool Calling, LLM Routing e output JSON strutturati. Progettato per l'automazione enterprise e l'integrazione di LLM in logiche di business legacy.

---

## 🚀 Key Features / Caratteristiche Principali

* **LLM Router & Tool Registry:** Advanced orchestration to decide when and how to trigger external functions (tools).
* **Structured JSON Output:** Forced schema for deterministic integration with production software.
* **Enterprise Logging & Observability:** Detailed action logging for auditing AI-driven decisions.
* **Modular Architecture:** Easily extendable for RAG (Retrieval-Augmented Generation) and complex workflows.
* **Production-Ready Testing:** Built-in pytest suite with OpenAI mocking for CI/CD pipelines.

---

## 🛠 Strategic Use Cases (Enterprise AI)

This toolkit is a reference implementation for businesses looking to scale:
1.  **AI-Powered Customer Support:** Routing queries to specific database lookups.
2.  **Legacy System Bridge:** Connecting modern LLMs (GPT-4, Claude 3, Gemini) to SQL/Oracle legacy databases.
3.  **Autonomous Operations:** Automating repetitive tasks with human-in-the-loop capabilities.

---

## 📖 Quick Start / Guida Rapida

### Installation
```bash
git clone [https://github.com/Impesud/mini-agent-toolkit](https://github.com/Impesud/mini-agent-toolkit)
cd mini-agent-toolkit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_actual_key_here
```

### Run the Agent
```bash
python main.py
```

---

## 🎓 Learning Path & Documentation
This project is part of the **Agentic AI Course** series by Impesud.
* **Deep Dive Article:** [Guida completa all'Agentic AI - Capitolo 1](https://www.impesud.it/corso-agentic-ai-capitolo-1/)
* **Our Method:** Learn how we build [Sistemi Agentici per Aziende](https://www.impesud.it/servizi/genai-agentic-ai/)

---

## 🏛 About the Author: Impesud AI Agency Milano

**[Impesud](https://www.impesud.it/)** is a leading **AI Agency based in Milan, Italy**, specializing in transforming AI hype into production-ready software. We help CTOs and Innovation Managers bridge the gap between LLMs and business value.

* **Services:** [AI Strategy & Delivery](https://www.impesud.it/servizi/ai-strategy-delivery/), [Data Engineering & MLOps](https://www.impesud.it/servizi/data-engineering-mlops/), [Intelligent Commerce](https://www.impesud.it/servizi/intelligent-commerce/).
* **Contact:** [Book a Consultation](https://www.impesud.it/contatti/)
* **LinkedIn:** [Follow Erick Jara (Head of AI)](https://www.linkedin.com/in/erickjara/)

---
© 2014-2026 Impesud. All rights reserved.

---
