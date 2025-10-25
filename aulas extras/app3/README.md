# Future Value of $1 Simulation

Welcome to the **Future Value of $1 Simulation**, a simple and interactive **Streamlit** app to visualize how money loses value over time under continuous compounding depreciation (inflation or negative interest).

---

## ✨ Features

* Input your **initial value** (default: $1)
* Set **annual interest rate** (default: 3%)
* Select **number of years** (1–100)
* Visualize results as a **line chart** and **bar chart**
* See the **final value** after the selected period

---

## ⚡ Installation

1. Clone this repository:

```bash
git clone https://github.com/pedromaltex/Introducao_Matematica_Financeira.git
cd cap1_paul_wilmott/present_value
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> Make sure `requirements.txt` includes `streamlit`, `numpy`, and `plotly`.

---

## 🚀 Usage

Run the app:

```bash
streamlit run app.py
```

1. Open the **sidebar** to set simulation parameters.
2. Click **Calculate**.
3. Explore how the value of money changes over time.

---

## 🔍 Example

* Initial Value: $1
* Annual Interest Rate: 3%
* Number of Years: 20

The app will display how $1 depreciates year by year, showing both charts and the final value.

---

## 💻 Code Snippet

```python
import numpy as np

def decreasing_continuously_compounded(P, r, t):
    return P * np.exp(-r * t)
```

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Pedro Maltez** – [GitHub Profile](https://github.com/pedromaltex)
