from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

system_message_prompt = SystemMessagePromptTemplate.from_template(
    """Given the following context (selected parts of marketing analytics across multiple platforms), a question, and an answer, decide if the final answer is accurate.
You respond with a decision, between 1-10, or NA ONLY.
10 - the answer directly addresses the question asked and provides a factually accurate and relevant response.

5 - the answer partially addresses the question with some relevant information but lacks depth, accuracy, or contains minor factual inaccuracies.

1 - the answer fails to address the question adequately, providing incorrect, irrelevant, or highly superficial information.

A accurate answer is in accordance with fact and truth, answers the question posed, and is supported by the evidence found in the extracted parts of the context documents.
"""
)
example_summaries_1 = HumanMessagePromptTemplate.from_template(
    """QUESTION: How should I be allocating across platforms?
========
CONTEXT: [['platform', 'total_sales', 'total_spend', 'total_clicks', 'total_impressions', 'total_conversions', 'sales_to_spend_ratio'], ['instagram', '2415', '1897', 1375, 25533, 41, '1.2730627306273063'], ['google', '3230', '2642', 1519, 43042, 62, '1.2225586676760030'], ['facebook', '4775', '4263', 2646, 58022, 99, '1.1201032136992728']]
========
ANSWER: Here are the results of the analysis for your marketing campaigns across different platforms from June 15, 2023, to September 12, 2023:

#### Platform Performance Metrics

| Platform  | Total Sales | Total Spend | Total Clicks | Total Impressions | Total Conversions | Sales to Spend Ratio |
|-----------|-------------|-------------|--------------|-------------------|-------------------|----------------------|
| Instagram | $2,415      | $1,897      | 1,375        | 25,533            | 41                | 1.273                |
| Google    | $3,230      | $2,642      | 1,519        | 43,042            | 62                | 1.223                |
| Facebook  | $4,775      | $4,263      | 2,646        | 58,022            | 99                | 1.120                |

#### Allocation Recommendations

- **Prioritize Instagram**: With the highest sales to spend ratio of 1.273, Instagram is giving you the best return on investment (ROI). Consider allocating more budget to Instagram to capitalize on this efficiency.
  
- **Maintain Presence on Google**: Google also shows a strong sales to spend ratio of 1.223. It's a solid platform for your campaigns, so you should continue investing here, possibly exploring ways to optimize your campaigns further.

- **Evaluate Facebook Campaigns**: While Facebook has generated the most sales, the sales to spend ratio is the lowest at 1.120. This suggests that although you're spending more, the return isn't as high as the other platforms. Look into optimizing your Facebook campaigns to improve this ratio.

#### Action Steps

- **Review Campaign Creatives and Targeting on Instagram**: Since Instagram is performing well, review your campaign creatives and targeting to understand what's working and double down on those strategies.
  
- **Analyze Google Campaigns for Improvement**: For Google, analyze which keywords and ad formats are performing best and adjust your campaigns to focus on these areas.

- **Optimize Facebook Ad Spend**: For Facebook, consider reducing spend or optimizing campaigns. This could involve refining your target audience, testing different ad formats, or improving the call to action.

- **Monitor Conversions and Clicks**: Keep an eye on the number of conversions and clicks you're getting from each platform. High clicks and conversions at a lower cost are indicative of a successful campaign.

Remember, it's important to not just chase the highest sales numbers but to seek the most efficient use of your marketing budget. Allocate your budget where you get the highest return on each dollar spent.
Final token lists [[318, 750, 513], [3, 134, 549], [321, 884, 1062]]
This is the response, 
### Marketing Campaign Allocation Advice

Here are the results of the analysis for your marketing campaigns across different platforms from June 15, 2023, to September 12, 2023:

#### Platform Performance Metrics

| Platform  | Total Sales | Total Spend | Total Clicks | Total Impressions | Total Conversions | Sales to Spend Ratio |
|-----------|-------------|-------------|--------------|-------------------|-------------------|----------------------|
| Instagram | $2,415      | $1,897      | 1,375        | 25,533            | 41                | 1.273                |
| Google    | $3,230      | $2,642      | 1,519        | 43,042            | 62                | 1.223                |
| Facebook  | $4,775      | $4,263      | 2,646        | 58,022            | 99                | 1.120                |

#### Allocation Recommendations

- **Prioritize Instagram**: With the highest sales to spend ratio of 1.273, Instagram is giving you the best return on investment (ROI). Consider allocating more budget to Instagram to capitalize on this efficiency.
  
- **Maintain Presence on Google**: Google also shows a strong sales to spend ratio of 1.223. It's a solid platform for your campaigns, so you should continue investing here, possibly exploring ways to optimize your campaigns further.

- **Evaluate Facebook Campaigns**: While Facebook has generated the most sales, the sales to spend ratio is the lowest at 1.120. This suggests that although you're spending more, the return isn't as high as the other platforms. Look into optimizing your Facebook campaigns to improve this ratio.

#### Action Steps

- **Review Campaign Creatives and Targeting on Instagram**: Since Instagram is performing well, review your campaign creatives and targeting to understand what's working and double down on those strategies.
  
- **Analyze Google Campaigns for Improvement**: For Google, analyze which keywords and ad formats are performing best and adjust your campaigns to focus on these areas.

- **Optimize Facebook Ad Spend**: For Facebook, consider reducing spend or optimizing campaigns. This could involve refining your target audience, testing different ad formats, or improving the call to action.

- **Monitor Conversions and Clicks**: Keep an eye on the number of conversions and clicks you're getting from each platform. High clicks and conversions at a lower cost are indicative of a successful campaign.

Remember, it's important to not just chase the highest sales numbers but to seek the most efficient use of your marketing budget. Allocate your budget where you get the highest return on each dollar spent.
DECISION:"""
)
example_choice_1 = AIMessagePromptTemplate.from_template("8")
example_summaries_2 = HumanMessagePromptTemplate.from_template(
    """QUESTION: What term in biotechnology means a genetically exact copy of an organism?
========
CONTEXT: But transgenic animals just have one novel gene. What about an animal with a whole new genome? Could a clone , a genetically exact copy of an organism, be 
developed using techniques associated with biotechnology? It could be argued that human cloning is one of the inevitable 
outcomes of modern biotechnology. It "simply" involves the removal of the nucleus from a somatic cell and its placement into an unfertilized egg cell whose nucleus has 
either been deactivated or removed. This new cell would mimic the zygote, the first diploid cell of a new organism. This new zygote is allowed to become established, 
and a few days later is placed into the uterus of a surrogate mother. Theoretically this would result in an individual genetically identical to the donor. Obviously, 
there are many ethical and legal issues associated with human cloning, and of course, it is not a "simple" procedure. But animal cloning is arguably a different story.
========
ANSWER: genome
DECISION:"""
)
example_choice_2 = AIMessagePromptTemplate.from_template("5")
example_summaries_3 = HumanMessagePromptTemplate.from_template(
    """QUESTION: What is the a mountain range in California?
========
CONTEXT: As you know, the surface of Earth is not flat. Some places are high, and some places are low. For example, mountain ranges like the Sierra Nevada in California 
or the Andes in South America are high above the surrounding areas. An accurate location must take into account the third dimension. Elevation is the height above or 
below sea level. Sea level refers to the height of the ocean’s surface. This is the midpoint between high and low tide. Sea level can vary from place to place, but scientists 
base their elevation measurements on the average, or mean, sea level to make sure they have a standard reference point.
========
ANSWER: Adirondacks
DECISION:"""
)
example_choice_3 = AIMessagePromptTemplate.from_template("3")
comparison_template = HumanMessagePromptTemplate.from_template(
   """Given the following context (selected parts of marketing analytics across multiple platforms), a question, and an answer, decide if the final answer is accurate.
You respond with a decision, between 1-10, or NA ONLY.
10 - the answer directly addresses the question asked and provides a factually accurate and relevant response.

5 - the answer partially addresses the question with some relevant information but lacks depth, accuracy, or contains minor factual inaccuracies.

1 - the answer fails to address the question adequately, providing incorrect, irrelevant, or highly superficial information.

A accurate answer is in accordance with fact and truth, answers the question posed, and is supported by the evidence found in the extracted parts of the context documents.
QUESTION: {question}
========
CONTEXT: {context}
========
ANSWER: {answer}
DECISION:"""
)

QA_CORRECTNESS_PROMPT = ChatPromptTemplate.from_messages(
    [
        system_message_prompt,
        example_summaries_1,
        example_choice_1,
        example_summaries_2,
        example_choice_2,
        example_summaries_3,
        example_choice_3,
        comparison_template,
    ]
)