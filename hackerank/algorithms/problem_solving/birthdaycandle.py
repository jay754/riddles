def birthdayCakeCandles(candles):
    tallest_candle = max(candles)
    candle_count = 0
    
    for i in candles:
        if i == tallest_candle:
            candle_count += 1
            
    return candle_count

