import json, sys
prompts_data = json.load(sys.stdin)
prompts_js = 'const PROMPTS = {\n'
prompts_js += ',\n'.join([f'  {i+1}: {{ title: `{p["主題"]}`.trim(), content: `### プロンプト\n{p["プロンプト"]}\n\n### 出力例\n{p["出力例"]}\n\n### コメント\n{p["コメント"]}`.trim() }}' for i, p in enumerate(prompts_data)])
prompts_js += '\n};'
print(prompts_js)
