import streamlit as st
import pandas as pd
import numpy as np
from comment_maker import streamlit_views_utils as UI_utils




def main():
    #记录测试用例
    if 'example' not in st.session_state:
        st.session_state.example = ''
    
    #描述信息和生成的评价
    describe_info = ''
    text = ''
    st.set_page_config(page_title="来评语", layout='wide')
    # 在侧边栏中创建一个下拉列表
    st.sidebar.title("学生评语生成工具")
    option = st.sidebar.selectbox(
        '请选择模式',
        (['chat'])
    )
    
    #chat界面
    if option == 'chat':
        comment_lenth = 100

        container_chat = st.container()
        examples_or_describe = st.sidebar.radio(
            "便捷选项",
            ("模板生成", "学生评语生成工具"), horizontal=True, index=1)

        #案例区显示
        student_name = ''
        if examples_or_describe == "模板生成":
            
            #案例区
            examples_container = container_chat.container()
            examples_container.title("模板区")
            examples_container.write("您可以选择以下的模板生成评语")
            #col1为案例展示区，col2为创建案例区
            col1, col2 = examples_container.columns(2)
            #测试案例
            example_list = UI_utils.read_json_keys()
            genre = col1.radio(
                "模板列表",
                example_list, horizontal=True)
            if genre =='请选择----->':
                pass
            else:
                #读取json
                describe_info = UI_utils.get_value_from_json_file(genre)
                text=UI_utils.make_comment(describe_info, comment_lenth)
                #describe_info = 
                
            #案例输入
            st.sidebar.write("添加自定义模板，输入名称和若干词语组成的描述")
            col2_1, col2_2 = st.sidebar.columns(2)
            with col2_1:
                example_name = st.sidebar.text_input("模板名称")
            with col2_2:
                example_body = st.sidebar.text_input("具体描述")
            #案例层按钮
            col2_3, col2_4 = st.sidebar.columns(2)
            if col2_3.button("添加模板"):
                if example_name not in example_list:
                    if example_name != '':
                        if example_body != '':
                            UI_utils.add_data_to_json_file(example_name, example_name+','+example_body)
                        else:
                            st.warning("请输入描述")
                    else:
                        st.warning("请输入模板名称")
                else:
                    st.warning("无法重名，若想修改，可以先删除")
                example_list = UI_utils.read_json_keys()
            if col1.button("删除模板") :
                if genre != '请选择----->':
                    UI_utils.remove_data_from_json_file(genre)
                else:
                    st.warning("无法删除默认选项")
                example_list = UI_utils.read_json_keys()

        if examples_or_describe == "学生评语生成工具":      
            #描述选项区
            describe_item_container = container_chat.container()
            

            #简单模式和复杂模式
            describe_item_container.title('生成评语',)
            describe_item_container.info('生成评语，两步到位')
            describe_item_container.header('1.选择简单或者复杂模式')
            easy_or_not = describe_item_container.radio("请选择", ('简略模式', '标准模式'),horizontal=True)
            #describe_item_container.title('评语调色盘')
            st.info("")
            describe_item_container.header("2.为您的评语添加个性化内容")
            if easy_or_not == '简略模式':
                describe_item_container.write('输入基本信息并给你的学生打个分')
                #姓名
                real_student_name = ''
                student_name = describe_item_container.text_input("学生姓名")
                if student_name != '' and UI_utils.is_valid_student_name(student_name): 
                    #describe_info += f"学生姓名：{student_name}"
                    real_student_name = student_name
                
                describe_info += f"学生姓名：{real_student_name}"
                sex = describe_item_container.radio('性别', ('男', '女'), horizontal=True)
                if sex :describe_info += f"\n性别：{sex}"
                #评语长度
                comment_lenth = describe_item_container.radio('选择评语长度（50-200）', 
                                                            ('50', '100', '150','200'),
                                                            horizontal=True, index=1)
                #打分
                number = describe_item_container.radio('请为学生打分（1-5）',  
                                                            (1, 2, 3, 4, 5),
                                                            horizontal=True, index=2)
                describe_info += UI_utils.choose_discribe_from_json(f'{number}')

            #复杂模式
            else:

                #基本信息
                #姓名
                real_student_name = ''
                student_name = describe_item_container.text_input("学生姓名")
                if student_name != '' and UI_utils.is_valid_student_name(student_name): 
                    #describe_info += f"学生姓名：{student_name}"
                    real_student_name = student_name
                
                describe_info += f"学生姓名：{real_student_name}"

                #长度
                comment_lenth = describe_item_container.radio('选择评语长度（50-200）', 
                                                            ('50', '100', '150','200'),
                                                            horizontal=True, index=1)
                #性别
                sex = describe_item_container.radio('性别', ('男', '女'), horizontal=True)
                if sex :describe_info += f"\n性别：{sex}"
                #性格
                #性格列表
                personality_traits = [
                    '进步','退步','上课专心听讲','上课开小差',
                    '作业认真完成','作业完成一般',"好奇心旺盛", "热情活泼","快乐友善","独立自主","乐于助人",
                    "坚持努力","喜欢学习","善于合作","有创造力",
                    "喜欢表达","有耐心","喜欢挑战","坦率直言","爱幻想","坚持正义",'具有创造性思维','顽皮'
                ]
                student_character = describe_item_container.multiselect("标签(可多选，生成具体的描述)", personality_traits)
                if student_character != '':describe_info += f"\n其他描述：{student_character}"

                #年级
                grade = describe_item_container.radio('年级', ('一年级', '二年级', '三年级', '四年级', '五年级', '六年级'), 
                                        horizontal=True)
                describe_info += f'\n年级：{grade}'


        #描述生成区
        describe_container = container_chat.container()
        describe_container.title('评语区')
        describe_text = describe_container.text_area("根据您的填写得到您学生的描述：", describe_info+"\n\n请确认这段描述是否合您要求，您可以选择手动修改，我将会根据这段描述生成评价", height=150)
        #如果是案例模式则不用点击按钮
        if examples_or_describe != '模板生成':
            d2c_col, info_col = describe_container.columns((1,7))
            describe2comment = d2c_col.button('生成')
            info_col.write("<--------填写完成后点击生成")
            text = ''
            if describe2comment:
                if student_name != '' and UI_utils.is_valid_student_name(student_name): 
                    text=UI_utils.make_comment(describe_text, comment_lenth)
                elif examples_or_describe == "模板生成":
                    text=UI_utils.make_comment(describe_text, comment_lenth)
                else:
                    st.warning("请输入正确的名字")
                #text=UI_utils.make_comment(describe_text, comment_lenth)
        #评语区
        if text == '':
            code_table = container_chat.code("")
        else:
            def add_newlines_every_n_chars(input_string, n=35):
                return '\n'.join(input_string[i:i+n] for i in range(0, len(input_string), n))

            code_table = container_chat.markdown(text) 
             


    else:
        st.write('这是页面2')
        container_excel = st.container()
        container_excel.write("This is inside the container")

