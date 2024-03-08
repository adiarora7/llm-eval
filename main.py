from metrics.check_markdown import CheckMarkdown
from metrics.readability import Readability
from metrics.qa_correctness_evaluation import QAQualityCorrectness

# Text to check for Markdown patterns
text_to_check = "This is a Markdown heading"

# Using the static method contains_markdown directly
if CheckMarkdown.contains_markdown(text_to_check):
    print("The text contains Markdown patterns.")
else:
    print("The text does not contain Markdown patterns.")

# Text for which to calculate Flesch Reading Ease score
text_to_evaluate = "Hello. Indubitably a child should not be able to comprehend such language."

# Using the static method evaluate to calculate Flesch Reading Ease score
flesch_score = Readability.evaluate(text_to_evaluate)
print(f"The Flesch Reading Ease score for the text is: {flesch_score}")

