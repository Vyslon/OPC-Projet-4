# -*- coding: UTF-8 -*-
def cat_into_cat_id(list_name, cat_list):
    if list_name in cat_list:
        return (cat_list.index(list_name))+1
    else:
        return 100
