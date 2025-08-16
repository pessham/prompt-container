#!/bin/bash

# QRコード一括生成スクリプト
# prompt-container.vercel.app の各プロンプト（#p1~#p85）へのQRコード生成

BASE_URL="https://prompt-container.vercel.app"
OUTPUT_DIR="qr-codes"

# qr-codesディレクトリが存在しない場合は作成
mkdir -p "$OUTPUT_DIR"

echo "=== Prompt Container QRコード生成開始 ==="
echo "Base URL: $BASE_URL"
echo "出力先: $OUTPUT_DIR/"
echo ""

# 1から85まで順次QRコード生成
for i in {1..85}
do
    URL="${BASE_URL}#p${i}"
    OUTPUT_FILE="${OUTPUT_DIR}/qr-p${i}.png"
    
    echo "生成中: QR-${i} -> ${URL}"
    
    # qrencode でQRコード生成
    qrencode -o "$OUTPUT_FILE" -s 8 -m 2 "$URL"
    
    if [ $? -eq 0 ]; then
        echo "✓ 完了: $OUTPUT_FILE"
    else
        echo "✗ 失敗: QR-${i}"
    fi
done

echo ""
echo "=== QRコード生成完了 ==="

# 生成されたファイル数を確認
GENERATED_COUNT=$(ls -1 "$OUTPUT_DIR"/qr-p*.png 2>/dev/null | wc -l)
echo "生成されたQRコード数: ${GENERATED_COUNT}/85"

if [ "$GENERATED_COUNT" -eq 85 ]; then
    echo "🎉 85個すべてのQRコード生成に成功しました！"
else
    echo "⚠️  一部のQRコード生成に失敗した可能性があります"
fi

echo ""
echo "生成されたファイル一覧:"
ls -la "$OUTPUT_DIR"/qr-p*.png | head -10
if [ "$GENERATED_COUNT" -gt 10 ]; then
    echo "... (残り $((GENERATED_COUNT - 10)) ファイル)"
fi