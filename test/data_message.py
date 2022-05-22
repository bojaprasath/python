#!/usr/bin/env python
# -*- coding: utf-8 -*-

def chunkstring(string, length):
    return (string[0 + i:length + i] for i in range(0, len(string), length))

def split_message(message):
    split_messages = []
    msg_backup = message
    msg_index = 0
    buffer_msg = ""
    i = 0
    import pdb;
    # pdb.set_trace()
    while len(message) > 4000:
        i = i + 1
        split_index = message[:4000].rfind('-  test')
        if split_index == 0:
            split_index = message.find('-  test')
        send_msg=message[msg_index:split_index]
        message=message[split_index:]
        print("Iteraton : %d , Length : %d" % (i, len(send_msg)))
        return message,data



print('done')
file='/Users/seveluch/Documents/python/test/message_data.txt'
import re
f = open(file,'r')
data=f.read()
print(data)
print('######')
split_message(data)