#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            try:
                div_result = dividend / divisor
                if type(div_result) not in (int, float):
                    raise TypeError("wrong type")
            except ZeroDivisionError:
                div_result = 0
                print("division by 0")
            except TypeError:
                div_result = 0
                print("wrong type")
        except IndexError as e:
            print(e)
            break
        else:
            result.append(div_result)
        finally:
            return (result)
