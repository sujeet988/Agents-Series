"""
 01: Create Azure AI Foundry Agent by using Microsoft Agent Framework (MAF) SDK
"""
print("hi agents")

import asyncio
import os
from dotenv import load_dotenv
from azure.ai.projects.aio import AIProjectClient
from azure.identity.aio import AzureCliCredential
from azure.core.credentials import AzureKeyCredential



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

async def get_project_client():
    if AUTH_MODE.lower() == "cli":
        credential = AzureCliCredential()
    else:
        credential = AzureKeyCredential(API_KEY)

    return AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=credential)



async def main():

    print("\nCreating Azure AI Foundry Agent...\n")

    project_client = await get_project_client()

    async with project_client:

        agent = await project_client.agents.create_agent(
            model=MODEL_DEPLOYMENT,
            name="DemoAssistant",
            instructions="You are a helpful AI assistant. Be concise and friendly."
        )

        print("Agent Created Successfully")
        print(f"Agent ID: {agent.id}")
        print(f"Agent Name: {agent.name}")

        # Optional: List Agents
        print("\nExisting Agents:")
        async for existing_agent in project_client.agents.list_agents():
            print(f" - {existing_agent.name} ({existing_agent.id})")

        # Optional cleanup
        # await project_client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())