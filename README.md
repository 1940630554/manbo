# 增强版Excel ↔ Json转换器

**作者:** local_user

**版本:** 0.0.1

**类型:** tool

## 描述

这是一个增强版的Excel与Json转换插件，专门解决了原插件可能遇到的HTTP 403错误问题。本插件提供了两个工具：

- `Excel转Json增强版`: 读取Excel文件并输出Json格式的数据，具有改进的文件处理和错误恢复功能
- `Json转Excel增强版`: 将Json字符串（记录列表）转换为Excel文件

## 主要改进

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

## 使用方法

### Excel转Json
1. 上传Excel文件（支持.xlsx和.xls格式）
2. 插件会自动下载并处理文件
3. 输出JSON格式的数据

### Json转Excel
1. 输入JSON字符串（对象数组格式）
2. 可选：指定输出文件名
3. 获得Excel文件下载

## 技术特点

- **本地处理**: 所有转换都在本地完成，保护数据隐私
- **自动清理**: 转换完成后自动删除临时文件
- **多格式支持**: 支持多种Excel文件格式
- **错误恢复**: 完善的错误处理和用户提示

## 依赖项目

- [pandas](https://github.com/pandas-dev/pandas), BSD 3-Clause License
- [openpyxl](https://openpyxl.readthedocs.io/), MIT License
- [requests](https://requests.readthedocs.io/), Apache 2.0 License

## 许可证

Apache License 2.0

## 隐私

本插件不收集任何数据。所有文件转换都在本地完成，不会向第三方服务传输数据。 