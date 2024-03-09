from textstat import flesch_reading_ease

class Readability:
    """
    Flesch Reading Ease Score: the higher the score, the easier to read.
    Scores of 100-90 correlate to a 5th grade reading level, while scores <10 are
    classified as "Extremely difficult to read, and best understood by university
    graduates."

    https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
    https://pypi.org/project/textstat/ See full score ranges here.
    """

    @staticmethod
    def name() -> str:
        return "readability"

    @staticmethod
    def run(text: str) -> float:
        return flesch_reading_ease(text)