# -*- coding: utf-8 -*-
"""
Created on Thu May 14 06:55:06 2020
@author: lcovarrubias, eledgarmurillo

"""
import utils as utils

class Strategy:
    def __init__(self):
        self.score = 0 # Strategy, score inicial
        self.Responses = {} # Dict obj. recording the action for each input
    def init(self, state):  
        self.Responses[state] = utils.rand_pm() # generates randomly -1 or 1
    def act(self, state):
        if not state in self.Responses: self.init(state)
        return self.Responses[state]
    def update(self, v=1):
        self.score += v #update score 

class User:
    def __init__(self, s=2):
        self.s = s # No. of strategies a user can have
        self.Strategies = [Strategy() for i in range(self.s)] # user strategies
        self.action = None # f4. recording the latest action
        self.score = 0 # score cumulative number of wins
        self.acted = False # flag. if the user acted
 
    def act(self, state):
        self.state = state # f4. recording current global information
        # respond using the bets strategy
        self.strategy_id = utils.max_idx([x.score for x in self.Strategies])
        self.action = self.Strategies[self.strategy_id].act(state) # get act
        self.acted = True # flag. if the user acted
         
    def update(self,w):
        # update scores of strategies based if wins-lose
        assert self.acted, 'act() first before update()'
        # update scores Strategies
        for strategy in self.Strategies:
            ds = utils.bool_pm(strategy.act(self.state) == w)
            strategy.update(ds)
        # update scores User
        self.score += ds
        self.acted = False # reset flag

class System:
    def __init__(self, T = 1, N = 101, m=3, s=2):
        self.T = T # number of steps to run
        self.N = N # number of users
        self.m = m # memory lenght
        self.s = s # number of strategies 
        self.Users = [User(s=self.s) for i in range(self.N)] #initialize users
        self.Prices = [0] # for storing the prices, initialize it with 0
        self.SuccessRates = [] # for storing the global success rates
        self.W = [utils.rand_pm() for i in range(self.m)] # init. global info
        self.D = [] # act. where a_i is the i-th user's action +1 or -1
  
    @property # current act
    def d(self):
        d = 0
        for u in self.Users:
            d += u.action
        return d
     
    def update(self):
        d = self.d
        self.D.append(d)
        self.W.append(utils.minority(d))
        rate = (self.N-abs(d))/(2.0*self.N) # tasa de éxito
        self.SuccessRates.append(rate)
        d = d/float(self.N) # by N get the price
        self.Prices.append(self.Prices[-1] + d) # update price 
             
    @property
    def state(self):
        return utils.w2s(self.W[-self.m:]) # from memory strategies ID
           
    def run(self):
        for t in range(self.T):
            state = self.state
            for u in self.Users:
                u.act(state)
            self.update()
            for u in self.Users:
                u.update(self.W[-1])