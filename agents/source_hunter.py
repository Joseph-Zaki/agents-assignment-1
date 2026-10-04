"""
Source Hunter Agent

TODO: Implement this agent that searches the curated paper corpus
to find relevant passages for each sub-question in the query strategy.

Hints:
- This agent MUST use the search_papers tool from tools.paper_rag_tool
- Define a role focused on investigation and source discovery
- Set a goal to find 8-12 relevant passages
- Write a backstory emphasizing thoroughness and not stopping at first results
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

from tools.paper_rag_tool import search_papers

# TODO: Create the source_hunter agent
#
source_hunter = Agent(
    role="Academic Literature Sourcer",
    goal="Search academic papers and sources for 8-12 relevant passages and their citations to given research topic(s).",
    backstory=(
        "You are a specialist in searching a corpus of sources for the most relevant passages to a given query." \
        "You are always very thorough and perform a comprehensive search, not simply returning the first result without considering all options." \
        "You always provide specific citations for each passage you provide."
    ),
    tools=[search_papers],  # This tool is required!
    verbose=True,
    memory=True,
)

# Placeholder - replace with your implementation
# source_hunter = None
