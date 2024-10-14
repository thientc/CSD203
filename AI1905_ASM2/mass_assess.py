import csv
import sys
# sys.tracebacklimit = 0

import importlib
from MyDoublyLinkedList import DoublyLinkedList as DefaultLinkedList

def printl(text:any):
    print(text,end =" ")
    
def module_import(name):
    components = name.split('.')
    try:
        mod = __import__(components[0])
    except:
        return None
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

student_list_csv = "AI1905.csv"
with open(student_list_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count +=1
            pass
        else:
            print("\n\nAssessment for student {0}".format(row[0]))
            module_name = "{0}.DoublyLinkedList".format(row[0])
            doubly_linked_list = module_import(module_name)
            if not doubly_linked_list:
                printl("  -- student's work not found!")
                continue
            
            printl("Test 01: ...")
            test1 = DefaultLinkedList()
            test1 = doubly_linked_list()
            test1.insert_first(2)
            test1.insert_first(1)
            test1.insert_first(3)
            test1.delete_second()
            test1.insert_first(4)
            result_good = test1.list_from_head()
            asm = doubly_linked_list()
            asm.insert_first(2)
            asm.insert_first(1)
            asm.insert_first(3)
            asm.delete_second()
            asm.insert_first(4)
            result = asm.list_from_head()
            if result_good == result:
                print("  result passed!")
            else:
                print("  result failed!")
            #------------
            print("Test 02:")
            
            test2 = DefaultLinkedList()
            test2.insert_first(2)
            try:
                test2.delete_second()
            except RuntimeError as e:
                pass
            except:
                printl("  -- please check code!")
            
            test2.insert_first(1)
            
            try:
                test2.delete_second()
            except RuntimeError as e:
                pass
            except:
                printl("  -- please check code!")
            result_good = test2.list_from_tail()
            
                            
            asm2 = doubly_linked_list()
            asm2.insert_first(2)
            try:
                asm2.delete_second()
                print("  -- wrong action!")
            except RuntimeError as e:
                if str(e) == "INVALID REQUEST!":
                    print(  "  -- handle passed!")
                else:
                    print("  -- handle message failed!")
            except:
                print("  -- handle failed!")
                
            asm2.insert_first(1)
            try:
                asm2.delete_second()
            except RuntimeError as e:
                if str(e) == "INVALID REQUEST!":
                    print("  -- handle passed!")
                else:
                    print("  -- handle message failed!")
            except:
                print("  -- handle failed!")
            
            try:
                result = asm2.list_from_tail()
            except:
                print("  -- method failed!")
            
            if result_good == result:
                print("  -- result passed!")
            else:
                print("  -- result failed!")
