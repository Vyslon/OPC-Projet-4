# -*- coding: UTF-8 -*-
def cat_into_cat_id(str, list):
    if str in list:
        return list.index(str)
    else:
        return -1
