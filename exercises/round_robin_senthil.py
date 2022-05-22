

def required_time(queue_list,position):
    ret_time = 0
    required_ticket = queue_list[position]
    new_list = list(queue_list)
    new_position = position
    print('Req ticket : %d'%required_ticket)
    goto_queue = True
    while goto_queue:
        current_ticket = new_list[0] - 1
        print('Curernt ticket : %d'%current_ticket)
        ret_time = ret_time + 1
        if new_position == 0:
            required_ticket = current_ticket
            if required_ticket == 0:
                goto_queue = False
            else:
                new_position = len(new_list)
        new_list = list(new_list[1:])
        #print(type(new_list))
        #print('New list before apending : %s'%new_list)
        if current_ticket != 0:
            new_list.append(current_ticket)
            #print(type(new_list))
            # new_position = len(new_list)
            print('list : %s'%new_list)
        new_position = new_position - 1
        print('required : %d'%required_ticket)
        print('position : %d'%new_position)
        print('ret time : %d'%ret_time)
    print(ret_time)


a = [1,2,3,4,5]
required_time(a,4)