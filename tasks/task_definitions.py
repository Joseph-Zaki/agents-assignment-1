"""
Task Definitions for Research Crew

TODO: Define the four sequential tasks:
1. Query Expansion - Break down the research question
2. Source Hunting - Search the paper corpus
3. Synthesis - Analyze and synthesize findings
4. Report Writing - Generate the literature review

Each task should:
- Have a clear description telling the agent what to do
- Specify the agent responsible
- Define expected_output format
- Use context parameter to pass information between tasks
"""

from crewai import Task

from agents import query_expander, report_writer, source_hunter, synthesizer


def create_research_tasks(research_question: str) -> list[Task]:
    """
    Create the task pipeline for a research question.

    Args:
        research_question: The user's research question

    Returns:
        List of 4 tasks in execution order

    TODO: Implement the four tasks below
    """

    # =========================================
    # Task 1: Query Expansion
    # =========================================
    # TODO: Create a task that breaks down the research question
    # into sub-questions, keywords, and search angles
    #
    expand_task = Task(
        description=f"Given the following question: \'{research_question}\', break down the research question into smaller sub-questions. \
                    The sub-questions should be narrow conceptually and clearly ask for information that will inform the answer to the larger question. \
                    Identify relevant keywords for each sub-question and suggest possible search paths for determining the answer to the research question. \
                    Make sure the sub-questions adequately capture all information needed to answer the research question.",
        agent=query_expander,
        expected_output="An expanded query including an enumerated list of sub-questions with their relevant keywords and potential search paths."
    )

    # =========================================
    # Task 2: Source Hunting
    # =========================================
    # TODO: Create a task that searches the paper corpus
    # Hint: Use context=[expand_task] to pass the query strategy
    #
    search_task = Task(
        description="Use the search_papers tool to research each of the sub-questions in the provided expanded query. \
                    Return only content relevant to each question and clearly identify the source of each piece of information. \
                    For each source found, briefly explain how it addresses the topic.",
        agent=source_hunter,
        context=[expand_task],
        expected_output="A focused and structured report with a section for each sub-question, the source material relevant to it, and clear citations. \
                        Include at least 3 sources for each sub-question."
    )

    # =========================================
    # Task 3: Synthesis
    # =========================================
    # TODO: Create a task that synthesizes findings into themes
    # Hint: Use context=[expand_task, search_task] for full context
    #
    synthesis_task = Task(
        description="Using the research provided, synthesize the findings into themes. \
                    Clearly identify the relevant themes, debates, and gaps across the provided sources. \
                    Call out any discrepancies and assumptions.",
        agent=synthesizer,
        context=[expand_task, search_task],
        expected_output="A clear and throrough markdown document identifying the main themes relvant to the questions asked along with the \
                        source citations for each claim made. Each section should correspond to a single theme and you should have sub-sections for \
                        summary of findings, assumptions and considerations, and comparison to other sources."
    )

    # =========================================
    # Task 4: Report Writing
    # =========================================
    # TODO: Create a task that writes the final literature review
    # Hint: Use context=[expand_task, search_task, synthesis_task]
    #
    report_task = Task(
        description="Using the provided expanded query, the identified relevant sources, and the synthesis report, write a clear and structured literature review \
                    addressing the questions and themes in the expanded query. Make sure to clearly cite sources used. Discuss how different sources support \
                    each other and interact. Identify any gaps in the currently available literature.",
        agent=report_writer,
        context=[expand_task, search_task, synthesis_task],
        expected_output="A structured and professionally written literature review with clear citations for all sources used." \
        "The document should cleary address the questions provided." \
        """The document should be in markdown with sections: 
          1. Executive Summary
          2. Introduction
          3. Methodology
          4. Findings (organized by theme)
          5. Discussion
          6. Conclusion
          7. References"""
    )

    # TODO: Return your tasks in order
    return [expand_task, search_task, synthesis_task, report_task]

    # Placeholder - replace with your implementation
    raise NotImplementedError(
        "TODO: Implement create_research_tasks() in tasks/task_definitions.py"
    )
