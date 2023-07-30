import os
from getpass import getpass
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import openai

openai.api_key = "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"
openai.api_base = "https://api.openai.com/v1"
""" os.environ[ "OPENAI_API_KEY" ] = "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"
os.environ["OPENAI_API_BASE"] = "https://api.openai.com/v1" """

def llm(question):
    
    
    template = """Question: {question}
    Answer: Let's think step by step."""
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = OpenAI()
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    #question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
    result = llm_chain.run(question)
    print(result)

def llm_chat(text):
    # 初始化包装器，temperature越高结果越随机
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

    prompt = "请你扮演一个幽默的AI助理，用诙谐有趣的语气回复我的问题或者请求，内容如下<<<{}>>>".format(text)

    return llm(text)    

def base_chat(message,model="gpt-3.5-turbo-0301"):
    # gpt-3.5-turbo-0301     
    completion = openai.ChatCompletion.create(
      model=model, 
      messages=[
        {"role": "user", "content":message}
      ]
    )

    print(completion)    
    
    #print("completion.usage", completion.usage) 
    
    return completion.choices[0].message['content']