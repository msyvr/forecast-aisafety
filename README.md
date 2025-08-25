# Framework for AI safety forecasting

--- _Initial skeleton set up in collaboration with Claude._ ---

AI safety forecasting with trajectory analysis, using LLMs to synthesize expert opinions and track AI capabilities progress.

> 2025.08.17: Initial draft - WIP!

The motivation for this project is threefold:

1. Explore forecasting.
2. Explore the current landscape of AI safety forecasting.
3. Test out performance of different LLM models in this domain.

Automatic and timely database updates, comprehensive coverage of key data sources, and optimizing prompts will be some of the primary future goals for the project, alongside development of benchmarks that aren't represented in other forecasting datasets and dashboards.

## Tech stack

- PostgreSQL: persistent storage
- Redis: cache query data
- Streamlit: low-effort frontend/viz, no-frills deploy
  - if this grows beyond being a toy app, move to a more performant frontend
- Docker: self-contained deploy
- Airflow: data scheduler
- MCP/CrewAI: orchestrate LLM agents (separate from target data source API polling)

  - analyze websites and newsletters for relevant new/updated datasets
  - analyze expert chatter and evaluate the system (LLM as judge of the forecasting system)

- _dbt: data transformation management/versioning (possibly overkill)_

## Use

```bash
git clone git@github.com:msyvr/forecast-aisafety
cd forecast-aisafety
# Setup environment
cp .env.example .env
# Edit .env with your configuration

# Initialize database and load seed data
python run_app.py

# Explore data
jupyter notebook notebooks/data_exploration.ipynb
```

## Tech stack

- [fireducks](https://fireducks-dev.github.io/): drop-in replacement for pandas with identical api (literally, just import fireducks as pd, no other changes)
  - [performance vs polars, duckdb, pandas](https://blog.dailydoseofds.com/p/fireducks-vs-pandas-vs-duckdb-vs)
- better known but, coming from pandas, the api takes getting used to - [polars](https://docs.pola.rs/user-guide/misc/comparison/): multithreaded on a single node (for distributed processing, use Apache Spark); pandas is single-threaded
- [ibis](https://ibis-project.org/tutorials/basics): [notes from a fan](https://www.reddit.com/r/Python/comments/16gciot/underused_library_ibis_dataframe_frontend_sql/)
