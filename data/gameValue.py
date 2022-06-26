
myPlayerRole = ""
anotherPlayerRole = ""

socket = None

upperPlayerTimeCard = None
upperPlayerBuffCard = None
upperPlayerDraw = 5


lowerPlayerTimeCard = None
lowerPlayerTimeCard = None
lowerPlayerDraw = 999
lowerPlayerUsable_card = 99999


# 重要全局变量 ##########################################
# 全局部分
GAME_STATE = "playing"
WINNER = ""
TURN = 1

# 资本家部分
MARKET_VALUE = 101  # 市值，以亿为单位结算
WORKERS = 5  # 工人数量

# 官僚部分
TRACE = 0

# 工人部分 ##########################################
DISSATISFACTION = 0  # 不满值
RELATION = 0  # 人脉
