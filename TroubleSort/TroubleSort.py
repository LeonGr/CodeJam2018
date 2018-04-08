test_input = '''
2
5
5 6 8 4 3
3
8 9 7
'''

# lines = test_input.splitlines()

test_cases = []

t = int(input()) # read a line with a single integer
for i in range(1, t * 2 + 1):
  line = input()
  test_cases.append(line)

#print('Test cases')
#print(test_cases)

test_cases_lists = []

for i in range(0, len(test_cases), 2):
    string_list = test_cases[i+1].split(" ")

    integer_list = list(map(int, string_list))

    # if not len(integer_list) == int(test_cases[i]):
        #print('Error')

    test_cases_lists.append(integer_list)

def Trouble_Sort(array):
    #print('Sorting array', array)
    done = is_sorted(array)
    #print(done)
    if done is True:
        #print('Sorted at start')
        return 'OK'

    done = False

    while not done:
        done = True
        for i in range(len(array) - 2):
            #print("Checking:")
            #print(array[i:i+3])
            if array[i] > array[i+2]:
                done = False
                array[i], array[i+2] = array[i+2], array[i]
                #print("After swap:")
                #print(array[i:i+3])

    #print('Done')
    #print(array)

    for i in range(0, len(array) - 1):
        if array[i] > array[i+1]:
            #print('Error at ', i)
            return i

    return 'OK'


def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]): # i is the index of the previous element
            return i
    return True

for index, test_case in enumerate(test_cases_lists):
    result = Trouble_Sort(test_case)
    print("Case #{}: {}".format(index + 1, result))
