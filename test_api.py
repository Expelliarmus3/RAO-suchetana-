import google.generativeai as genai

# Use your actual API Key here
genai.configure(api_key="AIzaSyC3nCzYWD-UIk312cLVxVIQN3xAuraQs1E")

print("Checking available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print("Error:", e)