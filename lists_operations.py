#tons of ways to make lists
#1 []
list1 = [1,2,3,4,5]
print("List created using square brackets:", list1)

#2 list() method
list2 = list((6,7,8,9,10))
print("List made by list() fn:", list2)

#3 list comprehension
list3 = [x for x in range(11, 16)]
print("List made by lift comprehension:", list3)

#4 * operator
list4 = [0] * 5
print("List created using * operator:", list4)

#5 append()
list5 = []
for i in range(1,6):
    list5.append(i)
print("List created using the append() method:", list5)

#6 extend
list6 = []
list6.extend([1,2,3])
list6.extend([4,5])
print("List created using extend method:", list6)


#list operations
the_list = [2, 19, 33, 51, 67, 84, 95]  #for demonstrating operations.

#1 len()
print("Using len() on the list:", len(the_list))

#2 count()
print("Using count() on the list:", count(the_list))

#3 index()
print("Using index() in the list:", the_list.index(51))

#4 append()
the_list.append(42)
print("appending 42 to the list:", the_list)

#5 insert()
the_list.insert(1, 133)
print("Inserting 133 at the first index:", the_list)

#6 extend(): adds other members of an iterable to end of a list
the_other_list = [343, 898, 959]
the_list.extend(the_other_list)
print("Adding the other list to the the the list's end by extend():", the_list)

#7 remove()
the_list.remove(898)
print("Removing 898 via remove() method:", the_list)