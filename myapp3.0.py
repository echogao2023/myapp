#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "当前时间:" + time.asctime(t)
 
print(str);
import streamlit as st
from glm import GLMGenerator
import os

# 实例化GLMGenerator
generator = GLMGenerator(model_name="gh/GLChineseBERT-wm-ext-forward")

# 定义Streamlit界面
def main():
    # 创建一个输入框，接收用户输入的文本
    user_input = st.text_input("请输入你的需求：", "")

    if st.button("生成App"):
        # 使用GLM2-6B生成文本
        app_description = generator.generate_text(user_input, max_length=100)[0]
        # 生成App的名称和描述
        app_name = "个性化App"
        app_description = f"这是一个基于你的需求生成的个性化App。需求：{user_input}\n\n{app_description}"
        
        # 在Streamlit界面上展示App的名称和描述
        st.markdown(f"### App名称：{app_name}")
        st.markdown(f"#### App描述：{app_description}")

        # 保存描述为一个文件
        save_app_description(app_name, app_description)

# 保存App描述为文件，并打包为安装包
def save_app_description(app_name, app_description):
    file_path = f"{app_name}.txt"  # 文件保存路径
    with open(file_path, "w") as f:
        f.write(app_description)
    
    st.markdown(f"已成功保存App描述为文件：{file_path}")

    package_name = f"{app_name}.apk"  # 安装包名称
    package_path = f"./{package_name}"  # 安装包保存路径
    os.system(f"android-packager {file_path} -o {package_name} -t {app_name}")

    st.markdown(f"已成功生成安装包文件：{package_name}")

    # 提供一个下载链接来下载安装包
    st.markdown(f"#### [点击这里下载安装包]({package_path})")

if __name__ == "__main__":
    main()
    