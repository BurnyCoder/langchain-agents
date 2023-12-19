from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType



from dotenv import load_dotenv

# Load OpenAI Api key
load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)

    primpt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have {animal_type} and I want cool name for it. It is {pet_color} in color. Suggest me five names for my pet."
    )

    name_chain = LLMChain(llm=llm, prompt=primpt_template_name, output_key ="pet_name")

    responce = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

    return responce

def langchain_agent(input):
    llm = OpenAI(temperature=0.8)
    
    tools = load_tools(["wikipedia", "llm-math"], llm = llm)

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    result = agent.run(input)

if __name__ == "__main__": 
    print(generate_pet_name("pony", 'rainbow'))
    print(langchain_agent("What is the avarage age of a dog? Multiply the age by 3."))
     
