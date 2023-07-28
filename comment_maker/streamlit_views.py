import streamlit as st
import pandas as pd
import numpy as np




def main():

    st.set_page_config(page_title="来评语")
    # 在侧边栏中创建一个下拉列表
    option = st.sidebar.selectbox(
        '请选择一个页面',
        ('主页', 'chat', 'excel')
    )

    # 根据选择的选项显示不同的页面
    if option == '主页':
        st.write('这是主页')

    #chat界面
    elif option == 'chat':
        st.write('这是页面1')
        container_chat = st.container()

        #案例区
        examples_container = container_chat.container()
        examples_container.write("examples_container")


        #描述选项区
        describe_item_container = container_chat.container()
        describe_item_container.write("describe_item_container")
        #描述生成区
        describe_container = container_chat.container()
        describe_container.write("describe_container")
        #评语区
        code_table = container_chat.code("it's code")


    else:
        st.write('这是页面2')
        container_excel = st.container()
        container_excel.write("This is inside the container")

