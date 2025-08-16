#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def fix_javascript_syntax():
    """
    JavaScriptオブジェクトのキー部分の「：」を「:」に修正
    """
    
    # index.htmlファイルを読み込み
    with open('/Users/macbookpro/Claude/prompt-container/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # オブジェクトキーの「：」を「:」に修正
    # パターン: 数字： → 数字:
    updated_content = re.sub(r'(\d+)：\{', r'\1: {', content)
    
    # 出力フォーマット内の「：」はそのまま残す（文字列内なので）
    
    # ファイルに書き戻し
    with open('/Users/macbookpro/Claude/prompt-container/index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ JavaScript構文エラーを修正しました")
    print("  - オブジェクトキーの「：」を「:」に変更")

if __name__ == "__main__":
    fix_javascript_syntax()