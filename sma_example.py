from AlgorithmImports import *

class SimpleMovingAverageAlgorithm(QCAlgorithm):
    def Initialize(self) -> None:
        self.SetStartDate(2006,1, 1)  #Set Start Date
        self.SetEndDate(2023,6,1)    #Set End Date
        self.SetCash(100000)           #Set Strategy Cash
        # Find more symbols here: http://quantconnect.com/data
        self.AddEquity("SPY", Resolution.Daily)
        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.sma_15 = self.SMA(self.symbol, 15 , Resolution.Daily)
        self.sma_60 = self.SMA(self.symbol, 50 , Resolution.Daily)
        self.sma_120 = self.SMA(self.symbol, 100 , Resolution.Daily)
    def OnData(self, slice: Slice) -> None:
        if self.sma_60.IsReady and self.Portfolio.Invested:
            
            if self.sma_60[0] < self.sma_60[1] :
                self.Liquidate()
                return
            if self.sma_120[0] < self.sma_120[1] :
                self.Liquidate()
                return
                
        #     # The current value of self.sma is represented by self.sma.Current.Value
        #     self.Plot("SimpleMovingAverage", "sma", self.sma.Current.Value)
        #     # Plot all attributes of self.sma
        #     self.Plot("SimpleMovingAverage", "rollingsum", self.sma.RollingSum.Current.Value)
        
        if not self.Portfolio.Invested:
            # if self.sma_15[0] > self.sma_15[1] :
                self.SetHoldings("SPY", 1)
