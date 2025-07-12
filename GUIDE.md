# 增强版Excel转换器插件开发指南

## 项目概述

这是一个增强版的Excel与Json转换插件，专门解决了原插件可能遇到的HTTP 403错误问题。本插件提供了改进的文件处理机制和更好的错误恢复功能。

## 主要特性

### 1. 改进的文件下载机制
- 使用更安全的HTTP请求头，模拟浏览器行为
- 添加超时和重试机制
- 更好的错误处理和用户反馈

### 2. 增强的错误处理
- 详细的错误信息提示
- 自动清理临时文件
- 多种Excel引擎支持（openpyxl, xlrd）

### 3. 数据验证
- JSON格式验证
- Excel文件格式检查
- 数据类型安全处理

## 项目结构

```
2/
├── manifest.yaml              # 插件清单文件
├── main.py                    # 主入口文件
├── requirements.txt           # 依赖文件
├── README.md                  # 项目说明
├── PRIVACY.md                 # 隐私政策
├── GUIDE.md                   # 开发指南（本文件）
├── .difyignore                # Dify打包忽略文件
├── .gitignore                 # Git忽略文件
├── icon.svg                   # 插件图标
├── _assets/                   # 资源文件
├── provider/
│   ├── excel_converter.yaml   # 工具提供者配置
│   └── excel_converter.py     # 核心转换逻辑
└── tools/
    ├── excel2json_enhanced.yaml    # Excel转JSON工具配置
    ├── excel2json_enhanced.py      # Excel转JSON实现
    ├── json2excel_enhanced.yaml    # JSON转Excel工具配置
    └── json2excel_enhanced.py      # JSON转Excel实现
```

## 开发环境设置

### 1. 安装依赖
```bash
cd 2
pip install -r requirements.txt
```

### 2. 本地调试
创建 `.env` 文件并配置以下环境变量：
```
INSTALL_METHOD=remote
REMOTE_INSTALL_URL=your_dify_instance:5003
REMOTE_INSTALL_KEY=your_debug_key
```

### 3. 运行插件
```bash
python -m main
```

## 核心组件说明

### ExcelConverterProvider
位于 `provider/excel_converter.py`，提供以下核心功能：

- `download_file_safely()`: 安全下载文件到本地临时目录
- `read_excel_safely()`: 安全读取Excel文件，支持多种引擎
- `cleanup_temp_file()`: 清理临时文件

### 工具实现
- `Excel2JsonEnhancedTool`: Excel转JSON工具，具有改进的错误处理
- `Json2ExcelEnhancedTool`: JSON转Excel工具，支持数据验证

## 打包和发布

### 1. 打包插件
```bash
dify plugin package ./2
```

### 2. 安装插件
- 在Dify插件管理页面选择"通过本地文件安装"
- 上传生成的 `.difypkg` 文件

## 故障排除

### HTTP 403错误
本插件通过以下方式解决HTTP 403错误：
- 使用完整的浏览器请求头
- 添加User-Agent和其他必要的头信息
- 实现流式下载机制

### 文件读取错误
- 支持多种Excel引擎（openpyxl, xlrd）
- 自动尝试不同的读取方式
- 提供详细的错误信息

### 内存管理
- 自动清理临时文件
- 使用流式处理大文件
- 及时释放资源

## 版本更新

当需要更新插件时：
1. 修改 `manifest.yaml` 中的版本号
2. 更新相关代码
3. 重新打包插件
4. 在Dify中重新安装

## 贡献指南

1. Fork项目
2. 创建功能分支
3. 提交更改
4. 创建Pull Request

## 许可证

Apache License 2.0

## 支持

如有问题或建议，请通过以下方式联系：
- 创建Issue
- 提交Pull Request
- 发送邮件反馈 