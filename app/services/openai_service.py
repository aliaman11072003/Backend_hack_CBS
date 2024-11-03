from openai import OpenAI
from app.core.config import settings
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        
    async def generate_negotiation_strategy(self, context: str) -> Dict[str, Any]:
        """Generate negotiation strategies using GPT-4"""
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert negotiation strategist."},
                    {"role": "user", "content": f"Analyze this negotiation context and provide strategic advice: {context}"}
                ]
            )
            return {
                "strategy": completion.choices[0].message.content,
                "success": True
            }
        except Exception as e:
            logger.error(f"OpenAI API error: {str(e)}")
            return {
                "strategy": "Failed to generate strategy",
                "success": False,
                "error": str(e)
            }
    
    async def analyze_cultural_context(self, text: str) -> Dict[str, Any]:
        """Analyze cultural context and sensitivities"""
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert in cross-cultural communication."},
                    {"role": "user", "content": f"Analyze this text for cultural context and sensitivities: {text}"}
                ]
            )
            return {
                "analysis": completion.choices[0].message.content,
                "success": True
            }
        except Exception as e:
            logger.error(f"OpenAI API error: {str(e)}")
            return {
                "analysis": "Failed to analyze cultural context",
                "success": False,
                "error": str(e)
            } 