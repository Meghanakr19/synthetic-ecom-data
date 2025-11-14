# synthetic-ecom-data

Synthetic E-commerce Data Generator and SQLite Integration. This project
generates synthetic e-commerce data, loads it into a SQLite database, and
performs analysis via SQL queries.

## Files
- `generate_data.py` – uses Faker + Pandas to create CSVs
- `load_to_sqlite.py` – loads CSVs into `ecommerce.db`
- `query_data.py` – runs SQL join queries and exports output

## Usage
1. `python generate_data.py`
2. `python load_to_sqlite.py`
3. `python query_data.py`

## Technology Stack
- Python
- Pandas
- SQLite
- Git + GitHub
