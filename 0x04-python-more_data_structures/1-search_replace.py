#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def func(elem):
        return (elem if elem != search else replace)
        
    return list(map(func, my_list))
