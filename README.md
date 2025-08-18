# Framework for AI safety forecasting

AI safety forecasting with AI research trajectory analysis, using LLMs to synthesize expert opinions and track AI capabilities progress.

> 2025.08.17: Initial draft - WIP!

The motivation for this project is threefold:

1. Get a feel for forecasting.
2. Explore the current landscape of AI safety forecasting.
3. Test out performance of different LLM models in this domain.

Automatic and timely database updates, comprehensive coverage of key data sources, and optimizing prompts will be some of the primary future goals for the project, alongside development of benchmarks that aren't represented in other forecasting datasets and dashboards.

The tech stack currently includes:

- Postgres: persistent data storage
- gpt-5-mini: cost-efficient LLM calls
- Python/Jupyter notebook: data exploration and experiments

Planned additions:

- _Streamlit: low-effort frontend, no-frills deploy - keeping in mind that, if this graduates from being a toy app, implementing a React frontend will be warranted_
- _Redis: cache query data and LLM calls_
- _Docker/docker-compose: self-contained deploy_
- _MCP server for LLM agents to manage database updates_

## Use

```bash
# Setup environment
cp .env.example .env
# Edit .env with your configuration

# Initialize database and load seed data
python run_app.py

# Explore data
jupyter notebook notebooks/data_exploration.ipynb
```
