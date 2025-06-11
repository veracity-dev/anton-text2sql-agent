from typing import List
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_core.tools import BaseTool
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import ToolMessage

from .database import DatabaseManager

class SQLAgent:
    def __init__(self, config):
        self.db_manager = DatabaseManager()
        self.llm = config.get_llm()
        self.toolkit = self._create_toolkit()
        self.tools = self.toolkit.get_tools()
        
    def _create_toolkit(self) -> SQLDatabaseToolkit:
        """Create SQLDatabaseToolkit with database and LLM."""
        return SQLDatabaseToolkit(
            db=self.db_manager.db,
            llm=self.llm
        )
    
    def create_tool_node_with_fallback(self, tools: List[BaseTool]) -> ToolNode:
        """Create a ToolNode with a fallback to handle errors."""
        return ToolNode(tools).with_fallbacks(
            [RunnableLambda(self._handle_tool_error)],
            exception_key="error"
        )
    
    def _handle_tool_error(self, state) -> dict:
        """Handle tool execution errors and return error messages."""
        error = state.get("error")
        tool_calls = state["messages"][-1].tool_calls
        return {
            "messages": [
                ToolMessage(
                    content=f"Error: {repr(error)}\n please fix your mistakes.",
                    tool_call_id=tc["id"],
                )
                for tc in tool_calls
            ]
        }
    
    def get_tools(self) -> List[BaseTool]:
        """Get all available tools."""
        return self.tools
    
    def get_specific_tools(self, tool_names: List[str]) -> List[BaseTool]:
        """Get specific tools by name."""
        return [tool for tool in self.tools if tool.name in tool_names] 