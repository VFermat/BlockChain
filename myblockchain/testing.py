# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:04:35 2018

@author: Vitor Eller
"""

from BlockChain import BlockChain

transactions = [{'value': '500', 'sender': 'eller', 'receiver': 'henry'},
                {'value': '100', 'sender': 'henry', 'receiver': 'lipe'}]

my_chain = BlockChain()

my_chain.print_chain_content()

my_chain.add_block(transactions)

my_chain.print_chain_content()