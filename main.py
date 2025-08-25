from config.database import get_db_session
from database.models import ForecastingQuestion
from data_collection.data_loader import load_all_seed_data

def setup_database():
    print('Setting up AI Safety Forecasting Database...')

    try:
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
    print('AI Safety Forecasting')
    print('Setup the database...')

    setup_database()

    print('Database is loaded with seed data. Next steps:')
    print('- Run jupyter notebook to explore the data.')

if __name__ == "__main__":
    main()
