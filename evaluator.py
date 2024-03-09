from metrics.qa_correctness_evaluation import AnswerAccuracy
from metrics.readability import Readability
from metrics.check_markdown import CheckMarkdown
from metrics.tone_evaluation import EvaluateToneResponse

from exceptions.exceptions import MissingParameterError


class Evaluator:
    """
    Class to evaluate LLM-generated response based on 4 metrics
    - (Accuracy, Readability, Tone, Markdown).

    run_test Method:
    - Takes parameters: question, context, answer.
    - Returns a formatted response of the 4 evaluated metrics.

    """
    
    @staticmethod
    def run_test(question: str, context: str, answer: str):
        try:
            if question is None:
                raise MissingParameterError("Question is required for evaluating the accuracy of the answer. Please provide a question.")
            if context is None:
                raise MissingParameterError("Context is required for evaluating the accuracy of the answer in regards to the question asked. Please provide a dataframe column or a list of your context strings.")
            if answer is None:
                raise MissingParameterError("Answer is required for all evaluation metrics. Please provide an answer.")

            answer_accuracy = AnswerAccuracy()
            tone_evaluator = EvaluateToneResponse()

            accuracy = answer_accuracy.run(question, context, answer)
            readability = Readability.run(answer)
            markdown = CheckMarkdown.contains_markdown(answer)
            tone = tone_evaluator.run(answer)

            result = f'==================================\nAccuracy: {accuracy} \nReadability: {readability} \nMarkdown: {markdown} \nTone: {tone} \n================================== '

            return result
        except MissingParameterError as mpe:
            return f"Error: {mpe}"
        except Exception as e:
            return f"An error occurred during evaluation: {e}"
