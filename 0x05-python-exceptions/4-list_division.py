#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    el = 0
    for i in range(list_length):
        try:
            el = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result.append(el)
            el = 0

    return result
