## Options for data transformation

To interact with an unstructured database that's accessed via
an API, use Python. Once the data is in a structured database,
SQL is the most efficient way to access select data.

## Visualization tools

Transformations enable appropriate data access for dashboards
and other visualization tools.

Transformations to generate materialized views are helpful
for streamlining data that will be accessed as a data frame
for Python-drive visualization or other processing.

## Transformation subtleties of note

### Assumptions implicit in transformations

- operation implicitly assumes a specific statistical distribution
- operation assumes independence of variables
- aggregation assumes acceptable loss of resolution

## Transformation tools and versioning

(Just the beginnings of a list, which will not be comprehensive
for this small project. Unordered, they are not recommendations
as they haven't yet been vetted for utility or suitability.)

- dbt: useful for less technical teams (reduces complex queries
  to select statements)
- cosmos
- dvc: open source versioning tool
- lakefs (versioning built in)
- iceberg
