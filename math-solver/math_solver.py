from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
load_dotenv()
# 2. Create a prompt template
math_prompt = PromptTemplate(
    input_variables=["problem"],
    template="""
You are a math teacher. Solve the following math word problem step by step and explain the answer clearly:

Problem:
{problem}

Answer:
"""
)

# 3. Load the language model and create the chain
llm = OpenAI(temperature=0.2)  # Low temperature = more accurate math
chain = LLMChain(llm=llm, prompt=math_prompt)

# 4. Main function to solve a math problem
def solve_math_problem(problem):
    solution = chain.run(problem)
    return solution

# 5. Run the code
if __name__ == "__main__":
    user_input = input("Enter a math word problem: ")
    print("\n🧠 Solving your problem...\n")
    result = solve_math_problem(user_input)
    print("--- Solution ---\n")
    print(result)
