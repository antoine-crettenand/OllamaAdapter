from typing import Optional, Dict, Any
from colorama import Fore, Style
from langchain_ollama import ChatOllama
from langchain.schema import SystemMessage, HumanMessage
from strictjson import strict_json


class Model:
    """
    Interface for interacting with a local or online LLM model.
    """
    def __init__(self, model_name: str = "llama3.1"):
        """
        Initializes the model interface.

        :param model_name: The name of the LLM model to use.
        """
        self.model: ChatOllama = ChatOllama(model=model_name)

    def llm(self, system_prompt: str, user_prompt: str) -> Optional[str]:
        """
        Sends a prompt to the LLM and returns the response.

        :param system_prompt: The system-level prompt guiding the model's behavior.
        :param user_prompt: The user's query or instruction.
        :return: The response from the model, or None if an error occurs.
        """

        try:
            response = self.model.invoke([
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt)
            ])
        except Exception as e:
            print(f"Error invoking the LLM: {e}")
            return None

        if response and hasattr(response, "content"):
            return response.content

        print("Received an empty response from the LLM.")
        return None

    def llm_task(self, system_prompt: str, user_prompt: str, output_format: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sends a structured task request to the LLM and returns the output in a strict JSON format.

        :param system_prompt: The system-level instructions for the model.
        :param user_prompt: The user-provided input.
        :param output_format: The expected JSON structure for the output.
        :return: A dictionary containing the formatted response or an empty dict on failure.
        """
        try:
            return strict_json(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                output_format=output_format,
                llm=self.llm
            )
        except Exception as e:
            print(f"Error processing structured LLM task: {e}")
            return {}
