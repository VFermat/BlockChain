# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 08:24:21 2018

@author: Vitor Eller
"""

from hashlib import sha256
from datetime import datetime

class Block:
    
    def __init__(self, transactions, previous_hash):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()
        
    def generate_hash(self):
        header = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(header.encode()).hexdigest()
        return block_hash
    
    def print_block_content(self):
        print('TimeStamp: {}'.format(self.timestamp))
        print('Transactions: {}'.format(self.transactions))
        print('Hash: {}'.format(self.hash))
        