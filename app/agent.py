import os
import json
from openai import OpenAI
from .registry import ToolRegistry
from .logger import log_action

class MiniAgent:
    def __init__(self, registry: ToolRegistry, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.registry = registry
        self.model = model


    def run(self, prompt: str):
        system_prompt = f"""
        Sei un assistente intelligente. Hai accesso a questi tool:
        {self.registry.list_tools()}
        
        Rispondi ESCLUSIVAMENTE in formato JSON con questa struttura:
        {{
            "tool": "nome_tool_o_null",
            "params": {{ "param1": "valore" }},
            "answer": "La tua risposta testuale se il tool è null o non necessario"
        }}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )

        data = json.loads(response.choices[0].message.content)
        tool_name = data.get("tool")
        params = data.get("params", {})
        direct_answer = data.get("answer")

        # Se l'LLM ha scelto un tool valido
        if tool_name and self.registry.get_tool(tool_name):
            try:
                func = self.registry.get_tool(tool_name)["func"]
                result = func(**params)
                log_action(tool_name, prompt, result)
                return f"[TOOL {tool_name}] {result}"
            except Exception as e:
                error_msg = f"Error executing tool {tool_name}: {str(e)}"
                log_action(tool_name, prompt, error_msg)
                return f"[ERROR] {error_msg}"

        
        # Fallback: Risposta diretta dell'LLM
        return direct_answer