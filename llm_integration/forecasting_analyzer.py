from llm_integration.config import llm_config
from database.models import Prediction, Forecaster, ForecastingQuestion
from config.database import get_db_session
from typing import Dict, List
import json

class ForecastingAnalyzer:

    def assess_rationale_quality(self, rationale_text: str) -> Dict[str, float]:
        prompt = f"""
        Analyze this forecasting rationale for quality:

        "{rationale_text}"

        Using a scale of 0-1, rate along each dimension:
        - clarity: How clear and well-structured is the reasoning?
        - evidence_quality: How robust is the evidence presented?
        - specificity: How specific and detailed is the analysis?
        - logical_consistency: How logically consistent is the argument?
        """

        schema = {
            "clarity": 0.0,
            "evidence_quality": 0.0,
            "specificity": 0.0,
            "logical_consistency": 0.0,
            "overall_score": 0.0,
            "key_strengths": "",
            "key_weaknesses": ""           
        }

        return llm_config.get_structured_completion(prompt, schema)
    
    def analyze_prediction_patterns(self, question_id: int) -> Dict:
        db = get_db_session()
        question = db.query(ForecastingQuestion).filter_by(id=question_id).first()
        predictions = db.query(Prediction).filter_by(question_id=question_id).all()

        if not predictions:
            return f'{"error": "No predictions found for question: {question}"}'
        
        prediction_data = []
        for p in predictions:
            forecaster = db.query(Forecaster).filter_by(id=p.forecaster_id).first()
            prediction_data.append({
                "prediction": p.prediction_value,
                "confidence": p.confidence,
                "expertise": forecaster.expertise_area if forecaster else "Unknown forecaster",
                "experience": forecaster.experience_level if forecaster else "Unknown forecaster",
                "rationale": p.rationale_text[:200] + "..." if len(p.rationale_text) > 200 else p.rationale_text
            })
        
        prompt = f"""
        Question: {question.question_text}

        Analyze these forecasting predictions:
        {json.dumps(prediction_data, indent=2)}

        Identify:
        1. Consensus areas vs disagreement
        2. Correlation between expertise and predictions
        3. Quality patterns in high vs low confidence predictions
        4. Common reasoning themes
        """

        schema = {
            "consensus_level": 0.0,
            "expert_agreement": 0.0,
            "confidence_patterns": "",
            "reasoning_themes": [],
            "prediction_quality_insights": "",
            "recommendations": ""
        }

        db.close()
        return llm_config.get_structured_completion(prompt, schema)
    
    def generate_forecasting_insights(self, category: str = None) -> Dict:
        db = get_db_session()
        query = db.query(Prediction).join(ForecastingQuestion)
        if category:
            query = query.filter(ForecastingQuestion.category == category)

        # Customize the limit according to acceptable costs for LLM API calls.
        predictions = query.limit(25).all()

        if not predictions:
            return {"error": "No predictions found for any forecasting questions"}
        
        analysis_data = []
        for p in predictions:
            forecaster = db.query(Forecaster).filter_by(id=p.forecaster_id).first()
            analysis_data.append({
                "question_category": p.question.category,
                "prediction_value": p.prediction_value,
                "confidence": p.confidence,
                "forecaster_experience": forecaster.experience_level if forecaster else "Unknown forecaster",
                "forecaster_expertise": forecaster.expertise_area if forecaster else "Unknown forecaster",
                "track_record": forecaster.track_record_score if forecaster else 0.5
            })

        # Adapt the prompt parameter for number of elements from analysis_data sufficient for context.
        prompt = f"""
        Analyze these forecasting patterns to identify the factors that make predictions successful:

        {json.dumps(analysis_data[:10], indent=2)}

        Focus on:
        1. Which forecaster characteristics correlate with better performance?
        2. What patterns exist between confidence and accuracy?
        3. Are there category-specific insights?
        4. What makes rationales effective?
        """

        schema = {
            "key_success_factors": [],
            "experience_impact": "",
            "confidence_accuracy_relationship": "",
            "category_insights": {},
            "recommendations_for_forecasters": [],
            "methodology_improvements": []            
        }

        db.close()
        return llm_config.get_structured_completion(prompt, schema)
    
forecasting_analyzer = ForecastingAnalyzer()
