import requests
import json

# Test the MCP server to see if DSP is loaded
response = requests.get("http://127.0.0.1:8787/status")
print("UI Status:", response.json())

response = requests.get("http://127.0.0.1:8787/params")
print("\nParameters:", json.dumps(response.json(), indent=2))

response = requests.get("http://127.0.0.1:8787/param-values")
print("\nParameter Values:", json.dumps(response.json(), indent=2))
