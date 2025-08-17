"""
AI Safety Forecasting Database
Main application entry point for development
"""

import os
from config.database import create_tables
from data_collection.data_loader import load_all_seed_data

def setup_database():
    """Initialize database and load seed data"""
    print('Setting up AI Safety Forecasting Database...')

    try:
        from config.database import get_db_session
        from database.models import ForecastingQuestion

        db = get_db_session()
        question_count = db.query(ForecastingQuestion).count()

        if question_count == 0:
            print('No data found. Loading seed data...')
            load_all_seed_data()
        else:
            print(f'Database already contains {question_count} questions.')

    except Exception as e:
        print(f'Setting up fresh database: {e}')
        load_all_seed_data()

def main():
    """Main application entry point"""
    print('--- AI Safety Forecasting Database ---')
    print('Setup the database...')

    setup_database()

    print('Database is loaded with seed data. Next steps:')
    print('- Run jupyter notebook to explore the data.')
    print('- Add LLM integration.')
    print('- Build Streamlit dashboard.')

if __name__ == "__main__":
    main()
