from typing import Optional

from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.chat_models.base import BaseChatModel

from metrics.evaluation_prompts.qa_prompt import (
    QA_CORRECTNESS_PROMPT,
)

from dotenv import load_dotenv

load_dotenv()


class AnswerAccuracy:
    """
    Determines if the LLM produced an accurate answer. 

    run Method:
    - Takes parameters: question, context, answer.
    - Returns score from 1-10 with 10 being completely accurate.
    """

    def __init__(self, llm: Optional[BaseChatModel] = None):
        if llm is None:
            llm = ChatOpenAI(temperature=0)
            # need to set OPENAI_API_KEY in env

        self.evaluator = LLMChain(llm=llm, prompt=QA_CORRECTNESS_PROMPT)

    def run(
        self, 
        question: str,
        context: str,
        answer: str,
    ):
       
        try:
            llmchoice = self.evaluator(
                {
                    "question": question,
                    "context": context,
                    "answer": answer,
                }
            )

            result = llmchoice["text"]
            return result
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
