import openai
from comment_maker import streamlit_views_utils, langchain_chat

""" openai.api_key = "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"
openai.api_base = "https://api.openai.com/v1" """
def test():
    #data = streamlit_views_utils.read_json_keys()
    #print(data)
    langchain_chat.base_chat("什么是台风")

def test1():
    print(streamlit_views_utils.select_random_values([1,2,3,4,5,6,7,8,9,0,435,7568,23,235]))
if __name__ == "__main__":
    test1()