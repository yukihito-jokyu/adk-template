import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

root_agent = Agent(
    model='gemini-2.0-flash',
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
