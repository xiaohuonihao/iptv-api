import re

import requests
from bs4 import BeautifulSoup

from utils.config import config

headers = {
    "Accept": "*/*",
    "Connection": "keep-alive",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

session = requests.Session()


def _merge_headers(custom: dict | None) -> dict:
    """Return a new headers dict merging default headers with custom headers (custom wins)."""
    result = headers.copy()
    if custom:
        for k, v in custom.items():
            if v is None:
                continue
            result[k] = v
    return result


def get_requests(url, data=None, proxy=None, timeout=30, headers_override: dict | None = None):
    """
    Get the response by requests. Accepts headers_override to set request headers.
    """
    if proxy is None:
        proxy = config.http_proxy
    proxies = {"http": proxy, "https": proxy} if proxy else None
    response = None
    try:
        with requests.Session() as session:
            req_headers = _merge_headers(headers_override)
            if data:
                response = session.post(
                    url, headers=req_headers, data=data, proxies=proxies, timeout=timeout
                )
            else:
                response = session.get(url, headers=req_headers, proxies=proxies, timeout=timeout)
    except requests.RequestException as e:
        raise e

    if response is None:
        raise requests.RequestException(f"No response from {url}")

    # ========== 编码修复（使用 requests 自带的 apparent_encoding）==========
    # 自动检测真实编码
    detected_encoding = response.apparent_encoding
    print(f"🔍 自动检测到编码: {detected_encoding} for {url}")
    
    # 用检测到的编码重新解码
    raw_content = response.content
    try:
        fixed_text = raw_content.decode(detected_encoding)
    except (UnicodeDecodeError, LookupError):
        # 失败则回退到 utf-8
        print(f"⚠️ 解码失败，回退到 utf-8 for {url}")
        fixed_text = raw_content.decode('utf-8', errors='ignore')
    
    # 替换 response 的 text 属性
    response._text = fixed_text
    response.encoding = detected_encoding if detected_encoding else 'utf-8'
    # ========== 修复结束 ==========

    text = re.sub(r"<!--.*?-->", "", fixed_text or "", flags=re.DOTALL)
    if not text.strip():
        raise requests.RequestException(f"Empty response from {url}")

    return response


def get_soup_requests(url, data=None, proxy=None, timeout=30, headers_override: dict | None = None):
    """
    Get the soup by requests, pass headers_override to underlying call.
    """
    response = get_requests(url, data, proxy, timeout, headers_override)
    source = re.sub(r"<!--.*?-->", "", response.text or "", flags=re.DOTALL)
    soup = BeautifulSoup(source, "html.parser")
    return soup


def get_source_requests(url, data=None, proxy=None, timeout=30, headers_override: dict | None = None):
    """
    Get the source text by requests.
    """
    if proxy is None:
        proxy = config.http_proxy
    proxies = {"http": proxy, "https": proxy} if proxy else None
    try:
        req_headers = _merge_headers(headers_override)
        if data:
            response = session.post(
                url, headers=req_headers, data=data, proxies=proxies, timeout=timeout
            )
        else:
            response = session.get(url, headers=req_headers, proxies=proxies, timeout=timeout)
    except requests.RequestException:
        return ""
    
    if response is None:
        return ""
    
    source = re.sub(r"<!--.*?-->", "", response.text or "", flags=re.DOTALL)
    return source


def close_session():
    """
    Close the requests session.
    """
    session.close()

