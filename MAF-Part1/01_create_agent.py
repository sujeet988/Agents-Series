"""
 01: Create Azure AI Foundry Agent
"""
print("hi agents")

import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env01')
PROJECT_ENDPOINT = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
MODEL_DEPLOYMENT = os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME")
print(f"Project Endpoint: {PROJECT_ENDPOINT}")
print(f"Model Deployment: {MODEL_DEPLOYMENT}")
