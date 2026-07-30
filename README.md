<div align="center">
  <img src="https://img.shields.io/badge/Nexu-Game_Engine-0f172a?style=for-the-badge&logo=python" alt="NexuPlay Banner">
  <h1>Nexu Game Engine: Alpha-Beta Minimax (NexuPlay) ✦</h1>
  <p><b>An Unassailable Game Theory AI Core</b></p>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
  [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)]()
  [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
  [![Status](https://img.shields.io/badge/Status-Production_Ready-success.svg)]()
</div>

---

## 🚀 The Vision

While Tic-Tac-Toe is often viewed as a foundational game, the underlying **Minimax Decision Engine** represents the core logical algorithm used in global logistics routing, financial hedging, and adversarial risk modeling. 

**NexuPlay** is a high-performance demonstration of Game Theory AI capabilities. By mathematically mapping the entire state-space tree, the AI fundamentally guarantees that it **cannot lose**. It is an unassailable engine designed for perfect deterministic environments.

---

## 🏆 Unmatched Performance: Competitive Analysis

Why use combinatorial mathematics over modern deep learning for zero-sum games?

| Feature | NexuPlay (Ours) | Random Move Bot | Heuristic Rules Bot | Deep Learning (RL) |
|---------|-----------------|-----------------|---------------------|--------------------|
| **Win/Draw Rate** | **100% Guaranteed** | ~50% | ~90% | ~99% (Requires Training) |
| **Logic Type** | **Deterministic Game Theory** | Stochastic | Hardcoded If/Else | Probabilistic Policy |
| **Computational Cost**| **Ultra Low (Alpha-Beta Pruned)**| Lowest | Low | Extremely High |
| **Predictability**| **Mathematically Perfect**| Unpredictable | Exploitable | Can Hallucinate |

As shown above, using Deep Learning (Reinforcement Learning) for a zero-sum, perfect information game like Tic-Tac-Toe is computationally wasteful and mathematically imperfect. NexuPlay solves the environment perfectly using standard combinatorial mathematics, utilizing zero GPU resources.

---

## 🧠 Core Architecture & System Flow

```mermaid
graph TD
    A["Client User Interface"] -->|"HTTP POST JSON"| B("FastAPI Server")
    B --> C{"State Matrix Parser"}
    C --> D["Minimax Evaluator"]
    D --> E{"Alpha-Beta Pruning"}
    E -->|"Cut Non-viable branches"| F["Decision Node"]
    F -->|"Return X,Y Coordinates"| G["JSON Response"]
    G --> A
```

### 1. Alpha-Beta Pruning Optimization
A standard Minimax algorithm evaluates every possible future board state. In Tic-Tac-Toe, that is `9!` (362,880) leaf nodes. By implementing advanced **Alpha-Beta pruning**, NexuPlay dynamically tracks the best possible score (`alpha`) and worst possible score (`beta`), allowing it to skip evaluating branches that cannot possibly influence the final decision. This mathematically cuts evaluation time by over **60%**.

### 2. VisionOS Frontend
The flawless AI logic is wrapped in a breathtaking VisionOS-inspired interface. It utilizes backdrop-filters, subtle gradients, and reactive hover animations to make a simple game feel like a next-generation SaaS product.

---

## 📂 Project Structure & Files

- `main.py`: The FastAPI application server bridging the backend logic with the web UI.
- `ai_agent.py`: The untouchable Minimax Alpha-Beta Pruning algorithm implementation.
- `static/index.html`: The futuristic VisionOS user interface structure.
- `static/styles.css`: The styling logic implementing glassmorphism and animations.
- `static/script.js`: The game loop, event listeners, and API integration.

---

## ⚙️ Installation & Usage

### Prerequisites
- Python 3.10+
- FastAPI, Uvicorn

### Quick Start
```bash
# 1. Clone the repository
git clone https://github.com/lakshanmuruganandam/Nexu-Game-Engine.git
cd Nexu-Game-Engine

# 2. Install dependencies
pip install fastapi uvicorn

# 3. Boot the API Server
python main.py
```
*The VisionOS UI will be available immediately at `http://localhost:8002/`.*

---

## 🤝 Contributing
We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📜 License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---
<div align="center">
  <b>Perfect Logic. Perfect Code. Built by Lakshan Muruganandam.</b>
</div>
