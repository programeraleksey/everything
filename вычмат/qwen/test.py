import requests
import json

payload = {
    "model": "qwen3.5:latest",
    "prompt": "Answer: 2+2?",
    "think": True,
    "stream": True,
}


r = requests.post("http://localhost:11434/api/generate", json=payload, stream=True, timeout=600)

if r.status_code != 200:
    print("STATUS:", r.status_code)
    print("BODY:", r.text)
    raise SystemExit

for line in r.iter_lines():
    if not line:
        continue
    chunk = json.loads(line)
    print(chunk.get("thinking", "") + chunk.get("response", ""), end="")
    if chunk.get("done"):
        break
#
# from google import genai
#
# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()
#
# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
# )
# print(response.text)
