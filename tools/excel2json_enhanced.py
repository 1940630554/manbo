from collections.abc import Generator
from typing import Any
import json

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from provider.excel_converter import ExcelConverterProvider

class Excel2JsonEnhancedTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        file_meta = tool_parameters['file']
        local_file_path = None
        
        try:
            # 安全下载文件
            local_file_path = ExcelConverterProvider.download_file_safely(file_meta.url)
            
            # 安全读取Excel文件
            df = ExcelConverterProvider.read_excel_safely(local_file_path)
            
            # 转换为JSON
            json_data = df.to_json(orient="records", force_ascii=False, indent=2)
            
            # 验证JSON格式
            json.loads(json_data)  # 确保JSON格式正确
            
            yield self.create_text_message(json_data)
            
        except Exception as e:
            error_msg = f"Excel转JSON失败: {str(e)}"
            yield self.create_text_message(f"错误: {error_msg}")
            
        finally:
            # 清理临时文件
            if local_file_path:
                ExcelConverterProvider.cleanup_temp_file(local_file_path) 