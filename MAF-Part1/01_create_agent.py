"""
 01: Create Azure AI Foundry Agent by using Microsoft Agent Framework (MAF) SDK
"""
print("hi agents")

import asyncio
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv('.env01')
PROJECT_ENDPOINT = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
MODEL_DEPLOYMENT = os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME")
AUTH_MODE = os.getenv("AZURE_AI_AUTH_MODE")
API_KEY = os.getenv("AZURE_AI_API_KEY")
print(f"Project Endpoint: {PROJECT_ENDPOINT}")
print(f"Model Deployment: {MODEL_DEPLOYMENT}")
print(f"Authentication Mode: {AUTH_MODE}")
print(f"API Key: {API_KEY}")

if AUTH_MODE.lower() == "cli":
    chat_client = AzureOpenAIChatClient(
        endpoint=PROJECT_ENDPOINT,
        deployment_name=MODEL_DEPLOYMENT,
        credential=AzureCliCredential()
    )
else:
    chat_client = AzureOpenAIChatClient(
        endpoint=PROJECT_ENDPOINT,
        deployment_name=MODEL_DEPLOYMENT,
        api_key=API_KEY
    )