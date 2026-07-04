import subprocess
import sys

def run(cmd):

    print(f"\nRunning: {cmd}\n")

    result = subprocess.call(
        cmd,
        shell=True
    )

    if result != 0:

        print(f"\nFailed: {cmd}")

        sys.exit(1)

print("================================")
print("AHNA INSTALLATION STARTED")
print("================================")

# Upgrade pip
run(
    f"{sys.executable} -m pip install --upgrade pip"
)

# Install requirements
run(
    f"{sys.executable} -m pip install -r backend/requirements.txt"
)

print("\n================================")
print("INSTALLATION COMPLETE")
print("================================")

print("""
NEXT STEPS:

1. Install Ollama
   https://ollama.com

2. Pull llama3 model:
   ollama run llama3

3. Start backend:
   cd backend
   uvicorn app:app --reload

4. Start frontend:
   cd frontend
   streamlit run streamlit_app.py
""")