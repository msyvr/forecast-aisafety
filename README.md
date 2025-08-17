# WIP! AI Safety Forecasting Database

AI safety forecasting with AI research trajectory analysis, using LLMs to synthesize expert opinions and track AI capabilities progress.

> 2025.08.17: A first pass which will be improved.

The motivation for this project is threefold:

1. Get a feel for forecasting.
2. Explore the current landscape of AI safety forecasting.
3. Test out performance of different LLM models in this domain.

For those particular goals, the latest and greatest data isn't required. However, that will be one of the primary future goals for the project, alongside development of benchmarks that aren't represented in other forecasting datasets and dashboards.

The tech stack may evolve but currently includes:

- Postgres: persistent data storage
- _Redis: cache query data and LLM calls_
- gpt-5-mini: cost-efficient LLM calls
- Python/Jupyter notebook: easily explore the data and run experiments
- Streamlit: built-in support for visualizations
- _Docker/docker-compose: self-contained deploy_

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
