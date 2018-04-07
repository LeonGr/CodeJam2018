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

# print(test_cases)

test_cases_lists = []

for i in range(0, len(test_cases), 2):
    integer_list = test_cases[i+1].split(" ")

    if not len(integer_list) == int(test_cases[i]):
        print('Error')

    test_cases_lists.append(integer_list)

def Trouble_Sort(array):
    # print('Sorting array', array)
    done = is_sorted(array)
    # print(done)
    if done is True:
        # print('Sorted at start')
        return 'OK'

    done = False

    while not done:
        done = True
        for i in range(len(array) - 2):
            # print("Checking:")
            # print(array[i:i+3])
            if array[i] > array[i+2]:
                done = False
                array[i], array[i+2] = array[i+2], array[i]
                # print("After swap:")
                # print(array[i:i+3])

    # print('Done')
    # print(array)
    result = is_sorted(array)
    if not result is True:
        # print('Error at ', result)
        return result

    return 'OK'


def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]): # i is the index of the previous element
            return i
    return True

for index, test_case in enumerate(test_cases_lists):
    result = Trouble_Sort(test_case)
    print('Case #' + str(index + 1) + ': ' + str(result))
