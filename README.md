# Home Appliance Fault Expert System — Streamlit

A rule-based AI expert system for diagnosing common home-appliance faults.

## What was changed

The original project used Flask + HTML + JavaScript API endpoints. For Streamlit deployment, it has been converted to a single Streamlit application:

- `app.py` → Streamlit user interface and inference logic
- `rules.py` → existing appliance/fault knowledge base
- `requirements.txt` → Streamlit dependency
- Flask routes and JavaScript API calls are no longer required
- Bundled `venv`, `__pycache__`, and `.pyc` files are excluded

## Local run

Open Command Prompt/PowerShell in this folder:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL shown by Streamlit, normally:

`http://localhost:8501`

## Streamlit Community Cloud deployment

1. Push this folder to a GitHub repository.
2. Go to Streamlit Community Cloud.
3. Choose **Create app**.
4. Select your GitHub repository and branch (`main`).
5. Set the main file to:
   `app.py`
6. Click **Deploy**.

No Flask server, port 5000, API URL, database, or environment variable is required for this rule-based version.

## Important

The faults shown in the Fault dropdown are generated directly from `APPLIANCE_FAULTS` in `rules.py`. Therefore, changing the appliance automatically changes the available faults.

Flow:

**User Input → Appliance → Related Fault → IF–THEN Rule → Possible Fault → Troubleshooting**
