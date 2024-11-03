import numpy as np
from transformers import pipeline
from app.core.config import settings
import torch
from typing import Dict, Any
import asyncio
from app.services.openai_service import OpenAIService

class MLPipeline:
    emotion_analyzer = None
    strategy_predictor = None
    openai_service = None
    
    @classmethod
    def initialize_models(cls):
        # Initialize existing models
        cls.emotion_analyzer = pipeline(
            "text-classification",
            model="SamLowe/roberta-base-go_emotions",
            top_k=3
        )
        
        cls.strategy_predictor = pipeline(
            "text-classification",
            model="bert-base-uncased",
            top_k=5
        )
        
        # Initialize OpenAI service
        cls.openai_service = OpenAIService()
    
    @classmethod
    async def process_realtime_data(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process real-time negotiation data using multiple ML models"""
        results = {}
        
        # Run analyses in parallel
        analyses = await asyncio.gather(
            cls._analyze_emotions(data),
            cls._predict_strategy(data),
            cls._analyze_cultural_context(data),
            cls._generate_counter_strategies(data)
        )
        
        results["emotion_analysis"] = analyses[0]
        results["strategy_prediction"] = analyses[1]
        results["cultural_context"] = analyses[2]
        results["counter_strategies"] = analyses[3]
        
        return results

    @classmethod
    async def _analyze_cultural_context(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze cultural context using OpenAI"""
        text = data.get("text", "")
        return await cls.openai_service.analyze_cultural_context(text)

    @classmethod
    async def _generate_counter_strategies(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate counter-strategies using OpenAI"""
        context = data.get("text", "")
        return await cls.openai_service.generate_negotiation_strategy(context)