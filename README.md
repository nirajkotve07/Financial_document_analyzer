# Financial Document Analyzer

## Project Description
A brief description of what this project does. (e.g., An application that analyzes financial documents using AI agents, built with CrewAI and FastAPI.)

## Status
The core application infrastructure is now stable. All initial dependency and code bugs have been resolved, and the application is ready for LLM configuration.

## Bugs Found and How They Were Fixed
This section details the issues I encountered and the steps taken to resolve them.

### Dependency Conflicts
- **OpenAI version conflict:** The `openai` library version (`1.30.5`) conflicted with the `litellm` dependency.
  - **Fix:** Updated `requirements.txt` from `openai==1.30.5` to `openai>=1.68.2`.

- **Pydantic-core version conflict:** The `pydantic-core` version (`2.8.0`) caused compatibility issues with `pydantic`.
  - **Fix:** Updated `requirements.txt` from `pydantic_core==2.8.0` to `pydantic_core>=2.14.1`.

### Code Bugs
- **CrewAI Import Errors:** The application used a deprecated `agent_builder` module.
  - **Fix:** Updated `agents.py` to use the correct import statement: `from crewai import Agent`.

- **Tool Validation Errors:** The `FinancialDocumentTool` was not properly defined for use with CrewAI.
  - **Fix:** Updated `tools.py` to ensure `FinancialDocumentTool` properly inherits from `crewai.tools.base_tool.BaseTool` and correctly defines the `path` parameter with a Pydantic field.

- **Function vs. Tool Confusion:** The main application was calling the tool's raw function instead of a tool instance.
  - **Fix:** Updated `main.py` to correctly instantiate and use `FinancialDocumentTool` objects.

## Setup Instructions
Follow these steps to set up the project locally.

1.  **Install Python 3.12:**
    This project is tested with and requires **Python 3.12**. You can download it from the [official Python website](https://www.python.org/downloads/).

2.  **Clone the repository:**
    ```bash
    git clone [Your Repository Link Here]
    cd [Your Repository Name]
    ```

3.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure your LLM:**
    Create a `.env` file in the project root and add your API key. (e.g., `GEMINI_API_KEY=your_key_here`). Note: This project uses `litellm` which may require a specific format for API keys.

## Usage Instructions
To start the FastAPI application:

```bash
uvicorn main:app --reload


I understand. You want to update the README.md file to explicitly state that the project requires Python 3.12. This is a good practice to ensure consistency and avoid compatibility issues for other users.

Here is the updated README.md template with the Python version requirement added to the setup instructions.

Markdown

# Financial Document Analyzer

## Project Description
A brief description of what this project does. (e.g., An application that analyzes financial documents using AI agents, built with CrewAI and FastAPI.)

## Status
The core application infrastructure is now stable. All initial dependency and code bugs have been resolved, and the application is ready for LLM configuration.

## Bugs Found and How They Were Fixed
This section details the issues I encountered and the steps taken to resolve them.

### Dependency Conflicts
- **OpenAI version conflict:** The `openai` library version (`1.30.5`) conflicted with the `litellm` dependency.
  - **Fix:** Updated `requirements.txt` from `openai==1.30.5` to `openai>=1.68.2`.

- **Pydantic-core version conflict:** The `pydantic-core` version (`2.8.0`) caused compatibility issues with `pydantic`.
  - **Fix:** Updated `requirements.txt` from `pydantic_core==2.8.0` to `pydantic_core>=2.14.1`.

### Code Bugs
- **CrewAI Import Errors:** The application used a deprecated `agent_builder` module.
  - **Fix:** Updated `agents.py` to use the correct import statement: `from crewai import Agent`.

- **Tool Validation Errors:** The `FinancialDocumentTool` was not properly defined for use with CrewAI.
  - **Fix:** Updated `tools.py` to ensure `FinancialDocumentTool` properly inherits from `crewai.tools.base_tool.BaseTool` and correctly defines the `path` parameter with a Pydantic field.

- **Function vs. Tool Confusion:** The main application was calling the tool's raw function instead of a tool instance.
  - **Fix:** Updated `main.py` to correctly instantiate and use `FinancialDocumentTool` objects.

## Setup Instructions
Follow these steps to set up the project locally.

1.  **Install Python 3.12:**
    This project is tested with and requires **Python 3.12**. You can download it from the [official Python website](https://www.python.org/downloads/).

2.  **Clone the repository:**
    ```bash
    git clone [Your Repository Link Here]
    cd [Your Repository Name]
    ```

3.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure your LLM:**
    Create a `.env` file in the project root and add your API key. (e.g., `GEMINI_API_KEY=your_key_here`). Note: This project uses `litellm` which may require a specific format for API keys.

## Usage Instructions
To start the FastAPI application:

```bash
uvicorn main:app --reload
The server will run on http://127.0.0.1:8000.

API Documentation
The API documentation is automatically generated by FastAPI. Once the server is running, you can access the interactive docs at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

The primary endpoint is:

POST /process_document

Description: Initiates the financial document analysis process.

Request Body:

JSON

{
  "file_path": "path/to/your/document.pdf"
}
Response:
Returns a JSON object with the analysis results.






