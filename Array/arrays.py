import  array as arr

# storing String in a python array
a = arr.array('b');
a.frombytes('hi'.encode());
a=a.tobytes().decode();
print(a);

# Array operations
numbers = arr.array('i', [2,4,6,8])
print(numbers);
print("Second Element : ", numbers[1]);

numbers.append(10);                           #0(1)
print("After Appending : ", numbers);

numbers.extend([12,14,16])                    #0(1)
print("After Extending : ", numbers);

numbers.insert(2,5);                          #0(n)
print("After Inserting : ", numbers);

numbers.remove(5);                            #0(n)
print("After Removing : ", numbers);

numbers.pop(3);                               #0(n)
print("After Pop : ", numbers);