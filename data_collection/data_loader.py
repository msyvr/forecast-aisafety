from config.database import get_db_session, create_tables
from database.models import *
from data_collection.collectors.synthetic_data import *
import pandas as pd

def load_all_seed_data():
    """Load all seed data into databases"""

    create_tables()
    db = get_db_session()

    try:
        print('Loading forecasters...')
        forecasters_df = generate_forecasters()
        for _, row in forecasters_df.iterrows():
            forecaster = Forecaster(**row.to_dict())
            db.add(forecaster)
        db.commit()

        print('Loading forecasting questions...')
        questions_df = generate_forecasting_questions()
        for _, row in questions_df.iterrows():
            question = ForecastingQuestion(**row.to_dict())
            db.add(question)
        db.commit()

        print('Loading AI safety scenarios...')
        scenarios_df = generate_ai_safety_scenarios()
        for _, row in scenarios_df.iterrows():
            scenario = AISafetyScenario(**row.to_dict())
            db.add(scenario)
        db.commit()

        print('Loading AI capabilities...')
        capabilities_df = generate_ai_capabilities()
        for _, row in capabilities_df.iterrows():
            capability = AICapabilityMetric(**row.to_dict())
            db.add(capability)
        db.commit()

        print("Generating predictions...")
        generate_sample_predictions(db)

        print('All seed data loaded successfully')

    except Exception as e:
        print(f'Error loading data: , {e}')
        db.rollback()
    finally:
        db.close()

def generate_sample_predictions(db):
    """Generate sample predictions for questions"""
    questions = db.query(ForecastingQuestion).all()
    forecasters = db.query(Forecaster).all()

    for question in questions:
        num_predictions = random.randint(3, 8)
        selected_forecasters = random.sample(forecasters, min(num_predictions, len(forecasters)))

        for forecaster in selected_forecasters:
            prediction = Prediction(
                question_id = question.id,
                forecaster_id = forecaster.id,
                prediction_value = round(random.uniform(0.1, 0.9), 2),
                confidence = round(random.uniform(0.5, 0.95), 2),
                rationale_text = f'Based on my expertise in {forecaster.expertise_area}, I believe this outcome has moderate probability due to current trends and available evidence.',
                timestamp = datetime.now(timezone.utc) - timedelta(days=random.randint(1, 100))
            )
            db.add(prediction)

    db.commit()

if __name__ == "__main__":
    load_all_seed_data()
