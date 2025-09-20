# Test Framework (Python + pytest)

## Run locally
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q

## Run with html report
pytest --html=reports/report.html --self-contained-html
