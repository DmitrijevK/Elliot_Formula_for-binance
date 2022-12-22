import binance
import pandas as pd

# create class BinanceClient
client = binance.Client(api_key='API_KEY', api_secret='API_SECRET')

# requesting information for the last 30 days
klines = client.futures.klines(symbol='BTCUSDT', interval=binance.enums.KLINE_INTERVAL_1DAY, limit=30)

# Transform the recieved data info to DataFrame
df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignored'])

# Convert timestamp to date
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Building Elliot Waves based on closing Prices
elliott_waves = elliott_wave_count(df['close'])

if elliott_waves[-1]['trend'] == 'up':
    print('The coin is in an upward wave, ст')
elif elliott_waves[-1]['trend'] == 'down':
    print('The coin is in a downward wave, it is not recommended to consider buying')

if elliott_waves[-1]['trend'] == 'down' and elliott_waves[-1]['correction'] == 'up':
  print('The coin is in a downward wave, but an upward turn is expected (correction), a purchase option can be considered')
