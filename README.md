# 📊 Quantitative Finance Simulations – Paul Wilmott

This repository contains implementations of **simulations and exercises** from *Introduction to Quantitative Finance* by **Paul Wilmott**.  
The goal is to practice and visualize key concepts from each chapter using Python.

---

## 📖 Project Overview

The project is organized by **chapters**, each containing Python modules, Jupyter notebooks, or Streamlit apps to illustrate concepts such as:

- Random walks (geometric & arithmetic)
- Monte Carlo simulations
- Option pricing
- Portfolio modeling
- Interest rate modeling
- Other fundamental quantitative finance techniques

The simulations are designed to be **interactive**, **educational**, and reproducible.

---

## 🗂 Project Structure

```bash
Introducao_Matematica_Financeira/
│
├── cap1_paul_wilmott/ # Chapter 1: Random Walks & Coin Toss simulations
│ ├── coin_toss/ # Module for random walk simulations
│ │ ├── app.py # Streamlit app for Random Walks
│ │ ├── coin_toss.py # Random walk logic (coin, geometric, arithmetic)
│ │ ├── requirements.txt # Python dependencies for this module
│ │ └── README.md # Documentation for chapter 1 module
│
├── cap2_paul_wilmott/ # Chapter 2: Monte Carlo & Option Pricing (future)
│ └── ...
│
├── cap3_paul_wilmott/ # Chapter 3: Portfolio simulations (future)
│ └── ...
│
├── LICENSE # MIT License
├── README.md # This project documentation
└── .gitignore # Ignore unnecessary files
```

> Each chapter folder can contain multiple modules, scripts, or apps relevant to that chapter.

---

## 🚀 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/pedromaltex/Introducao_Matematica_Financeira.git
cd Introducao_Matematica_Financeira

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# Linux/macOS
source venv/bin/activate
# Windows (Command Prompt)
venv\Scripts\activate

# Install dependencies for a chapter
cd cap1_paul_wilmott/coin_toss
pip install -r requirements.txt
```

## ▶️ Usage

For chapter 1 (Random Walks), run the Streamlit app:
```bash
streamlit run app.py
```

This will open an interactive web app where you can tweak parameters like initial value, probability of upward movement, number of steps, and number of simulations.

Other chapters will have their own scripts or notebooks to run.

## 📂 Background

This project is an educational resource for understanding quantitative finance principles:

- Random walks and stochastic processes

- Monte Carlo methods for pricing and risk

- Portfolio theory and simulation

- Interest rate models and derivatives

It’s meant as a hands-on companion to the book by Paul Wilmott.

## 🛠️ Future Plans

- Complete simulations for all chapters in the book

- Add more Streamlit apps for interactive exploration

- Include statistical analysis (mean, variance, histograms) for simulations

- Option to export results and charts as CSV or images

- Incorporate real financial data for comparison

## 📜 License

This project is licensed under the MIT License.