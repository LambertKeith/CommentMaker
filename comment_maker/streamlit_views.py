import streamlit as st
import pandas as pd
import numpy as np
from comment_maker import streamlit_views_utils as UI_utils




def main():
    #记录测试用例
    if 'example' not in st.session_state:
        st.session_state.example = ''

    st.set_page_config(page_title="来评语")
    # 在侧边栏中创建一个下拉列表
    option = st.sidebar.selectbox(
        '请选择模式',
        ('主页', 'chat', 'excel')
    )
    

    # 根据选择的选项显示不同的页面
    if option == '主页':
        st.write('这是主页')

    #chat界面
    elif option == 'chat':

        container_chat = st.container()
        examples_or_describe = st.sidebar.radio(
            "便捷选项",
            ("关闭","使用本地案例","使用便捷描述"), horizontal=True)

        #案例区显示
        if examples_or_describe == "使用本地案例":
            
            #案例区
            examples_container = container_chat.container()
            examples_container.title("案例区")
            #col1为案例展示区，col2为创建案例区
            col1, col2 = examples_container.columns(2)
            #测试案例
            example_list = UI_utils.read_json_keys()
            genre = col1.radio(
                "请选择您的测试案例",
                example_list, horizontal=True)
            if genre =='非测试':
                pass
            else:
                st.session_state.example = genre
                print(st.session_state.example)
            #案例输入
            col2_1, col2_2 = col2.columns(2)
            with col2_1:
                example_name = col2.text_input("案例名称")
            with col2_2:
                example_body = col2.text_input("具体描述")
            #案例层按钮
            col2_3, col2_4 = col2.columns(2)
            if col2_3.button("添加案例"):
                col2.write(f"Input 1: {example_name}")
                col2.write(f"Input 2: {example_body}") 
            if col2_4.button("删除案例") :
                col2.write(st.session_state.example)

        if examples_or_describe == "使用便捷描述":      
            #描述选项区
            describe_item_container = container_chat.container()
            describe_item_container.title("便捷描述")

            #简单模式和复杂模式
            easy_or_not = describe_item_container.radio("请选择简单模式还是复杂模式", ('简单模式', '复杂模式'),horizontal=True)
            if easy_or_not == '简单模式':
                student_name = describe_item_container.text_input("学生姓名")
                comment_lenth = describe_item_container.radio('选择评语长度（50-200）', 
                                                            ('50', '100', '150','200'),
                                                            horizontal=True)
                number = describe_item_container.number_input('请为学生打分（1-5）', 
                                                        min_value=1, 
                                                        max_value=5, 
                                                        step=1, 
                                                        value=3)
            #复杂模式
            else:
                col_basic, col_describe = describe_item_container.columns(2)
                #基本信息
                #姓名
                student_name = col_basic.text_input("学生姓名")
                #长度
                comment_lenth = col_basic.radio('选择评语长度（50-200）', 
                                                            ('50', '100', '150','200'),
                                                            horizontal=True)
                #性别
                sex = col_basic.radio('性别', ('男', '女'), horizontal=True)
                #性格
                student_character = col_basic.text_input("性格")
                #年级
                grade = col_basic.radio('年级', ('一年级', '二年级', '三年级', '四年级', '五年级', '六年级'), horizontal=True)
                #详细信息
                
                describe1 = col_describe.checkbox('是否进步')
                describe2 = col_describe.checkbox('是否退步')
                describe3 = col_describe.checkbox('上课专心听讲')
                describe4 = col_describe.checkbox('上课开小差')
                describe5 = col_describe.checkbox('作业认真完成')
                describe6 = col_describe.checkbox('作业完成一般')
                describe7 = col_describe.checkbox('具有创造性思维')
                describe8 = col_describe.checkbox('顽皮')
                describe9 = col_describe.checkbox('乐于助人')



        #描述生成区
        describe_container = container_chat.container()
        describe_text = describe_container.text_area("生成的描述", '你好')
        describe2comment = describe_container.button('生成')

        #评语区
        code_table = container_chat.code("it's code")


    else:
        st.write('这是页面2')
        container_excel = st.container()
        container_excel.write("This is inside the container")

