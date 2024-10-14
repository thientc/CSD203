import pandas as pd
from datetime import date
import csv

def main():
        print(" 1. Products          2. Customer list       3. Order list")
        c = input("Enter Choice : ")       
        if c == "1":
                product()
        elif c == '2':
                manager()
        elif c == '3':
                order()
        else:
                main()
                
def product():
        print("1. Check Products.     2. Buy.       3. Cancel")
        c = input("Enter Choice : ")
        if c == '1':
                cproducts()
        elif c == '2':
                buy()
        elif c == '3':
                cancel()
        else:
                product()

def cproducts():
        l = r'D:\Phi\products.csv'
        with open(l,'r') as cf:
            cw = csv.reader(cf)
            cd = pd.DataFrame(cw)
            print("|-----------------------------------------------------------------|")
            for i in cd.index:
                x = list(cd.loc[i])
                print("PCODE : ",i)
                print("Pro Name : ",x[0])
                print("Quantity : ",x[1])
                print("Saled : ",x[2])
                print("Price : ",x[3])
                print("|-----------------------------------------------------------------|")
        cf.close()
        product()

def buy():
        p = input("PCODE : ")
        n = input("Customer : ")
        a = input("Quantity : ")
        t = date.today()
        row =  [p,n,a,t]
        print("Ordering product")
        ol = r'D:\Phi\ordering.csv'
        with open(ol,'a+',newline='') as cf:
            cw = csv.writer(cf)
            cw.writerow(row)
        cf.close()
        product()

def cancel():
        p = input("PCODE : ")
        n = input("Customer : ")
        a = input("Quantity : ")
        t = input("Date : ")
        row =  [p,n,a,t]
        l = r'D:\Phi\ordering.csv'
        with open(l,'r+') as cf:
            cw = csv.reader(cf)
            cd = pd.DataFrame(cw)
            for i in cd.index:
                x = list(cd.loc[i])
                if row == x:
                    cd.drop([i],inplace=True)
            cf.close()
            with open(l, 'w',newline='') as cf:
                cw = csv.writer(cf)
                for i in cd.index:
                    x = list(cd.loc[i])
                    cw.writerow(x)
            cf.close()
        product()
        
        
def manager():
        print("1. Add.       2. Products.     3. Delete.     4. Check Orders.  ")
        c = input("Enter Choice : ")
        if c == '1':
                add()
        elif c == '2':
                products()
        elif c == '3':
                delete()
        elif c == '4':
                corders()
        else:
                manager()

def add():
        n = input("Product Name : ")
        c = input("Quantity : ")
        d = input("Price : ")
        row =  [n,c,d]
        l = r'D:\Phi\products.csv'
        with open(l, 'a+',newline='') as cf:
            cw = csv.writer(cf)
            cw.writerow(row)
        cf.close()
        manager()

def products():
        l = r'D:\Phi\products.csv'
        with open(l,'r') as cf:
            cw = csv.reader(cf)
            cd = pd.DataFrame(cw)
            print("|-----------------------------------------------------------------|")
            for i in cd.index:
                x = list(cd.loc[i])
                print("PCODE : ",i)
                print("NAME : ",x[0])
                print("Price : ",x[1])
                print("Quantity : ",x[2])
                print("|-----------------------------------------------------------------|")
        cf.close()
        manager()

def delete():
        d = int(input("Enter pcode : "))
        l = r'D:\Phi\products.csv'
        with open(l,'r+') as cf:
            cw = csv.reader(cf)
            cd = pd.DataFrame(cw)
            cd.drop([d],inplace=True)
            cf.close()
            with open(l, 'w',newline='') as cf:
                cw = csv.writer(cf)
                for i in cd.index:
                    x = list(cd.loc[i])
                    cw.writerow(x)
        cf.close()
        manager()
        
def order():
        l = r'D:\Phi\ordering.csv'
        with open(l,'r') as cf:
            cw = csv.reader(cf)
            cd = pd.DataFrame(cw)
            print("|-----------------------------------------------------------------|")
            for i in cd.index:
                x = list(cd.loc[i])
                print("PCODE : ",x[0])
                print("CCODE : ",x[1])
                print("QUANTITY : ",x[2])
                print("|-----------------------------------------------------------------|")
        cf.close()
        main()
main()