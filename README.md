# 💸 Aprender a Gerir o Meu Dinheiro — Simulações Interativas

**Aprender finanças pessoais nunca foi tão visual e interativo!**  
Esta aplicação, desenvolvida em **Streamlit**, permite aos utilizadores explorar de forma simples e envolvente os principais conceitos de **poupança, investimento e planeamento financeiro**.

> 🎯 Ideal para estudantes e curiosos que querem compreender **como o dinheiro cresce, se desvaloriza e se transforma em liberdade financeira.**

---

## 🚀 Funcionalidades Principais

- 📘 **Módulos educativos** sobre finanças pessoais, divididos por capítulos temáticos.
- 🧮 **Simulações interativas**: experimenta estratégias e vê o impacto em gráficos dinâmicos.
- 📈 **Visualizações com Plotly**, para explorar o crescimento do dinheiro ao longo do tempo.
- 💭 **Reflexões guiadas**, para consolidar o que aprendeste.
- 🗺️ **Navegação modular automática** — novos capítulos e simulações são detetados sem editar o `main.py`.

---

## 🧠 Estrutura do Projeto

A aplicação é totalmente **modular**, o que facilita a expansão com novos capítulos ou simulações.

```
📂 aprender_dinheiro/
│
├── main.py                         # Interface principal e sistema de navegação
│
├── cap1_poupanca/                  # Capítulo 1: Poupança e Juros Compostos
│   ├── chapter_info.py             # Metadados do capítulo
│   ├── simulador_poupanca/         # Simulação 1
│   │   └── app.py                  # Código Streamlit da simulação
│   └── poupar_investir/            # Simulação 2
│       └── app.py
│
├── cap2_investimentos/             # Capítulo 2 (exemplo futuro)
│   ├── chapter_info.py
│   └── simulacao_bolsa/
│       └── app.py
│
└── requirements.txt
```

Cada capítulo contém:
- `chapter_info.py` → contém o dicionário `CHAPTER_INFO` com o título e descrição.
- Subpastas → cada uma representa uma simulação independente (`app.py`).

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/teu-utilizador/aprender-dinheiro.git
cd aprender-dinheiro
```

### 2️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Executar a aplicação
```bash
streamlit run main.py
```

---

## 🧩 Requisitos Principais

- Python 3.9 ou superior  
- Bibliotecas:
  - `streamlit`
  - `plotly`
  - `pandas`
  - `numpy`

---

## 👨‍🏫 Autor

**Pedro Maltez**  
Professor de Matemática • Escola Básica 2/3 do Bairro Padre Cruz  
📘 Projeto pedagógico: *Aprender a Gerir o Meu Dinheiro (2025/2026)*

---

> Desenvolvido com 💙 para promover a literacia financeira nas escolas portuguesas.
