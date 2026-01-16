from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from typing import List
import os

os.environ.setdefault('CREWAI_EMBEDDING_MODEL', 'sentence-transformers/all-MiniLM-L6-v2')

@CrewBase
class ResearchCrew():
    """ResearchCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Create a knowledge source from text and pdf files in the knowledge folder
    def _get_knowledge_source(self):
        knowledge_path = "knowledge"
        sources = []
        
        if os.path.exists(knowledge_path):
            for file in os.listdir(knowledge_path):
                # Passamos apenas o nome do arquivo (ex: "documento.pdf")
                # O CrewAI automaticamente procura dentro da pasta "knowledge/"
                if file.endswith('.txt'):
                    sources.append(TextFileKnowledgeSource(
                        file_paths=[file]
                    ))
                elif file.endswith('.pdf'):
                    sources.append(PDFKnowledgeSource(
                        file_paths=[file]
                    ))
        return sources

    @agent
    def rigid_professor(self) -> Agent:
        return Agent(
            config=self.agents_config['rigid_professor'], # type: ignore[index]
            verbose=True
        )

    @agent
    def positive_professor(self) -> Agent:
        return Agent(
            config=self.agents_config['positive_professor'], # type: ignore[index]
            verbose=True
        )

    @task
    def critical_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['critical_analysis_task'], # type: ignore[index]
        )

    @task
    def constructive_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['constructive_analysis_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResearchCrew crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            knowledge_sources=self._get_knowledge_source()
        )
