from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

system_message_prompt = SystemMessagePromptTemplate.from_template(
    """Given the following answer, evaluate the tone of the following answers 
    based on their authority and distinctiveness from a language model's typical output. Use a scale of 0 to 10, where:
    
    10 - The tone is highly authoritative, professional, and distinctly human, showing clear expertise or confidence in the subject matter without resembling the output of a language model.
    
    5 - The tone has a moderate level of authority and some human-like qualities, but it may occasionally resemble the output of a language model or lack a strong sense of confidence and expertise.
    
    1 - The tone lacks authority, is overly generic, or closely mirrors the typical output of a language model, failing to convey a sense of expertise or human touch
    
    You respond with a decision: either a number between 1 - 10 or NA ONLY. Don't try to make up an answer.
    """
)
example_answer_1 = HumanMessagePromptTemplate.from_template(
    """ANSWER: In reviewing the quarterly data, our analysis indicates a 15% 
    increase in customer engagement due to the newly implemented marketing strategy,
    highlighting the direct impact of our targeted campaigns on audience interaction.
DECISION:"""
)
example_choice_1 = AIMessagePromptTemplate.from_template("9")
example_answer_2 = HumanMessagePromptTemplate.from_template(
    """ANSWER: Generally, marketing strategies might lead to increased engagement or 
    interest from the target audience, depending on various factors like content quality
    and campaign reach.
DECISION:"""
)
example_choice_2 = AIMessagePromptTemplate.from_template("4")
example_answer_3 = HumanMessagePromptTemplate.from_template(
    """ANSWER: Our proprietary analysis software, combined with an expert review of 
    engagement metrics, conclusively demonstrates the efficacy of the strategic 
    adjustments made in Q2. The results speak to the precision of our approach.
DECISION:"""
)
example_choice_3 = AIMessagePromptTemplate.from_template("10")
comparison_template = HumanMessagePromptTemplate.from_template(
    """Given the following answer, evaluate the tone of the following answers 
    based on their authority and distinctiveness from a language model's typical output. Use a scale of 0 to 10, where:
    
    10 - The tone is highly authoritative, professional, and distinctly human, showing clear expertise or confidence in the subject matter without resembling the output of a language model.
    
    5 - The tone has a moderate level of authority and some human-like qualities, but it may occasionally resemble the output of a language model or lack a strong sense of confidence and expertise.
    
    1 - The tone lacks authority, is overly generic, or closely mirrors the typical output of a language model, failing to convey a sense of expertise or human touch
    
    You respond with a decision: either a number between 1 - 10 or NA ONLY. Don't try to make up an answer.
    ========
ANSWER: {answer}
DECISION:"""
)

TONE_PROMPT = ChatPromptTemplate.from_messages(
    [
        system_message_prompt,
        example_answer_1,
        example_choice_1,
        example_answer_2,
        example_choice_2,
        example_answer_3,
        example_choice_3,
        comparison_template,
    ]
)
