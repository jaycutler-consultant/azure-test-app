from fastapi import FastAPI
import requests

app = FastAPI()

# Replace this with your actual Power Automate flow URL
POWER_AUTOMATE_URL = "https://defaultb802f42a4ac341f686f619634e46c6.83.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/48bccdbdcb274277a7553698948a4c8b/triggers/manual/paths/invoke/?api-version=1"

@app.get("/")
def read_root():
    payload = {
        "message": "Hello from Azure App!",
        "recipientEmail": "jay@staffingengine.onmicrosoft.com"
    }

    try:
        response = requests.post(POWER_AUTOMATE_URL, json=payload, timeout=5)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to notify Power Automate: {e}")

    return {"message": "Hello, Azure!"}
