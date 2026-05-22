You must place a ".env" file at location C:\Users\PCHAUH21\work\workspace_python\parent-python\agentic-ai-sdlc-hitl-langgraph
with content GROQ_API_KEY=<<actual key>>
--------------------------------------------------------------------
MAC
--------------------------------------------------------------------
cd
python3.12 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

streamlit run streamlit_app.py

--------------------------------------------------------------------
WINDOWS
--------------------------------------------------------------------
cd C:\Users\PCHAUH21\work\workspace_python\parent-python\agentic-ai-sdlc-hitl-langgraph

py -3.12 -m venv venv
python -m pip install --upgrade pip
pip install --index-url https://pypi.org/simple/ groq==0.18.0
pip install --index-url https://pypi.org/simple/ groq==0.18.0
pip install --extra-index-url https://pypi.org/simple/ -r requirements.txt

$env:PYTHONUTF8 = "1"
streamlit run streamlit_app.py

Requirement:
upgrade services: order-offers, order-pricing, order-taxes to spring boot 4