from enum import Enum

class CandlestickPattern(Enum):
    HAMMER = (1, lambda prev, current: CandlestickPattern.__hammer_shape(prev) and CandlestickPattern.is_uptrend(current) and CandlestickPattern.is_body_top(prev)),
    INVERTED_HAMMER = (2, lambda prev, current: CandlestickPattern.__hammer_shape(prev) and CandlestickPattern.is_downtrend(current) and CandlestickPattern.is_body_bottom(prev)),
    SHOOTING_STAR = (3, lambda prev, current: CandlestickPattern.__hammer_shape(prev) and CandlestickPattern.is_downtrend(current) and CandlestickPattern.is_body_bottom(prev)),
    HANGING_MAN = (4, lambda prev, current: CandlestickPattern.__hammer_shape(prev) and CandlestickPattern.is_downtrend(current) and CandlestickPattern.is_body_top(prev)),

    def __init__(self, args):
        self.__id = args[0]
        self.__matcher__ = args[1]

    def __hash__(self):
        return hash(self.__id)

    @staticmethod
    def evaluate(prev, current):
        return [t for t in CandlestickPattern if t.__matcher__(prev, current)]

    @staticmethod
    def is_uptrend(candlestick):
        return candlestick['close'] > candlestick['open'] \
               and CandlestickPattern.__body_height(candlestick) > (0.3 * CandlestickPattern.__shadow_height(candlestick))

    @staticmethod
    def is_downtrend(candlestick):
        return candlestick['open'] > candlestick['close'] \
               and CandlestickPattern.__body_height(candlestick) > (0.3 * CandlestickPattern.__shadow_height(candlestick))

    @staticmethod
    def is_body_bottom(candlestick):
        return CandlestickPattern.__body_midpoint(candlestick) < (0.3 * CandlestickPattern.__shadow_height(candlestick))

    @staticmethod
    def is_body_top(candlestick):
        return CandlestickPattern.__body_midpoint(candlestick) > (0.7 * CandlestickPattern.__shadow_height(candlestick))  

    @staticmethod
    def __body_midpoint(candlestick):
        return (0.5 * (candlestick['open'] + candlestick['close'])) - candlestick['low']

    @staticmethod
    def __body_height(candlestick):
        return abs(candlestick['open'] - candlestick['close'])

    @staticmethod
    def __shadow_height(candlestick):
        return abs(candlestick['high'] - candlestick['low'])

    @staticmethod
    def __hammer_shape(candlestick):
        return CandlestickPattern.__body_height(candlestick) < (0.5 * CandlestickPattern.__shadow_height(candlestick))


if __name__ == '__main__':
    print([1][0:1] or 1)



