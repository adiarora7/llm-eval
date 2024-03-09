from typing import Optional

from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.chat_models.base import BaseChatModel

from metrics.evaluation_prompts.tone_prompt import TONE_PROMPT


from dotenv import load_dotenv

load_dotenv()


class EvaluateToneResponse:    
    """
    Given a model generation, determines the tone of the answer.

    run Method:
    - Takes parameters: answer.
    - Returns score from 1-10 with 10 corresponding to a tone which is highly authoritative, professional, and distinctly human...
    """

    def __init__(self, llm: Optional[BaseChatModel] = None):
        if llm is None:
            llm = ChatOpenAI(temperature=0)
            # need to set OPENAI_API_KEY in env
        self.evaluator = LLMChain(llm=llm, prompt=TONE_PROMPT)

    def run(self, answer: str):
        try:
            llmchoice = self.evaluator({"answer": answer})
            result = llmchoice["text"]
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
				