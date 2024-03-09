import re

class CheckMarkdown:
    """
    Check if input contains any markdown.
    - Returns boolean.
    """
    def name() -> str:
        return "check markdown"

    @staticmethod
    def contains_markdown(text: str):
        pattern = r'(^\#+|\*|\*\*|`|```|_)'
        return re.search(pattern, text) is not None