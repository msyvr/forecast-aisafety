# Framework for AI safety forecasting

--- _Initial skeleton set up in collaboration with Claude._ ---

AI safety forecasting with trajectory analysis, using LLMs to synthesize expert opinions and track AI capabilities progress.

> 2025.08.17: Initial draft - WIP!

The motivation for this project is threefold:

1. Explore forecasting.
2. Explore the current landscape of AI safety forecasting.
3. Test out performance of different LLM models in this domain.

Automatic and timely database updates, comprehensive coverage of key data sources, and optimizing prompts will be some of the primary future goals for the project, alongside development of benchmarks that aren't represented in other forecasting datasets and dashboards.

The tech stack currently includes:

- Postgres: persistent data storage
- gpt-5-mini: cost-efficient LLM calls
- Python/Jupyter notebook: data exploration and experiments

TODO:

- dbt for data transformation management/versioning
- Streamlit: low-effort frontend, no-frills deploy - keeping in mind that, if this graduates from being a toy app, implementing a React frontend will be warranted
- Redis: cache query data and LLM calls
- Docker/docker-compose: self-contained deploy
- MCP server for LLM agents to manage database updates

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
