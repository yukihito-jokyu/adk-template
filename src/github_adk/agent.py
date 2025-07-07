import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    # model='gemini-2.0-flash',
    # model=LiteLlm(model="openai/mistral-small3.1"),
    model=LiteLlm(model="azure/gpt-4o-mini"),
    name='GitHubのアシスタントエージェント',
    instruction='GitHubのアシスタントエージェントです。',
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command='docker',
                args=[
                    "run",
                    "-i",
                    "--rm",
                    "-e",
                    "GITHUB_PERSONAL_ACCESS_TOKEN",
                    "ghcr.io/github/github-mcp-server",
                ],
                env={
                    "GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_TOKEN", ""),
                }
            ),
        )
    ],
)
