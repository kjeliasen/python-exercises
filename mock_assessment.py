def normalize_name(target_name):
    valid_chars = 'abcdefghijklmnopqrstuvwxyz0123456789_ '
    in_process_name = target_name.lower()
    name_list = []
    new_name = ''
    for test in in_process_name:
        if test in valid_chars:
            name_list.append(test)
    new_name = ''.join(name_list).strip().replace(' ','_')
    #if new_name == target_name:
    #    print('No change needed to [{}]'.format(target_name))
    #else:
    #    print('[{}] becomes [{}]'.format(target_name,new_name))
    return new_name


def cumsum(list):
    runsum = 0
    sumrun = []
    for item in list:
        runsum = runsum + item
        sumrun.append(runsum)
    return sumrun  

