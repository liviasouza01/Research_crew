# ResearchCrew

Welcome to the ResearchCrew Crew project, powered by [crewAI](https://crewai.com). This project is designed to analyze academic documents (theses, articles, research papers) using a multi-agent AI system. The crew consists of two specialized agents that collaborate to provide comprehensive technical critiques and constructive improvement recommendations for academic work.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `API_KEY` into the `.env` file**

- **Add your academic documents**: Place PDF files in the `knowledge/` directory. The crew will analyze any document you place there.
- Modify `src/research_crew/config/agents.yaml` to define your agents' personalities and expertise
- Modify `src/research_crew/config/tasks.yaml` to customize the analysis criteria and output format
- Modify `src/research_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/research_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the research_crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

The crew will:

1. **Critical Analysis**: A rigorous professor agent analyzes the document for technical gaps, weaknesses, and methodological issues
2. **Constructive Analysis**: A supportive professor agent reviews the critique and provides detailed improvement recommendations

The final output will be saved as `report.md` in the root folder, containing a comprehensive academic advisory report with actionable recommendations.

## Understanding Your Crew

The research_crew Crew is composed of two specialized AI agents:

1. **Rigid Professor** (`rigid_professor`): Performs critical analysis, identifying technical flaws, gaps, and weaknesses across all sections of the academic document. This agent is thorough and uncompromising in finding issues.
2. **Positive Professor** (`positive_professor`): Reviews the critique and provides constructive solutions, detailed improvement recommendations, and a prioritized roadmap. This agent balances criticism with actionable guidance.

These agents collaborate on a series of tasks defined in `config/tasks.yaml`, leveraging their collective skills to provide comprehensive academic feedback. The `config/agents.yaml` file outlines the capabilities and configurations of each agent.

### Workflow

1. Place your academic document (PDF) in the `knowledge/` directory
2. Run `crewai run` to start the analysis
3. The rigid professor analyzes the document and creates a technical critique
4. The positive professor reviews the critique and creates a comprehensive advisory report
5. Review the `report.md` file for detailed feedback and recommendations

## Support

For support, questions, or feedback regarding the ResearchCrew Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
