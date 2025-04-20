from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from google import genai

load_dotenv()

def get(
    model_name: str = "gemini-2.0-flash",
    temperature: int = 0,
):
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    return llm

if __name__ == '__main__':
    client = genai.Client()

    print("List of models that support generateContent:\n")
    for m in client.models.list():
        for action in m.supported_actions:
            if action == "generateContent":
                print(m.name)

    print("List of models that support embedContent:\n")
    for m in client.models.list():
        for action in m.supported_actions:
            if action == "embedContent":
                print(m.name)
