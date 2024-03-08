from typing import List, Optional, Dict, Any, Union, Tuple

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.chat_models.base import BaseChatModel

from evaluation_prompts.qa_prompt import QA_CORRECTNESS_PROMPT


class QAQualityCorrectness:
    """
    Given an input question, context string, and model generation, determine if the
    generation produced a correct answer.
    """

    def __init__(self, llm: Optional[BaseChatModel] = None):
        if llm is None:
            llm = ChatOpenAI(temperature=0)
        
        self.evaluator = LLMChain(llm=llm, prompt=QA_CORRECTNESS_PROMPT)


    @staticmethod
    def run_batch(
        self,
        question: List[str],
        context: Optional[str] = None,
        answer: Optional[str] = None,
    ):
        """
        """

        llmchoice = self.evaluator(
            {
                "question": question,
                "context": context,
                "answer": answer,
            }
        )

        result = llmchoice["text"]
        return result
