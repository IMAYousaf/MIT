#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:17:30 2017

@author: munamwasi
"""

string = 'Too many Bananas in a Banana Split Sunday is a nasty thing to eat!'
substring = 'ana'

def main():
    count = 0
    for substring in string:
            count += 1
            
    print("Number of times ana occurs is: ", count)
    
main()