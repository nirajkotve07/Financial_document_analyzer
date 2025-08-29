## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

<<<<<<< HEAD
from crewai_tools import SerperDevTool, PDFSearchTool
from crewai.tools import BaseTool
from pydantic import Field
=======
from crewai_tools import tools
from crewai_tools.tools.serper_dev_tool import SerperDevTool
>>>>>>> 851790940b11093737b9bca8c6f23b0f1464ea65

## Creating search tool
search_tool = SerperDevTool()

<<<<<<< HEAD
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
=======
## Creating custom pdf reader tool
class FinancialDocumentTool():
    async def read_data_tool(path='data/sample.pdf'):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document file
        """
        
        docs = Pdf(file_path=path).load()

        full_report = ""
        for data in docs:
            # Clean and format the financial document data
            content = data.page_content
            
            # Remove extra whitespaces and format properly
>>>>>>> 851790940b11093737b9bca8c6f23b0f1464ea65
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
        return full_report
<<<<<<< HEAD
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
=======

## Creating Investment Analysis Tool
class InvestmentTool:
    async def analyze_investment_tool(financial_document_data):
        # Process and analyze the financial document data
        processed_data = financial_document_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
>>>>>>> 851790940b11093737b9bca8c6f23b0f1464ea65
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
<<<<<<< HEAD
=======
        # TODO: Implement investment analysis logic here
>>>>>>> 851790940b11093737b9bca8c6f23b0f1464ea65
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool:
<<<<<<< HEAD
    def create_risk_assessment_tool(self, financial_document_data):        
=======
    async def create_risk_assessment_tool(financial_document_data):        
        # TODO: Implement risk assessment logic here
>>>>>>> 851790940b11093737b9bca8c6f23b0f1464ea65
        return "Risk assessment functionality to be implemented"