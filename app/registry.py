from typing import Callable, Dict, Any, Optional

class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}

    def register(self, name: str, func: Callable, description: str) -> None:
        self.tools[name] = {"func": func, "description": description}

    def get_tool(self, name: str) -> Optional[Dict[str, Any]]:
        return self.tools.get(name)

    def list_tools(self) -> str:
        return "\n".join([f"- {name}: {info['description']}" for name, info in self.tools.items()])
