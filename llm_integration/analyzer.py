from llm_integration.forecasting_analyzer import forecasting_analyzer
from llm_integration.safety_analyzer import safety_analyzer
from llm_integration.trajectory_analyzer import trajectory_analyzer
from typing import Dict, Any

class AnalysisCoordinator:
    """Main interface for all LLM analysis functions"""
    
    def __init__(self):
        self.forecasting = forecasting_analyzer
        self.safety = safety_analyzer
        self.trajectory = trajectory_analyzer
    
    def run_comprehensive_analysis(self) -> Dict[str, Any]:
        
        results = {
            "forecasting_insights": {},
            "safety_analysis": {},
            "trajectory_analysis": {},
            "cross_domain_insights": {}
        }
        
        try:
            # Forecasting analysis
            print("Running forecasting analysis...")
            results["forecasting_insights"] = {
                "general_patterns": self.forecasting.generate_forecasting_insights(),
                "ai_category_patterns": self.forecasting.generate_forecasting_insights("ai_capabilities")
            }
            
            # Safety analysis
            print("Running safety analysis...")
            results["safety_analysis"] = {
                "consensus_synthesis": self.safety.synthesize_safety_concerns(),
                "research_gaps": self.safety.identify_research_gaps(),
                "risk_correlations": self.safety.analyze_risk_correlations()
            }
            
            # Trajectory analysis
            print("Running trajectory analysis...")
            results["trajectory_analysis"] = {
                "capability_trends": self.trajectory.analyze_capability_trends(),
                "governance_insights": self.trajectory.generate_governance_insights(),
                "prediction_accuracy": self.trajectory.evaluate_prediction_accuracy()
            }
            
            # Cross-domain synthesis
            print("Generating cross-domain insights...")
            results["cross_domain_insights"] = self._generate_cross_domain_insights(results)
            
        except Exception as e:
            print(f"Analysis error: {e}")
            results["error"] = str(e)
        
        return results
    
    def _generate_cross_domain_insights(self, analysis_results: Dict) -> Dict:
        
        from llm_integration.config import llm_config
        
        summary = {
            "forecasting_key_findings": str(analysis_results.get("forecasting_insights", {}))[:500],
            "safety_key_findings": str(analysis_results.get("safety_analysis", {}))[:500],
            "trajectory_key_findings": str(analysis_results.get("trajectory_analysis", {}))[:500]
        }
        
        prompt = f"""
        Based on these analysis results across forecasting, AI safety, and AI trajectory:
        
        {summary}
        
        Generate cross-domain insights:
        1. How do AI capability trends inform safety research priorities?
        2. What do forecasting patterns tell us about AI governance needs?
        3. Where do expert safety concerns align or conflict with capability trajectories?
        4. What integrated research agenda emerges from this analysis?
        """
        
        schema = {
            "capability_safety_connections": [],
            "forecasting_governance_insights": [],
            "expert_trajectory_alignment": "",
            "integrated_research_agenda": [],
            "policy_implications": [],
            "research_coordination_opportunities": []
        }
        
        return llm_config.get_structured_completion(prompt, schema)
    
    def analyze_specific_question(self, question_id: int) -> Dict:
        return self.forecasting.analyze_prediction_patterns(question_id)
    
    def assess_rationale(self, rationale_text: str) -> Dict:
        return self.forecasting.assess_rationale_quality(rationale_text)

# Global analyzer instance
analyzer = AnalysisCoordinator()