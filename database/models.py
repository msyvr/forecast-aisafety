from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime, timezone

Base = declarative_base()

# Core forecasting tables
class ForecastingQuestion(Base):
    __tablename__ = 'forecasting_questions'

    id = Column(Integer, primary_key=True)
    question_text = Column(Text, nullable=False)
    category = Column(String(100))
    created_date = Column(DateTime, default=datetime.now(timezone.utc))
    resolution_date = Column(DateTime)
    actual_outcome = Column(Float)
    # Sources might be: labs, experts, metaculus, synthetic, etc.
    source = Column(String(255))

    predictions = relationship("Prediction", back_populates="question")

class Forecaster(Base):
    __tablename__ = 'forecasters'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    # Standardize as: novice, intermediate, expert, unknown.
    experience_level = Column(String(50))
    track_record_score = Column(Float)
    # TODO swap 'area' for 'domain' throughout.
    expertise_area = Column(String(200))

    predictions = relationship("Prediction", back_populates="forecaster")
    expert_predictions = relationship("ExpertPrediction", back_populates="expert")

class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('forecasting_questions.id'))
    forecaster_id = Column(Integer, ForeignKey('forecasters.id'))
    prediction_value = Column(Float)
    confidence = Column(Float)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
    rationale_text = Column(Text)

    question = relationship("ForecastingQuestion", back_populates="predictions")
    forecaster = relationship("Forecaster", back_populates="predictions")

class AISafetyScenario(Base):
    __tablename__ = 'ai_safety_scenarios'

    id = Column(Integer, primary_key=True)
    scenario_description = Column(Text, nullable=False)
    # Categories: alignment, capabilities, governance
    risk_category = Column(String(100))
    # Scale 1-10
    severity_level = Column(Integer)
    # Horizon: near-term, medium-term, long-term
    timeline = Column(String(100))

    expert_predictions = relationship("ExpertPrediction", back_populates="scenario")

class ExpertPrediction(Base):
    __tablename__ = 'expert_predictions'

    id = Column(Integer, primary_key=True)
    scenario_id = Column(Integer, ForeignKey('ai_safety_scenarios.id'))
    expert_id = Column(Integer, ForeignKey('forecasters.id'))
    p_doom = Column(Float)
    confidence = Column(Float)
    reasoning = Column(Text)
    # TODO swap 'area' for 'domain' throughout.
    expertise_area = Column(String(200))
    prediction_date = Column(DateTime, default=datetime.now(timezone.utc))

    scenario = relationship("AISafetyScenario", back_populates="expert_predictions")
    expert = relationship("Forecaster", back_populates="expert_predictions")

class AICapabilityMetric(Base):
    __tablename__ = 'ai_capabilities_metrics'

    id = Column(Integer, primary_key=True)
    model_name = Column(String(200))
    # Current benchmarks: MMLU, HumanEval, HellaSwag, etc ???
    # TODO Update the above list and consider how to identify relevant new benchmarks.
    benchmark_type = Column(String(100))
    score = Column(Float)
    date_achieved = Column(DateTime)
    organization = Column(String(200))
    # Number of parameters in billions
    # TODO swap 'parameters_B' for 'parameters' throughout.
    parameters = Column(Float)
    # TODO consider normalization as SoTA evolves
    training_compute_flops = Column(Float)

class ResearchTrajectoryData(Base):
    __tablename__ = 'research_trajectory_data'

    id = Column(Integer, primary_key=True)
    # Standardize domains: language models, robotics, computer vision
    # TODO swap 'area' for 'domain' throughout.
    capability_area = Column(String(200))
    # Progress rate units: % per annum.
    # TODO swap 'rate' for 'pct_pa'.
    progress_rate = Column(Float)
    # TODO units - start with millions but should this be total or pa?
    funding_levels = Column(Float)
    researcher_count = Column(Integer)
    measurement_date = Column(DateTime, default=datetime.now(timezone.utc))

class SafetyResearchGap(Base):
    __tablename__ = 'safety_research_gaps'

    id = Column(Integer, primary_key=True)
    # TODO swap 'area' for 'domain' throughout.
    research_area = Column(String(200))
    current_capability = Column(Text)
    required_capability = Column(Text)
    # Scale 1-10.
    urgency_score = Column(Integer)
    # TODO Estimation algorithm.
    funding_needed = Column(Float)

