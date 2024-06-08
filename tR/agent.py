from llama_index.core.tools import FunctionTool
from llama_index.llms.ollama import Ollama
from llama_index.core.agent import ReActAgent

from functions import multiply

functions_defs = [
    multiply
]

tools = map(FunctionTool.from_defaults, functions_defs)

llm = Ollama(model="qwen:0.5b", request_timeout=120.0)

# initialize ReAct agent
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)

agent.chat("What is 2123 * 215123")