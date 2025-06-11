import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import PendingRollbackError
from langchain_community.utilities import SQLDatabase

class DatabaseManager:
    def __init__(self):
        self.MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
        self.MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
        self.MYSQL_HOST = os.getenv("MYSQL_HOST")
        self.MYSQL_PORT = os.getenv("MYSQL_PORT")
        self.MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
        
        self.engine = self._create_engine()
        self.db = SQLDatabase(self.engine)
    
    def _create_engine(self):
        """Create SQLAlchemy engine with MySQL connection."""
        return create_engine(
            f"mysql+pymysql://{self.MYSQL_USERNAME}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
        )
    
    def execute_query(self, query: str) -> pd.DataFrame:
        """Execute SQL query and return results as DataFrame."""
        try:
            return pd.read_sql(query, self.engine)
        except PendingRollbackError:
            print("Rolling back due to pending transaction...")
            self.engine.rollback()
            return pd.read_sql(query, self.engine)
    
    def get_tables_info(self) -> pd.DataFrame:
        """Get information about all tables in the database."""
        query = """
        SELECT
            table_name,
            table_rows
        FROM
            INFORMATION_SCHEMA.TABLES
        WHERE
            table_schema = %s;
        """
        return self.execute_query(query, params=[self.MYSQL_DATABASE]) 