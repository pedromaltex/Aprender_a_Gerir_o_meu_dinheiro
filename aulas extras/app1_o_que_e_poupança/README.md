# 🎲 Random Walk Simulator

An interactive **Streamlit** app to simulate and visualize random walks.  
The user can choose between:

- **Geometric Random Walk** → multiplicative growth/decay (+1% or -1% each step)  
- **Arithmetic Random Walk** → additive growth/decay (+1 or -1 each step)  

The app lets you define:

- Initial value  
- Probability of an upward move  
- Number of steps  
- Number of simulations  

Results are displayed with interactive **Plotly** charts.

---

## 🚀 Demo

When running the app, you’ll see a control panel in the sidebar where you can tweak the parameters.  
Each simulation generates a trajectory of a random walk.

DEMO: https://coin-toss.streamlit.app/

---

## 📦 Installation

Clone this repository and install dependencies:

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

# Go to the app folder
cd cap1_paul_wilmott/coin_toss

# Install dependencies
pip install -r requirements.txt
```

## Requirements

Python 3.9+

Streamlit

NumPy

Plotly

## ▶️ Usage

Run the Streamlit app locally:

```bash
streamlit run app.py
```


This will open a browser window at http://localhost:8501
.

## 📂 Project Structure
```bash
coin_toss/
│
├── app.py                # Main Streamlit app
├── coin_toss.py          # Random walk logic (coin, geometric, arithmetic)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── screenshot.png        # Demo screenshot (optional)
```

## 📖 Background

Random walks are widely used to model:

- Stock prices and financial markets

- Particle motion in physics

- Population growth in biology

This app is a simple educational tool to experiment with such stochastic processes.

## 🛠️ Future Improvements

- Add histograms of final values (distribution view)

- Display statistics (mean, variance, min, max)
 
- Option to export results as CSV
 
- Add Monte Carlo comparison

## 📜 License

This project is licensed under the MIT License.
