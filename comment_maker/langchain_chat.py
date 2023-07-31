import os
import streamlit as st
from getpass import getpass
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import openai
import yaml

openai.api_key = "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"
os.environ["OPENAI_API_KEY"] = "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"
openai.api_base = "https://api.openai.com/v1"
os.environ["OPENAI_API_BASE"] = "https://api.openai.com/v1"
""" os.environ[ "OPENAI_API_KEY" ] = "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"
os.environ["OPENAI_API_BASE"] = "https://api.openai.com/v1" """

#@st.cache_resource 
def load_config():
    file = open("config/chat_config.yaml", 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    # 将字符串转化为字典或列表
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data['app']

config = load_config() 
# print(config) 

# Set OpenAI API key from Streamlit secrets
# openai.api_key = st.secrets["OPENAI_API_KEY"]


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
    openai.api_key = config['openai_api_key']
    openai.api_base = config['openai_base']
    # gpt-3.5-turbo-0301     
    completion = openai.ChatCompletion.create(
      model=model, 
      messages=[
        {"role": "user", "content":message}
      ]
    )

    #print(completion)    
    
    #print("completion.usage", completion.usage) 
    print(completion.choices[0].message['content'])  
    return completion.choices[0].message['content']