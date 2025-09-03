# 設定錄影時長和檔案名
DURATION=210  # 錄影時長（秒）
CLEAR_INTERVAL=600  # 10分鐘清除檢查圖像（秒）

# 捕捉初始圖像
raspistill -o prev.jpg -t 1000

LAST_CLEARED=$(date +%s)

while true; do
    # 捕捉當前圖像
    raspistill -o current.jpg -t 100 -w 640 -h 480

    # 計算圖像差異
    DIFF=$(compare -metric PSNR prev.jpg current.jpg null: 2>&1)
    PERCENTAGE=$(echo "$DIFF" | awk '{print (100 - $1)}')

    if (( $(echo "$PERCENTAGE > 53" | bc -l) )); then
        OUTPUT_FILE="video_$(date +%Y%m%d_%H%M%S).mp4"
        echo "Movement detected! Recording..."
        raspivid -o "$OUTPUT_FILE" -t $DURATION -v
        # 錄影後繼續檢測
        raspistill -o prev.jpg -t 1000
    fi

    # 清除圖像
    CURRENT_TIME=$(date +%s)
    if (( CURRENT_TIME - LAST_CLEARED >= CLEAR_INTERVAL )); then
        echo "Clearing check images..."
        rm -f current.jpg
        LAST_CLEARED=$CURRENT_TIME
    fi

    mv current.jpg prev.jpg
    sleep 1  # 每秒檢測一次
done

#copyright givemetocode.net 2025 - github.
