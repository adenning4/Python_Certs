# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 08:10:12 2022

@author: adenn
"""

import math

class Category:
    def __init__(self,name):
        self.name = name.capitalize()
        #self.ledger = [{'amount':0, 'description':'initial value'}] 
        self.ledger = []
    
    def __str__(self):
        info = ''
        titleline = self.name.center(30,'*')
        info += titleline
        for item in self.ledger:
            description = item['description'][:23]
            description = '{:<23}'.format(description)
            amount_raw = item['amount']
            amount = '{:>7.2f}'.format(amount_raw)[:7]
            line = description + amount
            info += '\n' + line
        total_raw = self.get_balance()
        total = '{:.2f}'.format(total_raw)
        info += '\nTotal: ' + total
        return info
        
    def deposit(self,amount,description = ''):
        amount = round(amount,2)
        self.ledger.append({'amount':amount,'description':description})
    
    def withdraw(self,amount,description = ''):
        if self.check_funds(amount) is False:
            return False
        else:
            self.ledger.append({'amount':-amount,'description':description})
            return True
    
    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']
        return balance
    
    def transfer(self,amount,category):
        check = self.withdraw(amount, 'Transfer to ' + category.name)
        if check != False:
            category.deposit(amount, 'Transfer from ' + self.name)
            return True
        else:
            return False
        
    def check_funds(self,amount):
        if (amount > self.get_balance()):
            return False
        else:
            return True
    
def create_spend_chart(categories):
    
    #calculate the total spent for each category
    total_spent=[]
    names=[]
    name_max = 0
    for category in categories:
        spent=0
        for item in category.ledger:
            amount = item['amount']
            if amount < 0:
                spent += abs(amount)
        total_spent.append(spent)
        #grab the category name while looping
        #grab max category name length
        names.append(category.name)
        if len(category.name) > name_max:
            name_max = len(category.name)
        
    
    #calculate the grand total spent
    grand_total = 0
    for total in total_spent:
        grand_total += total
        
    #convert each category's amount spent to percentage of total
    total_percent = []
    for total in total_spent:
        percent = math.floor((total/grand_total)*10)*10
        total_percent.append(percent)
    
    
    #begin writing the final output
    #write title line first
    final_line='Percentage spent by category\n'
    
    #write the percentages and "bars"
    for i in range(100,-10,-10):
        #final_line += '\n'
        yaxis =  str(i)+'|'
        final_line += yaxis.rjust(4,' ')
        for total in total_percent:
            if total >= i:
                final_line += ' o '
            else:
                final_line += '   '
        final_line += ' \n'
        
    #write the horizontal line
    horizontal_line = '    ' + ('---'*len(total_percent)) + '-\n'
    final_line += horizontal_line
    
    #make names common length, left justified
    for i in range(len(names)):
        names[i]=names[i].ljust(name_max,' ')

    for i in range(name_max):
        final_line += '     '
        for name in names:
            #final_line += name[i].center(3)
            final_line += name[i] + '  '
        if i < (name_max-1):
            final_line += '\n'
    
    return final_line
'''
c1 = Category('Business')
c2 = Category('Food')
c3 = Category('Entertainment')
c1.deposit(900,'initial deposit')
c2.deposit(900,'initial deposit')
c3.deposit(900,'initial deposit')
c1.withdraw(10.99,'Cheese')
c2.withdraw(105.55,'Premium')
c3.withdraw(33.40,'TV')

output = create_spend_chart([c1,c2,c3])
print(output)
'''