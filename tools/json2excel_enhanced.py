from collections.abc import Generator
from typing import Any
import json
import tempfile
import os

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

import pandas as pd

class Json2ExcelEnhancedTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        json_data = tool_parameters['json_data']
        filename = tool_parameters.get('filename', 'Converted_Data')
        
        try:
            # 验证JSON格式
            try:
                data = json.loads(json_data)
            except json.JSONDecodeError as e:
                raise Exception(f"JSON格式错误: {str(e)}")
            
            # 确保数据是列表格式
            if not isinstance(data, list):
                raise Exception("JSON数据必须是对象数组格式")
            
            if not data:
                raise Exception("JSON数据不能为空")
            
            # 转换为DataFrame
            df = pd.DataFrame(data)
            
            # 创建临时文件
            temp_dir = tempfile.mkdtemp()
            excel_path = os.path.join(temp_dir, f"{filename}.xlsx")
            
            # 保存为Excel文件
            with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            
            # 读取文件并返回
            with open(excel_path, 'rb') as f:
                excel_content = f.read()
            
            yield self.create_file_message(
                content=excel_content,
                filename=f"{filename}.xlsx",
                mime_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            
        except Exception as e:
            error_msg = f"JSON转Excel失败: {str(e)}"
            yield self.create_text_message(f"错误: {error_msg}")
            
        finally:
            # 清理临时文件
            try:
                if 'excel_path' in locals() and os.path.exists(excel_path):
                    os.remove(excel_path)
                    if os.path.exists(temp_dir) and not os.listdir(temp_dir):
                        os.rmdir(temp_dir)
            except Exception:
                pass 