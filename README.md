# Model Interface

## Overview
This repository provides an interface for interacting with a local or online LLM (Large Language Model) using `langchain_ollama`. It includes functionalities for general LLM interactions and structured task execution with JSON formatting.

## Features
- Sends system and user prompts to an LLM.
- Retrieves responses from the model.
- Processes structured tasks with strict JSON output.
- Uses `colorama` for colored logging messages.
- Error handling and logging for better debugging.

## Installation
Ensure you have Python installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
### Initializing the Model
```python
from model import Model

model = Model()
```

### Sending a Prompt
```python
response = model.llm("System Prompt Example", "User input question")
print(response)
```

### Executing a Structured Task
```python
output_format = {"key": "value"}
response = model.llm_task("System Prompt Example", "User input question", output_format)
print(response)
```

## Dependencies
- `colorama`
- `langchain_ollama`
- `strictjson`

## License
This project is licensed under the MIT License.