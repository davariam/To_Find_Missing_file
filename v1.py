import fnmatch
import re
import os
ep_file_list = []
ep_list = ['ep1f','ep2f','ep3f','ep4f']

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, 'ep*.txt'):
        ep_file_list.append(file)

cbp = list(range(1,13,1))
z = 0

for item in cbp:
    cbp[z] = str(item)
    z = z+1

for item_name in ep_file_list:
    file_list = open(item_name, "r")

    file_result= re.search(r"^.*cm_credit_limit_in.txt$",item_name)
    if file_result:
        list_final_file = []

        f = open(item_name,"r")
        text = f.readlines()
        f.close
        for index,item in enumerate(text):
            result = re.search(r"cm_credit_limit_accm.*",item)
            result2 = re.search(r"cm_credit_limit_value.*",item)

            if result or result2:
                list_final_file.append(index)

        for list_item in reversed(list_final_file):
           del text[int(list_item)]
        new_file = open(item_name,"w+")
        for line in text:
            new_file.write(line)
        new_file.close()



    cbp_list = []

    for item in file_list:
        z = 0
        for item_in_item in item:
            if item_in_item.isdigit():
                if item[z + 1].isdigit():
                    cbp_number = item[z]
                    cbp_number = cbp_number + item[z + 1]
                    cbp_list.append(cbp_number)
                    break
                else:
                    cbp_number = item[z]
                    cbp_list.append(cbp_number)
                    break
            z = z+1
    file_list.close()

    with open(item_name) as f:
        first_line = f.readline()
    f.close()

    for index, item in enumerate(first_line):

        if item.isdigit():
            Index_list = index
            break

    not_existed = list(set(cbp) - set(cbp_list))
    if ep_list[0] == item_name[0:4]:
        for item in not_existed:
            print(first_line[0:Index_list-3]+" file is missing in: cbp" + item )
    elif ep_list[1] == item_name[0:4]:
        for item in not_existed:
            print(first_line[0:Index_list-4]+" file is missing in: mcbp" + item )
    elif ep_list[2] == item_name[0:4]:
        for item in not_existed:
            print(first_line[0:Index_list-4]+" file is missing in: scbp" + item )
    elif ep_list[3] == item_name[0:4]:
        for item in not_existed:
            print(first_line[0:Index_list-4]+" file is missing in: tcbp" + item )
