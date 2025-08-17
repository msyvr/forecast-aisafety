from dotenv import load_dotenv

import os
import openai
from typing import Dict, Any, List
import json

load_dotenv()

class LLMConfig:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        # Costs: https://platform.openai.com/docs/pricing, https://yourgpt.ai/tools/openai-and-other-llm-api-pricing-calculator
        # Context:
        # gpt-5-mini: 400k
        # gpt-4.1-nano: 1M context
        # gpt-4o-mini: multimodal (voice, image, video); 128k context
        self.default_model = 'gpt-5-mini'
        self.max_tokens = 1000
        self.temperature = 0.1

    def get_completion(self, prompt: str, model: str = None) -> str:
        try:
            response = self.openai_client.chat.completions.create(
                model=model or self.default_model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f'LLM API Error: {e}')
            return f'Error: {str(e)}'
        
    def get_structured_completion(self, prompt: str, schema: Dict) -> Dict:
        structured_prompt = f"""
        {prompt}

        Respond with valid JSON matching this schema:
        {json.dumps(schema, indent=2)}
        """

        response = self.get_completion(structured_prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Attempt to explicitly extract JSON
            import re
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            return {"error": "Could not parse JSON response"}
        
llm_config = LLMConfig()
