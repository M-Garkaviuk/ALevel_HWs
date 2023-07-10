filename = 'Lesson_3_Numbers.txt'
with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        numbers = list(map(int, line.split()))
        # fizz = numbers[0]
        # buzz = numbers[1]
        # n = numbers[2]
        shag = range(1, numbers[2]+1)

        result_list_temp = [(y, i) for y, i in enumerate(shag, 0) if i % numbers[0] == 0 and i % numbers[1] == 0                                                              
                       ]
        print(result_list_temp)

        # result_list_temp1 = ("F" if i % numbers[0] == 0 else "B" for i in result_list_temp if i != "FB" and i % numbers[1] == 0)
        # print(str(result_list_temp1))
        # # result_list_final = [y for y in result_list_temp if y =! "FB"] 
        # shag = range(1, n+1)
        # for i in shag:
        #     if i % fizz == 0 and i % buzz == 0:
        #         result_list.append('FB')
        #     elif i % fizz == 0:
        #         result_list.append('F')
        #     elif i % buzz == 0:
        #         result_list.append('B')
#         #     else: result_list.append(str(i))
# formated_result = ", ".join(str(result_list_temp)) 
# formated_result1 = ", ".join(str(result_list_temp1))
            # print(result_list)  
f.close()
# with open ('new.txt', 'w') as file:
#     file.write(str(formated_result))
# file.close()