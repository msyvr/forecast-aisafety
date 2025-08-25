## Accessing and retrieving data from source

Code to automate periodic or triggered retrieval is essential.
A scheduler like Airflow can be used to run the pipeline at
designated periodicity and days/times.

The following also should be accommodated from within the same
data pipeline (via CLI script or integration into a team data
management portal/dashboard) to ensure protocols are
respected and metadata is consistent:

1. manual upload via API
2. manual upload from a file

On retrieval, update both the target database as well as the
data_sources database. The metadata for these tables should
not be impacted by retrieved data.

### Sources that publish their data with an API

Each such source will have an entry in the data_source database.

Code to automate data retrieval will be included in this project.
On retrieval, the target db is updated, as is the data_source db.

### Sources that publish their data, no API

The CLI scripts or app-based update utility will trigger
data_source database updates (manual, if necessary).

The scripts/app will target only registered target databases,
and retrieved data will pass through the same pipeline as
automatically-retrieved data.

### Indirect sources

- AI folks on social (e.g., Twitter)
- AI newsletters
