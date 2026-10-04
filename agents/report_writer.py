"""
Report Writer Agent

TODO: Implement this agent that produces a well-structured literature
review with proper citations.

Hints:
- Define a role focused on academic writing and communication
- Set a goal to produce a clear, well-organized literature review
- Write a backstory emphasizing clarity and proper attribution
- The output should be in markdown with sections:
  1. Executive Summary
  2. Introduction
  3. Methodology
  4. Findings (organized by theme)
  5. Discussion
  6. Conclusion
  7. References
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

# TODO: Create the report_writer agent
#
report_writer = Agent(
    role="Literature Review Academic Writer",
    goal="Write a clear and well-organized literature review surrounding a provided research question.",
    backstory=(
        "You are a highly experienced academic writer with 20+ years of experience writing literature reviews."
        "You always produce professional, organized and comprehensive reports to clearly address your given research question."
        "You organize your findings by theme and always properly cite the relevant sources"
        "You provide your literature reviews in markdown format with the following sections: Executive Summary, Introduction, Methodology, "
        "Findings (organized by theme), Discussion, Conclusion, References."
    ),
    tools=[],
    verbose=True,
    memory=True,
)

# Placeholder - replace with your implementation
# report_writer = None
