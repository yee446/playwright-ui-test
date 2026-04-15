#!/bin/bash

# 设置错误时退出
set -e

echo "=== 开始构建和测试 ==="

# 创建虚拟环境
if [ ! -d "venv" ]; then
    echo "创建虚拟环境..."
    python -m venv venv
fi

# 激活虚拟环境
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate.ps1" ]; then
    venv\Scripts\Activate.ps1
fi

# 安装依赖
echo "安装依赖..."
pip install -r requirements.txt

# 安装Playwright浏览器
echo "安装Playwright浏览器..."
playwright install

# 运行测试
echo "运行测试..."
pytest tests/ --html=reports/report.html --self-contained-html

echo "=== 构建和测试完成 ==="