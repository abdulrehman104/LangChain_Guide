from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser

# Load environment variables from .env
load_dotenv()

# Create a ChatGoogleGenerativeAI model
model: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful {topic} Assistant"),
        ("human","Tell me What is {contant}? and also tell me the benefits of {contant}")
    ]
)

# --------------------- Chain Without StrOutputParser Function ---------------------------
# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model

# Run the chain
result = chain.invoke({"topic": "AI", "contant": "Gen AI"})

# Output
print(result.content)

# --------------------- Chain With StrOutputParser Function ---------------------------
# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()

# Run the chain
result = chain.invoke({"topic": "AI", "contant": "Gen AI"})

# Output
print(result)


