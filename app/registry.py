class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, func, description):
        self.tools[name] = {"func": func, "description": description}

    def get_tool(self, name):
        return self.tools.get(name)

    def list_tools(self):
        return "\n".join([f"- {name}: {info['description']}" for name, info in self.tools.items()])