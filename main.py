from pydantic_ai import Agent
import re
from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    model = GeminiModel('gemini-1.5-flash',
                        api_key=os.getenv('GEMINI_API_KEY'))
    with open("input.txt", "r") as f:
        raw_text = f.read()
    agent = Agent(model, deps_type=str, system_prompt=(
        "You are an AI Assistant that has professional skills to transform tailwind html components into Rust's Yew html! macro", "Your job will be transforming following tailwind html components into Rust's Yew html! macro"))

    result = agent.run_sync(raw_text, deps="TailwindCSS to Yew View Macro")
    pattern = r'```rust(.*?)```'
    matches = re.findall(pattern, result.data, re.DOTALL)

    print(matches[0].strip())
    with open("output.txt", "w") as f:
        f.write(matches[0].strip())
