import openai
from comment_maker import streamlit_views_utils, langchain_chat

""" openai.api_key = "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"
openai.api_base = "https://api.openai.com/v1" """
def test():
    #data = streamlit_views_utils.read_json_keys()
    #print(data)
    langchain_chat.base_chat("什么是台风")


if __name__ == "__main__":
    test()