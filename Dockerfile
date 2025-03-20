FROM aliyunfc/runtime-python3.9

# 安装必要的系统依赖，包括支持图形界面的库
RUN yum update -y && \
    yum install -y \
    mesa-libGL-devel \
    libXext \
    libSM \
    libXrender \
    && yum clean all

# 安装Python依赖包
RUN pip install --upgrade pip && \
    pip install opencv-python moviepy oss2 flask

# 设置工作目录（可选）
WORKDIR /app


# 复制你的代码到容器中（根据实际情况调整路径）
 COPY . /app

# 如果有额外的配置或初始化脚本，可以在这里添加

# 默认命令或其他入口点设置（根据实际情况调整）
CMD ["python", "main.py"]