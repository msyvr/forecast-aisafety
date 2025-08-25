from llm_integration.config import llm_config
from database.models import AICapabilityMetric
from config.database import get_db_session
from typing import Dict
import json

class TrajectoryAnalyzer:
    
    def analyze_capability_trends(self, capability_area: str = None) -> Dict:
        
        db = get_db_session()
        
        query = db.query(AICapabilityMetric)
        if capability_area:
            query = query.filter(AICapabilityMetric.benchmark_type.contains(capability_area))
        
        capabilities = query.order_by(AICapabilityMetric.date_achieved).all()
        
        capability_data = []
        for cap in capabilities:
            capability_data.append({
                "model": cap.model_name,
                "benchmark": cap.benchmark_type,
                "score": cap.score,
                "date": cap.date_achieved.isoformat() if cap.date_achieved else None,
                "organization": cap.organization,
                "parameters": cap.parameters
            })
        
        prompt = f"""
        Analyze these AI capability trends:
        
        {json.dumps(capability_data, indent=2)}
        
        Identify:
        1. Rate of progress in different capability areas
        2. Which organizations are leading in which areas
        3. Potential acceleration or saturation patterns
        4. Timeline predictions for key capability milestones
        """
        
        schema = {
            "progress_rates": {},
            "leading_organizations": {},
            "trend_patterns": [],
            "capability_predictions": [],
            "acceleration_indicators": [],
            "potential_bottlenecks": [],
            "timeline_estimates": {}
        }
        
        db.close()
        return llm_config.get_structured_completion(prompt, schema)
    
    def evaluate_prediction_accuracy(self) -> Dict:
        
        # This would compare historical predictions vs actual outcomes
        # For now, provide framework for when real historical data is available
        
        prompt = """
        Based on the AI capability data available, analyze patterns in prediction accuracy:
        
        1. What factors make AI progress predictions more accurate?
        2. Which types of capabilities are hardest to predict?
        3. What methodological improvements could enhance forecasting?
        4. How do expert predictions compare to trend extrapolation?
        """
        
        schema = {
            "accuracy_factors": [],
            "prediction_challenges": [],
            "methodology_recommendations": [],
            "expert_vs_trend_analysis": "",
            "forecasting_improvements": [],
            "uncertainty_quantification": ""
        }
        
        return llm_config.get_structured_completion(prompt, schema)
    
    def generate_governance_insights(self) -> Dict:
        """AI progress trends vs. safety/governance goals"""
        
        db = get_db_session()
        capabilities = db.query(AICapabilityMetric).order_by(AICapabilityMetric.date_achieved.desc()).limit(20).all()
        
        recent_progress = []
        for cap in capabilities:
            recent_progress.append({
                "model": cap.model_name,
                "benchmark": cap.benchmark_type,
                "score": cap.score,
                "organization": cap.organization,
                "date": cap.date_achieved.isoformat() if cap.date_achieved else None
            })
        
        prompt = f"""
        Based on recent AI capability progress:
        
        {json.dumps(recent_progress, indent=2)}
        
        Analyze governance implications:
        1. What capability developments create new governance challenges?
        2. What regulatory responses might be needed and when?
        3. How should safety research priorities adapt to capability trends?
        4. What international coordination challenges emerge?
        """
        
        schema = {
            "governance_challenges": [],
            "regulatory_recommendations": {},
            "safety_research_priorities": [],
            "international_coordination_needs": [],
            "timeline_for_action": {},
            "policy_recommendations": []
        }
        
        db.close()
        return llm_config.get_structured_completion(prompt, schema)

trajectory_analyzer = TrajectoryAnalyzer()