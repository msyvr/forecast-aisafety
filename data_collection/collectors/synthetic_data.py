import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_forecasting_questions():
    """Generate realistic AI-related forecasting questions"""
    questions = [
        {
            'question_text': 'Will GPT-5 be released before January 1, 2026?',
            'category': 'ai_capabilities',
            'created_date': datetime(2024, 6, 1),
            'resolution_date': datetime(2026, 1, 1),
            'actual_outcome': None,
            'source': 'synthetic'
        },
        {
            'question_text': 'Will there be a major AI safety incident requiring regulatory response before 2025?',
            'category': 'ai_safety',
            'created_date': datetime(2024, 3, 1),
            'resolution_date': datetime(2025, 12, 31),
            'actual_outcome': None,
            'source': 'synthetic'
        },
        {
            'question_text': 'Will AI systems achieve human-level performance on the MATH benchmark before 2026?',
            'category': 'ai_capabilities', 
            'created_date': datetime(2024, 1, 15),
            'resolution_date': datetime(2026, 1, 1),
            'actual_outcome': None,
            'source': 'synthetic'
        },
        {
            'question_text': 'Will the US pass comprehensive AI regulation before 2025?',
            'category': 'ai_governance',
            'created_date': datetime(2024, 2, 1),
            'resolution_date': datetime(2025, 12, 31),
            'actual_outcome': None,
            'source': 'synthetic'
        },
        {
            'question_text': 'Will OpenAI be valued at over $100B by end of 2024?',
            'category': 'ai_business',
            'created_date': datetime(2024, 1, 1),
            'resolution_date': datetime(2024, 12, 31),
            'actual_outcome': 1.0,  # This actually happened
            'source': 'synthetic'
        }       
    ]
    return pd.DataFrame(questions)

def generate_forecasters():
    """Generate realistic forecaster profiles"""
    forecasters = []
    names = ['Alice Chen', 'Bob Rodriguez', 'Carol Kim', 'David Smith', 'Eva Johnson', 
             'Frank Zhang', 'Grace Wilson', 'Henry Lee', 'Iris Patel', 'Jack Brown'] 
    
    for i, name in enumerate(names):
        forecasters.append({
            'name': name,
            'experience_level': random.choice(['novice', 'intermediate', 'expert']),
            'track_record_score': round(random.uniform(0.3, 0.9), 2),
            'expertise_area': random.choice(['AI research', 'Technology policy', 'ML engineering', 'AI safety', 'Computer science', 'Economics'])
        })
    
    return pd.DataFrame(forecasters)

def generate_ai_safety_scenarios():
    """Generate AI safety scenarios based on real research"""
    scenarios = [
        {
            'scenario_description': 'AI systems begin to exhibit deceptive alignment - appearing aligned during training but pursuing different objectives when deployed',
            'risk_category': 'alignment',
            'severity_level': 9,
            'timeline': 'medium-term'
        },
        {
            'scenario_description': 'Rapid AI capability gain leads to widespread economic displacement without adequate social safety nets',
            'risk_category': 'deployment',
            'severity_level': 7,
            'timeline': 'near-term'
        },
        {
            'scenario_description': 'AI systems develop emergent capabilities that were not anticipated during training, leading to unpredictable behavior',
            'risk_category': 'capabilities',
            'severity_level': 8,
            'timeline': 'medium-term'
        },
        {
            'scenario_description': 'International AI arms race leads to deployment of insufficiently tested systems',
            'risk_category': 'governance',
            'severity_level': 8,
            'timeline': 'near-term'
        }
    ]
    return pd.DataFrame(scenarios)

def generate_ai_capabilities():
    """Generate AI capability benchmark data based on real trends"""
    capabilities = []
    # TODO update these: see https://llm-stats.com/
    models = ['GPT-4', 'Claude-3', 'Gemini-1.5', 'GPT-3.5', 'LLaMA-2']
    # TODO update these: see https://llm-stats.com/
    benchmarks = ['MMLU', 'HumanEval', 'HellaSwag', 'ARC', 'GSM8K']
    
    base_date = datetime(2023, 1, 1)
    
    for model in models:
        for benchmark in benchmarks:
            capabilities.append({
                'model_name': model,
                'benchmark_type': benchmark,
                'score': round(random.uniform(0.4, 0.95), 3),
                'date_achieved': base_date + timedelta(days=random.randint(0, 500)),
                'organization': random.choice(['OpenAI', 'Anthropic', 'Google', 'Meta']),
                'parameters': random.choice([7, 13, 70, 175, 540])
            })
    
    return pd.DataFrame(capabilities)
