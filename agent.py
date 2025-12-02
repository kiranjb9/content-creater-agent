from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
import os

load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# if not GROQ_API_KEY:
#     raise RuntimeError("GROQ_API_KEY not set. Add it to Vercel env vars or a local .env for development.")

@tool
def save_content(filename: str, content: str) -> str:
    """Save generated content to a file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully saved content to '{filename}' ({len(content)} characters)."
    except Exception as e:
        return f"Error saving file: {str(e)}"


@tool
def read_content(filename: str) -> str:
    """Read existing content from a file for refinement."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"Contents of '{filename}':\n{content}"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"


TOOLS = [save_content, read_content]

SYSTEM_MESSAGE = (
    "You are a professional content creation assistant. Your role is to help users "
    "generate, refine, and optimize written content across multiple formats. "
    "\n\nCapabilities:"
    "\n- Write blog posts, articles, and long-form content with engaging narratives"
    "\n- Create social media posts (Twitter, LinkedIn, Instagram captions) tailored to platform tone"
    "\n- Draft marketing copy, product descriptions, and promotional content"
    "\n- Edit and refine existing content for clarity, tone, and engagement"
    "\n- Suggest headlines, meta descriptions, and call-to-action statements"
    "\n- Adapt content for different audiences and skill levels"
    "\n- Maintain brand voice consistency across all content"
    "\n\nGuidelines:"
    "\n- Always ask for context: target audience, purpose, tone (professional/casual/creative)"
    "\n- Provide multiple variations when asked"
    "\n- Optimize for SEO when relevant"
    "\n- Keep content concise, scannable, and action-oriented"
    "\n- Be creative but factually accurate"
    "\n- Format output clearly with headers and bullet points where appropriate"
    "\n- Provide trending Hashtags for social media posts"
)

llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.7)
agent = create_agent(llm, TOOLS, system_prompt=SYSTEM_MESSAGE)


def run_content_creator(user_input: str) -> str:
    """Run the content creator agent with a user query."""
    try:
        result = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config={"recursion_limit": 50}
        )
        return result["messages"][-1].content
    except Exception as e:
        return f"Error: {str(e)}"


# Example usage:
# if __name__ == "__main__":
#     query = "Write a LinkedIn post about AI agents in business, keep it professional but engaging"
#     print(run_content_creator(query))