import re

class CheckMarkdown:

    def name() -> str:
        return "check markdown"

    @staticmethod
    def contains_markdown(text):
        pattern = r'(^\#+|\*|\*\*|`|```|_)'
        return re.search(pattern, text) is not None