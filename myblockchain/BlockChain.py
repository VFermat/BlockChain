# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 08:55:08 2018

@author: Vitor Eller
"""

from Block import Block

class BlockChain:
    
    def __init__(self):
        self.chain = []
        self.genesis_block()
        
    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, '0')
        self.chain.append(genesis_block)
    
    def print_chain_content(self):
        for i in range(len(self.chain)):
            print('Block {}'.format(i))
            block = self.chain[i]
            block.print_block_content()
        
    def add_block(self, transactions):
        previous_hash = self.chain[-1].generate_hash()
        new_block = Block(transactions, previous_hash)
        self.chain.append(new_block)
        