## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import SerperDevTool, PDFSearchTool
from crewai.tools import BaseTool
from pydantic import Field

## Creating search tool
search_tool = SerperDevTool()

def read_financial_document(file_path):
    """Tool to read data from a pdf file from a path
    
    Args:
        file_path (str): The path to the pdf file.
        
    Returns:
        str: Full Financial Document file
    """
    try:
        docs = PDFSearchTool(file_path=file_path).load()
        full_report = ""
        for data in docs:
            content = data.page_content
            
            # Clean up extra newlines
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
        return full_report
    except Exception as e:
        return f"Error reading document: {e}"

## Creating a placeholder class for FinancialDocumentTool
class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = "Reads financial documents from PDF files"
    path: str = Field(default='data/sample.pdf', description="Path to the financial document PDF file")
    
    def _run(self):
        return read_financial_document(self.path)

## Creating Investment Analysis Tool
class InvestmentTool:
    def analyze_investment_tool(self, financial_document_data):
        processed_data = financial_document_data
        
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool:
    def create_risk_assessment_tool(self, financial_document_data):        
        return "Risk assessment functionality to be implemented"