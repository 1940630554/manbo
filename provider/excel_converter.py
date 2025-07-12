from collections.abc import Generator
from typing import Any
import os
import tempfile
import requests
from urllib.parse import urlparse

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

import pandas as pd

class ExcelConverterProvider:
    """Enhanced Excel converter provider with improved file handling"""
    
    @staticmethod
    def download_file_safely(file_url: str) -> str:
        """
        安全下载文件到本地临时目录
        """
        try:
            # 创建临时文件
            temp_dir = tempfile.mkdtemp()
            file_name = os.path.basename(urlparse(file_url).path) or "temp_file.xlsx"
            local_path = os.path.join(temp_dir, file_name)
            
            # 设置请求头，模拟浏览器行为
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,*/*',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
            
            # 下载文件
            response = requests.get(file_url, headers=headers, timeout=30, stream=True)
            response.raise_for_status()
            
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            return local_path
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"文件下载失败: {str(e)}")
        except Exception as e:
            raise Exception(f"文件处理失败: {str(e)}")
    
    @staticmethod
    def read_excel_safely(file_path: str) -> pd.DataFrame:
        """
        安全读取Excel文件
        """
        try:
            # 尝试不同的引擎读取Excel文件
            engines = ['openpyxl', 'xlrd']
            df = None
            
            for engine in engines:
                try:
                    df = pd.read_excel(file_path, engine=engine, dtype=str)
                    break
                except Exception:
                    continue
            
            if df is None:
                raise Exception("无法读取Excel文件，请检查文件格式")
            
            return df
            
        except Exception as e:
            raise Exception(f"Excel文件读取失败: {str(e)}")
    
    @staticmethod
    def cleanup_temp_file(file_path: str):
        """
        清理临时文件
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                temp_dir = os.path.dirname(file_path)
                if os.path.exists(temp_dir) and not os.listdir(temp_dir):
                    os.rmdir(temp_dir)
        except Exception:
            pass  # 忽略清理错误 