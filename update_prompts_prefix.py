#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json

def update_prompts_with_prefix():
    """
    index.htmlのPROMPTSオブジェクトの各プロンプトに「上に記載の下書きから〜」を追加
    """
    
    # index.htmlファイルを読み込み
    with open('/Users/macbookpro/Claude/prompt-container/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # PROMPTSオブジェクトの部分を抽出
    prompts_pattern = r'const PROMPTS = \{(.*?)\};'
    match = re.search(prompts_pattern, content, re.DOTALL)
    
    if not match:
        print("PROMPTSオブジェクトが見つかりませんでした")
        return
    
    prompts_section = match.group(1)
    
    # 各プロンプトのcontentを「上に記載の下書きから、」で始まるように更新
    def replace_content(match):
        number = match.group(1)
        title = match.group(2)
        original_content = match.group(3)
        
        # すでに「上に記載の下書きから」で始まっている場合はスキップ
        if original_content.strip().startswith('上に記載の下書きから'):
            return match.group(0)
        
        # 新しいcontentを作成
        new_content = f"上に記載の下書きから、{original_content}"
        
        return f"  {number}: {{\n    title: \"{title}\",\n    content: `{new_content}`\n  }},"
    
    # プロンプトの各エントリを更新
    prompt_pattern = r'  (\d+): \{\s*title: "(.*?)",\s*content: `(.*?)`\s*\},'
    updated_prompts = re.sub(prompt_pattern, replace_content, prompts_section, flags=re.DOTALL)
    
    # 元のファイル内容を更新
    new_content = content.replace(match.group(0), f'const PROMPTS = {{{updated_prompts}}};')
    
    # ファイルに書き戻し
    with open('/Users/macbookpro/Claude/prompt-container/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ 全プロンプトに「上に記載の下書きから、」を追加しました")

if __name__ == "__main__":
    update_prompts_with_prefix()