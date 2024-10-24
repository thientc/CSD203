import csv
import sys
# sys.tracebacklimit = 0

from MyDoublyLinkedList import DoublyLinkedList as DefaultLinkedList

def printl(text:any):
    print(text,end =" ")
    

def test0(checker:DefaultLinkedList, worker, mark):
    realmark = 0
    print("Test 00: check pop at head, tail:")
    checker.insert_first(2)
    checker.insert_first("hello")
    checker.insert_first(4)
    try:
        worker.insert_first(2)
        worker.insert_first("hello")
        worker.insert_first(4)
    except:
        print("  -- insert into head failed!")
        return 0

    result = checker.show_first()
    try:
        compare = worker.show_first()
    except:
        print("  -- action failed!")

    if compare == result:
        print("  show_first passed, mark +",str(mark/2))
        realmark += mark/2
    else:
        print("  show_first failed!")
    
    result = checker.show_last()
    try:
        compare = worker.show_last()
    except:
        print("  -- action failed!")
    
    if compare == result:
        print("  show_last passed, mark +",str(mark/2))
        realmark +=mark/2 
    else:
        print("  show_last failed!")
    
    return realmark

def test1(checker:DefaultLinkedList, worker, mark):
    print("Test 01: check insert to head, list from head")
    checker.insert_first(2)
    worker.insert_first(2)
    checker.insert_first(1)
    worker.insert_first(1)
    checker.insert_first(3)
    worker.insert_first(3)
    checker.insert_first(4)
    worker.insert_first(4)

    result = checker.list_from_head()
    compare = worker.list_from_head()
    if compare == result:
        print("  result passed, mark +", mark)
        return mark
    else:
        print("  result failed!")
        return 0
    #------------
def test2(checker:DefaultLinkedList, worker, mark):
    print("Test 02: check insert to tail, list from tail")
    checker.insert_last(2)
    checker.insert_last(1)
    checker.insert_last(3)
    checker.insert_last(4)

    try:
        worker.insert_last(2)
        worker.insert_last(1)
        worker.insert_last(3)
        worker.insert_last(4)
    except:
        print("  -- insert into tail failed!")
        return 0
    
    result = checker.list_from_tail()
    try:
        compare = worker.list_from_tail()
    except:
        print("  -- list from tail failed!")
        return 0
    if compare == result:
        print("  result passed, mark +", mark)
        return mark
    else:
        print("  result failed!")
        return 0
    #------------

def test3(checker:DefaultLinkedList, worker, mark):
    print("Test 03: handle deleting from head")
    realmark = 0
    checker.insert_first(1)
    checker.insert_first(2)
    checker.insert_first(3)
    try:
        checker.delete_first()
    except RuntimeError as e:
        pass
    except:
        printl("  -- please check code!")
    result = checker.list_from_head()

    worker.insert_first(1)
    worker.insert_first(2)
    worker.insert_first(3)
    try:
        worker.delete_first()
        compare = worker.list_from_head()
        if compare == result:
            print("  result passed, mark +", mark)
            realmark += mark
        else:
            print("  result failed!")
    except:
        print("  -- wrong action!")
    return realmark      
  
def test4(checker:DefaultLinkedList, worker, mark):
    print("Test 04: handle deleting from tail")
    realmark = 0
    checker.insert_last(1)
    checker.insert_last(2)
    checker.insert_last(3)
    try:
        checker.delete_last()
    except RuntimeError as e:
        pass
    except:
        printl("  -- please check code!")
    result = checker.list_from_tail()

    try:
        worker.insert_last(1)
        worker.insert_last(2)
        worker.insert_last(3)
    except:
        print("  -- wrong action!")
    try:
        worker.delete_last()
        compare = worker.list_from_tail()
        if compare == result:
            print("  result passed, mark +",mark)
            realmark += mark
        else:
            print("  result failed!")
    except:
        print("  -- wrong action!")
    return realmark   

def test5(checker:DefaultLinkedList, worker, mark):
    print("Test 05: handle advanced deleting from head")
    realmark = 0
    checker.insert_first(2)
    try:
        checker.delete_second()
    except RuntimeError as e:
        pass
    except:
        printl("  -- please check code!")

    worker.insert_first(2)
    try:
        worker.delete_second()
        print("  -- wrong action!")
        return 0
    except RuntimeError as e:
        if str(e) == "INVALID REQUEST!":
            realmark += mark/2
            print(  "  -- handle passed, mark + ", str(mark/2))
        else:
            print("  -- handle message failed, mark + ", str(mark/4))
            realmark += mark/4
    except:
        print("  -- handle failed!")

    checker.insert_last(3)
    checker.insert_last(4)
    worker.insert_last(3)
    worker.insert_last(4)
    result = checker.list_from_tail()

    try:
        worker.delete_second()
        compare = worker.list_from_tail()
        if compare == result:
            print("  result passed, mark +",str(mark/2))
            realmark += mark/2
        else:
            print("  result failed!")
    except:
        print("  -- handle failed!")
    
    return realmark
    
def test6(checker:DefaultLinkedList, worker, mark):
    print("Test 06: handle advanced deleting from tail")
    realmark = 0
    checker.insert_last(2)
    try:
        checker.delete_before_last()
    except RuntimeError as e:
        pass
    except:
        printl("  -- please check code!")

    try:
        worker.insert_last(2)
    except:
        print("  -- insert into tail failed!")
        return 0
    try:
        worker.delete_before_last()
        print("  -- wrong action!")
        return 0
    except RuntimeError as e:
        if str(e) == "INVALID REQUEST!":
            realmark += mark/2
            print(  "  -- handle passed, mark + ", str(mark/2))
        else:
            print("  -- handle message failed, mark + ", str(mark/4))
            realmark += mark/4
    except:
        print("  -- handle failed!")

    checker.insert_first(3)
    worker.insert_first(3)
    checker.insert_first(4)
    worker.insert_first(4)
    result = checker.list_from_tail()

    try:
        worker.delete_before_last()
        compare = worker.list_from_tail()
        if compare == result:
            print("  result passed, mark +",str(mark/2))
            realmark += mark/2
        else:
            print("  result failed!")
    except:
        print("  -- handle failed!")
    
    return realmark

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
with open(student_list_csv, encoding='utf-8') as csvin:
    csv_reader = csv.reader(csvin, delimiter=',')
    line_count = 0
    with open('result.csv', 'w', newline='', encoding='utf-8', ) as csvout:
        csvwriter = csv.writer(csvout, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in csv_reader:
            if line_count == 0:
                line_count +=1
                pass
            else:
                if row[0] != 'SE184346':
                    continue
                total_mark = 0
                print("\n\nAssessment for student {0}".format(row[0]))
                module_name = "{0}.DoublyLinkedList".format(row[0])
                doubly_linked_list = module_import(module_name)
                if not doubly_linked_list:
                    printl("  -- student's work not found!")
                    row.append(total_mark)
                    csvwriter.writerow(row)
                    continue
                
                checker0 = DefaultLinkedList()
                worker0 = doubly_linked_list()
                total_mark += test0(checker=checker0, worker=worker0, mark=1)

                checker1 = DefaultLinkedList()
                worker1 = doubly_linked_list()
                total_mark += test1(checker=checker1, worker=worker1, mark=1)
                
                checker2 = DefaultLinkedList()
                worker2 = doubly_linked_list()
                total_mark += test2(checker=checker2, worker=worker2, mark=1)
                
                checker3 = DefaultLinkedList()
                worker3 = doubly_linked_list()
                total_mark += test3(checker=checker3, worker=worker3, mark=1)

                checker4 = DefaultLinkedList()
                worker4 = doubly_linked_list()
                total_mark += test4(checker=checker4, worker=worker4, mark=2)

                checker5 = DefaultLinkedList()
                worker5 = doubly_linked_list()
                total_mark += test5(checker=checker5, worker=worker5, mark=2)

                checker6 = DefaultLinkedList()
                worker6 = doubly_linked_list()
                total_mark += test6(checker=checker6, worker=worker6, mark=2)

                row.append(total_mark)
                print("\nTotal mark for student {0}: {1}".format(row[0], total_mark))
                csvwriter.writerow(row)