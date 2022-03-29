user_time = {}
with open('logs.txt', mode='r', encoding='utf-8') as log_file:
    for line in log_file:
        info = line.split(';')
        if info[0] in user_time:
            if info[1] == 'LOGIN':
                user_time[info[0]][0] = int(info[2])
            else:
                user_time[info[0]][1] += (int(info[2]) - user_time[info[0]][0])
        else:
            user_time[info[0]] = [int(info[2]), 0]

sort_user_time = sorted(user_time.items())
for user, time in sort_user_time:
    print(f' - {user:8}: {time[1]} s')
