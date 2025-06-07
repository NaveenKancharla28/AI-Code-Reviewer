# code_review.py

import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Explicitly fetch the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# ✅ DEBUG: Show what key was loaded (clip this after testing)
print("DEBUG >> Loaded API KEY:", openai_api_key)

# ✅ Error if not found
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

# ✅ Load prompt template
def load_prompt():
    with open("prompts/review_prompt.txt", "r") as f:
        return f.read()
def analyze_code(user_code: str) -> str:
    prompt_template = PromptTemplate(
        input_variables=["code_block"],
        template=load_prompt()
    )

    llm = ChatOpenAI(
        temperature=0.2,
        model_name="gpt-4",
        openai_api_key=openai_api_key
    )

    # 🔧 Define the chain properly
    chain = LLMChain(llm=llm, prompt=prompt_template)

    # Optional: Debug print
    filled_prompt = prompt_template.format(code_block=user_code)
    print("\n\n🔧 PROMPT BEING SENT TO GPT:\n")
    print(filled_prompt)

    # ✅ Now run it
    response = chain.run(code_block=user_code)

    return response
