from crewai import Crew

from agents.query_expander import query_expander

if __name__ == '__main__':
    crew = Crew(
            agents=[query_expander],
            tasks=[],
            verbose=True,
            memory=True,
        )
    crew.reset_memories('all')