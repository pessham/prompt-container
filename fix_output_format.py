#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def analyze_and_fix_prompts():
    """
    全プロンプトの出力フォーマットを分析し、不自然なラベル形式を自然な文章に修正
    """
    
    # index.htmlファイルを読み込み
    with open('/Users/macbookpro/Claude/prompt-container/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修正が必要なパターンを定義
    fixes = [
        # #1 メール関連の「結論：」「理由：」「次の一手：」形式を自然な文章に
        {
            'pattern': r'結論：\{目的\}のため、\{実施内容\}いたします。\n理由：\{根拠や効果を1行\}\n次の一手：\{期日\}までに\{具体アクション\}いたします。',
            'replacement': '{目的}のため、{実施内容}いたします。\n{根拠や効果を1行}\n{期日}までに{具体アクション}いたします。'
        },
        
        # #8 提案受領の「感謝（1文）」「要旨の復唱（1行）」形式
        {
            'pattern': r'\{感謝（1文）\}。\{要旨の復唱（1行）\}。\n次の一手：\{具体アクション（日時/判断ポイント）\}。',
            'replacement': '{感謝（1文）}。{要旨の復唱（1行）}。\n{具体アクション（日時/判断ポイント）}をお願いいたします。'
        },
        
        # #9 上司報告の「現状：」「課題：」「相談：」形式
        {
            'pattern': r'現状: \{今の到達点\}\n課題: \{詰まり/リスク\}\n相談: \{承認/方針/予算などのYes/No問合せ\}',
            'replacement': '現状：{今の到達点}\n課題：{詰まり/リスク}\nご相談：{承認/方針/予算などのYes/No問合せ}'
        },
        
        # #10 断りの「謝意（1文）」「困難理由（1行）」形式
        {
            'pattern': r'\{謝意（1文）\}。\{困難理由（1行）\}。\{代替案（紹介/時期提案など）\}。\{必要ならお手伝いの意志\}。',
            'replacement': '{謝意（1文）}。{困難理由（1行）}。{代替案（紹介/時期提案など）}。{必要ならお手伝いの意志}。'
        },
        
        # #5 遅延お詫びの形式
        {
            'pattern': r'\{お礼/お詫び\}。\{理由（名詞句）\}により遅延しました。\{挽回策（今日/いつまでに何をするか）\}。',
            'replacement': '{お礼/お詫び}。{理由（名詞句）}により遅延いたしました。{挽回策（今日/いつまでに何をするか）}。'
        },
        
        # #7 クレーム初動の「お詫び：」「事実確認：」「提案：」形式
        {
            'pattern': r'お詫び: \{ご不便への謝罪\}\n事実確認: \{確認中の対象/範囲（1行）\}\n提案: \{選択肢1\} または \{選択肢2\}',
            'replacement': '{ご不便への謝罪}\n{確認中の対象/範囲（1行）}\n{選択肢1}または{選択肢2}をご提案いたします。'
        },
        
        # #25 記事要約の「結論：」「理由：」「明日試す一手：」形式
        {
            'pattern': r'結論: \{主要メッセージを1行\}\n理由: \{根拠や重要データを1行\}\n明日試す一手: \{具体行動を1行\}',
            'replacement': '要約：{主要メッセージを1行}\n根拠：{根拠や重要データを1行}\n実践案：{具体行動を1行}'
        },
        
        # #42 導入→結果→次の一手の「導入前：」形式
        {
            'pattern': r'導入前: \{現状の痛み\}\n導入後: \{改善の実感や数値\}\n次の一手: \{誰が/何を/いつまでに\}',
            'replacement': '導入前：{現状の痛み}\n導入後：{改善の実感や数値}\n次のアクション：{誰が/何を/いつまでに}'
        },
        
        # 汎用的なラベル形式の修正
        {
            'pattern': r'(\w+): (\{[^}]+\})',
            'replacement': r'\1：\2'
        }
    ]
    
    updated_content = content
    changes_made = []
    
    # 各修正パターンを適用
    for i, fix in enumerate(fixes):
        old_content = updated_content
        updated_content = re.sub(fix['pattern'], fix['replacement'], updated_content, flags=re.MULTILINE)
        if old_content != updated_content:
            changes_made.append(f"パターン{i+1}: {len(re.findall(fix['pattern'], old_content))}箇所修正")
    
    # ファイルに書き戻し
    if changes_made:
        with open('/Users/macbookpro/Claude/prompt-container/index.html', 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print("✅ プロンプト出力フォーマットを自然な文章に修正しました")
        for change in changes_made:
            print(f"  - {change}")
    else:
        print("❌ 修正対象が見つかりませんでした")

if __name__ == "__main__":
    analyze_and_fix_prompts()