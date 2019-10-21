import redis

# マスタ(Redis)に、入力したキーが存在するか確認
def exists(input):
  HOST = 'localhost'
  # HOST  = ****.****.0001.apne1.cache.amazonaws.com
  r = redis.StrictRedis(host=HOST, port="6379", db=0)
  # 入力された文字列(候補者名+地名)をキーとして使用
  KEY = input

  if r.get(KEY) == None:
    return 0
  else:
    return 1

# 投票ロジック(Redisの特定キーにインクリメント)
def vote(voteeID):
  # TODO to be implemented
  return 1

### Main Logic ###
input = '170384aa-1053-4d43-b407-0e1effb25dbb,小柳初,岐阜'
# comma separate
input = input.split(',')
uuid = input[0]
name = input[1]
pref = input[2]

if exists(name+pref):
  print("有効票")
  # TODO 投票時のキーを考える
  vote(name+pref)
else:
  print("無効票")
  # 無効票


