from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime 

API_KEY = "PKY4ZBVBSAZI9GZ0HMAI"

API_SECRET = "SVwclaSal6xW7dxOyZ2Gh60oP69xckrLmvooEB7I"   

BASE_URL = "https://paper-api.alpaca.markets/v2"

ALPACE_CREDITS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

class MLTrader(Strategy):
    def initialize(self, symbol:str="SPY", cash_at_risk: float=.5):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None
        self.cash_at_risk = cash_at_risk

    def position_sizing():
        cash = self.get_cash()
        last_price = self.get_last_price(self.symbol)
        # Calculate the number of shares to buy, units per
        quantity = round (cash * self.cash_at_risk / last_price, 0) # round to nearest whole number
        return cash, last_price, quantity

    def on_trading_iteration(self):
        cash, last_price, quantity = self.position_sizing()

        if cash > last_price: # only if you have cash execute
            if self.last_trade == None:
                order = self.create_order(self.symbol, quantity, "buy", type="bracket")
                self.submit_order(order)
                self.last_trade = "buy"
    

start_date = datetime(2023, 12, 15)
end_date = datetime(2023, 12, 31)

broker = Alpaca(ALPACE_CREDITS)

strategy = MLTrader(name='mlstrat', broker = broker, parameters={"symbol": "SPY", "cash_at_risk": 0.5})

strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={}
)
