import streamlit as st
import pandas as pd
import numpy as np
from comment_maker import streamlit_views_utils as UI_utils




def main():
    #记录测试用例
    if 'example' not in st.session_state:
        st.session_state.example = ''
    describe_info = ''

    st.set_page_config(page_title="来评语", layout='wide')
    # 在侧边栏中创建一个下拉列表
    option = st.sidebar.selectbox(
        '请选择模式',
        ('chat', 'excel')
    )
    
    #chat界面
    if option == 'chat':
        comment_lenth = 100

        container_chat = st.container()
        examples_or_describe = st.sidebar.radio(
            "便捷选项",
            ("案例", "学生评语生成工具"), horizontal=True, index=1)

        #案例区显示
        if examples_or_describe == "案例":
            
            #案例区
            examples_container = container_chat.container()
            examples_container.title("案例区")
            examples_container.write("您可以选择以下的示例生成评语")
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
                #读取json
                describe_info = UI_utils.get_value_from_json_file(genre)
                #describe_info = 
                
            #案例输入
            st.sidebar.write("添加自定义案例，输入名称和若干词语组成的描述")
            col2_1, col2_2 = st.sidebar.columns(2)
            with col2_1:
                example_name = st.sidebar.text_input("案例名称")
            with col2_2:
                example_body = st.sidebar.text_input("具体描述")
            #案例层按钮
            col2_3, col2_4 = st.sidebar.columns(2)
            if col2_3.button("添加案例"):
                if example_name not in example_list:
                    UI_utils.add_data_to_json_file(example_name, example_name+','+example_body)
                else:
                    st.warning("无法添加重名案例，若想修改，可以先删除")
                example_list = UI_utils.read_json_keys()
            if col2_4.button("删除案例") :
                if genre != '非测试':
                    UI_utils.remove_data_from_json_file(genre)
                else:
                    st.warning("无法删除默认选项")
                example_list = UI_utils.read_json_keys()

        if examples_or_describe == "学生评语生成工具":      
            #描述选项区
            describe_item_container = container_chat.container()
            describe_item_container.title("学生评语生成工具")

            #简单模式和复杂模式
            describe_item_container.title('简单&复杂',)
            easy_or_not = describe_item_container.radio("请选择简单模式还是复杂模式", ('简单模式', '复杂模式'),horizontal=True)
            #describe_item_container.title('评语调色盘')
            describe_item_container.write("为您的评语添加个性化内容")
            if easy_or_not == '简单模式':
                #姓名
                student_name = describe_item_container.text_input("学生姓名")
                if student_name != '': describe_info += f"学生姓名：{student_name}"
                #性别
                sex = describe_item_container.radio('性别', ('男', '女'), horizontal=True)
                if sex :describe_info += f"，性别：{sex}"
                #评语长度
                comment_lenth = describe_item_container.radio('选择评语长度（50-200）', 
                                                            ('50', '100', '150','200'),
                                                            horizontal=True, index=1)
                #打分
                number = describe_item_container.radio('请为学生打分（1-5）',  
                                                            (1, 2, 3, 4, 5),
                                                            horizontal=True, index=2)
                if number == 1:
                    describe_info += ",最近表现不太好"
                elif number == 2:
                    describe_info += ",最近表现一般"
                elif number == 3:
                    describe_info += ",最近表现中规中矩"
                elif number == 4:
                    describe_info += ",最近表现比较好"
                elif number == 5:
                    describe_info += ",最近表现非常好"
            #复杂模式
            else:
                col_basic, col_describe = describe_item_container.columns(2)
                #基本信息
                #姓名
                student_name = col_basic.text_input("学生姓名")
                if student_name != '' and UI_utils.is_valid_student_name(student_name): describe_info += f"学生姓名：{student_name}"
                #长度
                comment_lenth = col_basic.radio('选择评语长度（50-200）', 
                                                            ('50', '100', '150','200'),
                                                            horizontal=True, index=1)
                #性别
                sex = col_basic.radio('性别', ('男', '女'), horizontal=True)
                if sex :describe_info += f"，性别：{sex}"
                #性格
                #性格列表
                personality_traits = [
                    "好奇心旺盛",
                    "热情活泼",
                    "快乐友善",
                    "独立自主",
                    "乐于助人",
                    "坚持努力",
                    "喜欢学习",
                    "善于合作",
                    "有创造力",
                    "喜欢表达",
                    "有耐心",
                    "喜欢挑战",
                    "坦率直言",
                    "爱幻想",
                    "坚持正义"
                ]
                student_character = col_basic.multiselect("性格", personality_traits)
                if student_character != '':describe_info += f"，性格：{student_character}"

                #年级
                grade = col_basic.radio('年级', ('一年级', '二年级', '三年级', '四年级', '五年级', '六年级'), 
                                        horizontal=True)
                describe_info += f'，年级：{grade}'
                #详细信息
                describe1 = col_describe.checkbox('是否进步')
                if describe1 : describe_info += '，有所进步'
                describe2 = col_describe.checkbox('是否退步')
                if describe2 : describe_info += '，有所退步'
                describe3 = col_describe.checkbox('上课专心听讲')
                if describe3 : describe_info += '，上课专心听讲'
                describe4 = col_describe.checkbox('上课开小差')
                if describe4 : describe_info += '，上课开小差'
                describe5 = col_describe.checkbox('作业认真完成')
                if describe5 : describe_info += '，作业认真完成'
                describe6 = col_describe.checkbox('作业完成一般')
                if describe6 : describe_info += '，作业完成一般'
                describe7 = col_describe.checkbox('具有创造性思维')
                if describe7 : describe_info += '，具有创造性思维'
                describe8 = col_describe.checkbox('顽皮')
                if describe8 : describe_info += '，有点顽皮'
                describe9 = col_describe.checkbox('乐于助人')
                if describe9 : describe_info += '，乐于助人'

        #描述生成区
        describe_container = container_chat.container()
        describe_container.title('评语区')
        describe_text = describe_container.text_area("学生最近表现", describe_info)
        describe2comment = describe_container.button('生成')
        text = ''
        if describe2comment:
            text=UI_utils.make_comment(describe_text, comment_lenth)
        #评语区
        if text == '':
            code_table = container_chat.markdown("it's code")
        else:
            code_table = container_chat.markdown(text) 


    else:
        st.write('这是页面2')
        container_excel = st.container()
        container_excel.write("This is inside the container")

