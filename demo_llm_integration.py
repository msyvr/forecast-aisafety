"""
Demo script to test LLM analysis code
"""

from llm_integration.analyzer import analyzer
import json
from datetime import datetime

def run_analysis_demo():
    
    print("AI Safety Forecasting: LLM analysis demo")
    print(f"Started at: {datetime.now()}\n")
    
    # Test individual components
    print("1. Testing rationale assessment...")
    test_rationale = """
    Based on current AI development trends and the trade policies relevant to AI governance, 
    I believe China will remain about six months behind the best models from OpenAI, Google,
    and Anthropic by mid-2026. Chip export controls and lack of government support have left 
    China under-resourced compared to the West. Smuggling banned Taiwanese chips, buying 
    older chips, and producing domestic chips leaves China about three years behind the 
    U.S.-Taiwanese chip frontier. Since China will manage to maintain only about one-tenth of 
    AI-relevant compute globally, the compute deficit limits what they can achieve without 
    government support.
    """
    
    rationale_analysis = analyzer.assess_rationale(test_rationale)
    print(f"Rationale Quality Assessment:")
    print(json.dumps(rationale_analysis, indent=2))
    print()
    
    print("2. Testing safety concern synthesis...")
    safety_synthesis = analyzer.safety.synthesize_safety_concerns("alignment")
    print(f"Safety Concerns (Alignment):")
    print(json.dumps(safety_synthesis, indent=2))
    print()
    
    print("3. Testing capability trend analysis...")
    capability_trends = analyzer.trajectory.analyze_capability_trends()
    print(f"Capability Trends:")
    print(json.dumps(capability_trends, indent=2))
    print()
    
    print("4. Running comprehensive analysis...")
    comprehensive_results = analyzer.run_comprehensive_analysis()
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"analysis_results_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(comprehensive_results, f, indent=2, default=str)
    
    print(f"Analysis saved to: {filename}\n")
    
    print("Demo complete. The following results were saved to file:\n")
    return comprehensive_results

if __name__ == "__main__":
    results = run_analysis_demo()