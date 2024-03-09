from evaluator import Evaluator

question = "Compounds that are capable of accepting electrons, such as o 2 or f2, are called what?"
context = """Oxidants and Reductants Compounds that are capable of accepting electrons, such as O 2 or F2, are called oxidants (or oxidizing agents) because they can oxidize other compounds. 
In the process of accepting electrons, an oxidant is reduced. Compounds that are capable of donating electrons, such as sodium metal or cyclohexane (C6H12), are called 
reductants (or reducing agents) because they can cause the reduction of another compound. In the process of donating electrons, a reductant is oxidized. These relationships are 
summarized in Equation 3.30."""
answer = "oxidants"

result = Evaluator.run_test(question, context, answer)

print(result)