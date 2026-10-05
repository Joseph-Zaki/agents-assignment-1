"""
Synthesizer Agent

TODO: Implement this agent that analyzes collected sources to identify
themes, agreements, contradictions, and gaps in the literature.

Hints:
- Define a role focused on synthesis and analysis
- Set a goal to identify themes, consensus, debates, and gaps
- Write a backstory emphasizing pattern recognition across sources
- This agent primarily reasons - may not need tools
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

# TODO: Create the synthesizer agent

synthesizer = Agent(
    role="Research Source Analyst",
    goal=(
        "Carefully and thoroughly analyze provided sources and their relevance to the provided query. "
        "Identify themes, consensus, contradictions, and gaps in the sources. "
        "Produce meaningful insights based on the reviewed sources and tie your findings to the research question."
    ),
    backstory=(
        "You are an expert research with 20 years of experience in analyzing academic sources and their efficacy in addressing research topics."
        "You pay close attention to patterns across sources and identify common themes, agreements, contradictions, assumptions, and knowledge gaps."
        "You always provide an organized, clear, and comprehensive synthesis of your findings across the provided sources, always addressing the target research question."
    ),
    tools=[],
    verbose=True,
    memory=True,
)

# Placeholder - replace with your implementation
# synthesizer = None
