# 📊 GHI Dashboard (Streamlit)

Interactive Streamlit app to explore Global Hunger Index (GHI) or any numeric metric by country/region.

## Features
- Country/region filters with multiselect widgets
- Boxplot / Violin / Histogram / Bar (mean) charts (Plotly)
- Top regions table (mean/median/std)
- CSV download of the filtered slice
- Reads local CSVs from ./data (this folder is ignored by git)

## Quickstart
`bash
# 1) Clone your repo and create a branch
git checkout -b dashboard-dev

# 2) Create & activate a virtual environment (example: venv)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3) Install deps
pip install -r requirements.txt

# 4) Put your dataset CSV into ./data
#    Required columns: country, region; optional numeric columns (e.g., GHI)

# 5) Run the app
streamlit run app/main.py
