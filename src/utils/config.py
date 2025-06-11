import os
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

class LLMConfig(BaseModel):
    """Configuration for Language Models"""
    model_name: str = "gpt-4o"
    temperature: float = 0.1
    max_tokens: Optional[int] = None
    streaming: bool = False
    
    def get_llm(self) -> ChatOpenAI:
        """Initialize and return ChatOpenAI instance with current config"""
        return ChatOpenAI(
            model_name=self.model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            streaming=self.streaming
        )

class Config:
    """Main configuration class"""
    def __init__(self):
        # API Keys
        self.openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
        
        # Database configs
        self.db_host: str = os.getenv("DB_HOST", "localhost")
        self.db_port: int = int(os.getenv("DB_PORT", "3306"))
        self.db_name: str = os.getenv("DB_NAME", "")
        self.db_user: str = os.getenv("DB_USER", "")
        self.db_password: str = os.getenv("DB_PASSWORD", "")
        
        # LLM Configuration
        self.llm_config = LLMConfig()
    
    @property
    def database_url(self) -> str:
        """Construct database URL from components"""
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    def get_llm(self) -> ChatOpenAI:
        """Get configured LLM instance"""
        return self.llm_config.get_llm()