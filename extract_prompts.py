#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json

def extract_prompts_from_markdown(md_file_path):
    """
    markdownファイルからプロンプトを抽出してJavaScript形式に変換
    """
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prompts = {}
    
    # パターン: ## 番号. タイトル または # 番号. タイトル
    # その後の ### プロンプト以下の ```コードブロック``` を抽出
    pattern = r'(?:^## |^# )(\d+)\.\s+(.*?)\n.*?### プロンプト\n\n```\n(.*?)\n```'
    
    matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
    
    for match in matches:
        number = int(match[0])
        title = match[1].strip()
        prompt_content = match[2].strip()
        
        # バッククォートとバックスラッシュをエスケープ
        escaped_content = prompt_content.replace('\\', '\\\\').replace('`', '\\`')
        
        prompts[number] = {
            'title': title,
            'content': escaped_content
        }
    
    return prompts

def generate_javascript_object(prompts_dict):
    """
    プロンプト辞書からJavaScriptのPROMPTSオブジェクトを生成
    """
    js_lines = ["const PROMPTS = {"]
    
    for number in sorted(prompts_dict.keys()):
        prompt = prompts_dict[number]
        title = prompt['title']
        content = prompt['content']
        
        js_lines.append(f"  {number}: {{")
        js_lines.append(f"    title: \"{title}\",")
        js_lines.append(f"    content: `{content}`")
        js_lines.append(f"  }},")
    
    js_lines.append("};")
    
    return '\n'.join(js_lines)

if __name__ == "__main__":
    # プロンプト抽出
    prompts = extract_prompts_from_markdown('/Users/macbookpro/Claude/prompt-container/prompt.md')
    
    print(f"抽出されたプロンプト数: {len(prompts)}")
    
    # JavaScriptオブジェクト生成
    js_code = generate_javascript_object(prompts)
    
    # 結果を出力ファイルに保存
    with open('/Users/macbookpro/Claude/prompt-container/prompts_generated.js', 'w', encoding='utf-8') as f:
        f.write(js_code)
    
    print("JavaScriptオブジェクトが prompts_generated.js に生成されました")
    print(f"プロンプト番号: {sorted(prompts.keys())}")