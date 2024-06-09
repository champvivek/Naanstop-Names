from langchain.llms import GooglePalm
from langchain import PromptTemplate, LLMChain
from langchain.chains import SequentialChain
from secret_key import api_key

llm = GooglePalm(google_api_key = api_key, temperature = 0.6)
def generate_restaurant_name_and_items(cuisine):

    #Chain No. 1: Help to generate Restaurant Name

    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest me some name for this"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    ##Chain No. 2: Help to generate Menu Items

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}."
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )
    response = chain.invoke({"cuisine": cuisine})
    return (response)

    if __name__ == "__main__":
        print(generate_restaurant_name_and_items("Italian"))