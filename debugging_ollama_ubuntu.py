# from langchain_community.llms import Ollama

# llm = Ollama(model="llama3.2:1b")
# try:
#     response = llm("Hello!")
#     print("LLM Response:", response)
# except Exception as e:
#     print("LLM Error:", e)

# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationChain
# from langchain.prompts import PromptTemplate
# from langchain_community.llms import Ollama

# memory = ConversationBufferMemory(ai_prefix="Assistant:")
# prompt = PromptTemplate(
#     input_variables=["history", "input"],
#     template="""
#     You are a helpful and friendly AI assistant. You are polite and respectful.
#     The conversation transcript is as follows:
#     {history}
#     And here is the user's follow-up: {input}
#     Your response:
#     """
# )
# chain = ConversationChain(
#     prompt=prompt,
#     memory=memory,
#     llm=Ollama(model="llama3.2:1b"),
#     verbose=True
# )

# response = chain.run(input="Hello, how are you?")
# print("Chain Response:", response)

# memory.save_context({"input": "Hi!"}, {"output": "Hello, how can I help you?"})
# print("Memory State:", memory.load_memory_variables({}))

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
    You are a helpful and friendly AI assistant. The conversation transcript is as follows:
    {history}
    User's follow-up: {input}
    Your response:
    """
)
test_prompt = prompt.format(history="User: Hi\nAssistant: Hello!", input="What can you do?")
print("Formatted Prompt:", test_prompt)



