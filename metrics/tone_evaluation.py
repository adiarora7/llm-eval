from evaluation_prompts.tone_prompt import TONE_PROMPT

class EvaluateToneResponse:
    def __init__(self, answer):
       
        self.answer = answer

    def evaluate_response(self):
        full_prompt = TONE_PROMPT 
				