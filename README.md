<<<<<<< HEAD
# Web UI 自动化测试框架

基于 Playwright + pytest + Python 的 Web UI 自动化测试框架。

## 项目结构

```
play/
├── config/                # 配置文件
│   ├── __init__.py
│   └── config.py          # 配置类
├── logs/                  # 日志文件（自动生成）
├── pages/                 # 页面对象模型
│   ├── __init__.py
│   ├── base_page.py       # 基础页面类
│   └── google_search_page.py  # 示例页面类
├── reports/               # 测试报告（自动生成）
├── tests/                 # 测试用例
│   ├── __init__.py
│   └── test_google_search.py  # 示例测试用例
├── utils/                 # 工具类
│   ├── __init__.py
│   └── logger.py          # 日志工具
├── .env                   # 环境变量配置
├── conftest.py            # pytest 配置和 fixtures
├── pytest.ini             # pytest 运行配置
├── README.md              # 项目说明文档
├── requirements.txt       # 依赖包列表
└── venv/                  # 虚拟环境（自动生成）
```

## 安装步骤

1. **克隆项目**

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   ```

3. **激活虚拟环境**
   - Windows: `venv\Scripts\Activate.ps1`
   - Linux/Mac: `source venv/bin/activate`

4. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

5. **安装 Playwright 浏览器**
   ```bash
   playwright install
   ```

## 运行测试

### 运行所有测试
```bash
pytest
```

### 运行指定测试文件
```bash
pytest tests/test_google_search.py
```

### 运行指定测试用例
```bash
pytest tests/test_google_search.py::test_google_search
```

## 查看报告

测试运行完成后，报告将生成在 `reports/report.html` 目录中。

## 配置说明

可以通过修改 `.env` 文件来配置测试环境：

- `BASE_URL`: 测试基础 URL
- `BROWSER`: 浏览器类型（chromium, firefox, webkit）
- `HEADLESS`: 是否以无头模式运行（true/false）
- `TIMEOUT`: 超时时间（毫秒）
- `REPORTS_DIR`: 报告目录

## 页面对象模型（POM）

框架采用页面对象模型，将页面元素和操作封装在对应的页面类中：

- `BasePage`: 基础页面类，提供通用的页面操作方法
- `GoogleSearchPage`: 示例页面类，封装 Google 搜索页面的元素和操作

## 日志功能

测试过程中的日志会记录在 `logs` 目录中，包括调试信息、警告和错误。

## 扩展指南

1. **添加新页面**
   - 在 `pages` 目录下创建新的页面类，继承 `BasePage`
   - 封装页面元素和操作方法

2. **添加新测试用例**
   - 在 `tests` 目录下创建新的测试文件
   - 使用对应的页面类进行测试

3. **添加新工具**
   - 在 `utils` 目录下创建新的工具类

## 依赖说明

- `playwright`: 浏览器自动化库
- `pytest`: 测试框架
- `pytest-playwright`: pytest 与 Playwright 的集成
- `pytest-html`: 生成 HTML 测试报告
- `python-dotenv`: 管理环境变量

## Jenkins 集成

### 前提条件
1. 安装 Jenkins
2. 安装 Git 插件（用于代码拉取）
3. 安装 HTML Publisher 插件（用于查看测试报告）
4. 安装 JUnit 插件（用于测试结果分析）

### 集成步骤

1. **创建新的 Jenkins 任务**
   - 选择「流水线」类型
   - 在「流水线」选项中，选择「从 SCM 中获取 Jenkinsfile」
   - 配置 Git 仓库地址和凭证
   - 设置分支（如 `main` 或 `master`）

2. **配置构建触发器**
   - 可以设置定时构建（如每天凌晨执行）
   - 或设置代码提交触发构建

3. **运行构建**
   - 保存配置后，点击「立即构建」
   - 查看构建日志和测试报告

### 构建脚本

项目中已包含以下构建相关文件：

- `Jenkinsfile`: Jenkins 流水线配置文件
- `build.sh`: 通用构建脚本（支持 Linux/Mac/Windows）

### 查看测试报告

构建完成后，可以在 Jenkins 任务页面查看：
- **HTML 报告**: 通过「HTML 报告」链接查看详细的测试结果
- **测试结果趋势**: 通过「测试结果」查看历史测试趋势
- **构建历史**: 查看每次构建的状态和日志
=======
# playwright-ui-test
>>>>>>> 25c4041eadb96bf23ba908853e5a89ed4767a2b7
