from llm_integration.config import llm_config
from database.models import AISafetyScenario, ExpertPrediction, Forecaster
from config.database import get_db_session
from typing import Dict, List
import json

class SafetyAnalyzer:
    
    def synthesize_safety_concerns(self, risk_category: str = None) -> Dict:
        """Synthesize expert opinions on AI safety scenarios"""
        
        db = get_db_session()
        query = db.query(AISafetyScenario)
        if risk_category:
            query = query.filter_by(risk_category=risk_category)
        
        scenarios = query.all()
        
        scenario_data = []
        for scenario in scenarios:
            expert_preds = db.query(ExpertPrediction).filter_by(scenario_id=scenario.id).all()
            
            predictions = []
            for pred in expert_preds:
                expert = db.query(Forecaster).filter_by(id=pred.expert_id).first()
                predictions.append({
                    "p_doom": pred.p_doom,
                    "confidence": pred.confidence,
                    "reasoning": pred.reasoning[:300] + "..." if len(pred.reasoning) > 300 else pred.reasoning,
                    "expertise": expert.expertise_area if expert else "Unknown"
                })
            
            scenario_data.append({
                "scenario": scenario.scenario_description,
                "risk_category": scenario.risk_category,
                "severity": scenario.severity_level,
                "timeline": scenario.timeline,
                "expert_predictions": predictions
            })
        
        prompt = f"""
        Analyze these AI safety expert assessments:
        
        {json.dumps(scenario_data, indent=2)}
        
        Synthesize:
        1. Areas of expert consensus vs disagreement
        2. Most concerning scenarios based on expert assessment
        3. Common themes in expert reasoning
        4. Gaps in current risk assessment
        """
        
        schema = {
            "consensus_scenarios": [],
            "disagreement_areas": [],
            "highest_risk_scenarios": [],
            "common_concerns": [],
            "reasoning_patterns": {},
            "assessment_gaps": [],
            "research_priorities": []
        }
        
        db.close()
        return llm_config.get_structured_completion(prompt, schema)
    
    def identify_research_gaps(self) -> Dict:
        """Identify AI safety research gaps based on scenarios and expert input"""
        
        db = get_db_session()
        scenarios = db.query(AISafetyScenario).all()
        
        scenario_summaries = []
        for scenario in scenarios:
            scenario_summaries.append({
                "description": scenario.scenario_description,
                "category": scenario.risk_category,
                "severity": scenario.severity_level,
                "timeline": scenario.timeline
            })
        
        prompt = f"""
        Based on these AI safety scenarios, identify research gaps:
        
        {json.dumps(scenario_summaries, indent=2)}
        
        For each risk category (alignment, capabilities, deployment, governance):
        1. What research is most urgently needed?
        2. What current capabilities are insufficient?
        3. What would be the highest impact research directions?
        """
        
        schema = {
            "alignment_gaps": {
                "urgent_research": [],
                "capability_gaps": [],
                "high_impact_directions": []
            },
            "capabilities_gaps": {
                "urgent_research": [],
                "capability_gaps": [],
                "high_impact_directions": []
            },
            "deployment_gaps": {
                "urgent_research": [],
                "capability_gaps": [],
                "high_impact_directions": []
            },
            "governance_gaps": {
                "urgent_research": [],
                "capability_gaps": [],
                "high_impact_directions": []
            },
            "cross_cutting_priorities": [],
            "funding_recommendations": {}
        }
        
        db.close()
        return llm_config.get_structured_completion(prompt, schema)
    
    def analyze_risk_correlations(self) -> Dict:
        """Analyze how different AI safety risks might compound"""
        
        db = get_db_session()
        scenarios = db.query(AISafetyScenario).all()
        
        scenario_data = [{
            "id": s.id,
            "description": s.scenario_description,
            "category": s.risk_category,
            "severity": s.severity_level,
            "timeline": s.timeline
        } for s in scenarios]
        
        prompt = f"""
        Analyze potential correlations and compounding effects between these AI safety risks:
        
        {json.dumps(scenario_data, indent=2)}
        
        Identify:
        1. Which risks might trigger or amplify others?
        2. Common failure modes across categories
        3. Cascading risk scenarios
        4. Risk mitigation strategies that address multiple threats
        """
        
        schema = {
            "risk_correlations": [],
            "cascading_scenarios": [],
            "common_failure_modes": [],
            "multi_risk_mitigations": [],
            "risk_interaction_map": {},
            "priority_interventions": []
        }
        
        db.close()
        return llm_config.get_structured_completion(prompt, schema)

safety_analyzer = SafetyAnalyzer()