import google.generativeai as genai

def generate(img):
    API_KEY = "YOUR_API_KEY"
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(["explain in detail to me about this image", img], stream=True, generation_config= genai.types.GenerationConfig(temperature=0.8))
    response.resolve()
    return response.text