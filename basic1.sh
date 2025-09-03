# 設定錄影時長和檔案名
DURATION=210  # 錄影時長（秒）
OUTPUT_FILE="video_$(date +%Y%m%d_%H%M%S).mp4"

# 捕捉初始圖像
raspistill -o prev.jpg -t 1000

# 設定清除檢查圖像的間隔（以秒為單位）
CLEAR_INTERVAL=600  # 10分鐘
LAST_CLEARED=$(date +%s)

while true; do
    # 捕捉當前圖像
    raspistill -o current.jpg -t 100 -w 640 -h 480

    # 計算圖像差異
    DIFF=$(compare -metric PSNR prev.jpg current.jpg null: 2>&1)

    # 轉換 PSNR 值為百分比
    PERCENTAGE=$(echo "$DIFF" | awk '{print (100 - $1)}')

    # 檢查是否達到差異閾值
    if (( $(echo "$PERCENTAGE > 53" | bc -l) )); then
        echo "Movement detected! Recording..."
        raspivid -o "$OUTPUT_FILE" -t $DURATION -v
        break
    fi

    # 更新上一幀
    mv current.jpg prev.jpg

    # 檢查是否需要清除圖像
    CURRENT_TIME=$(date +%s)
    if (( CURRENT_TIME - LAST_CLEARED >= CLEAR_INTERVAL )); then
        echo "Clearing check images..."
        rm -f prev.jpg current.jpg
        touch prev.jpg  # 重新創建 prev.jpg
        LAST_CLEARED=$CURRENT_TIME
    fi

    sleep 1  # 每秒檢測一次
done

echo "Recording complete. Video saved as $OUTPUT_FILE."
