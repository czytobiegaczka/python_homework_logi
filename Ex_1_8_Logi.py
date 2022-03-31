from collections import defaultdict

id_to_logged_in_time = {}
id_to_login_times = defaultdict(list)
id_to_logout_times = defaultdict(list)

with open('logs.txt') as log_file:
    for line in log_file:
        username, operation, timestamp = line.split(';')
        prefix, user_id = username.split('-')
        user_id = int(user_id)

        if operation == 'LOGIN':
            id_to_login_times[user_id].append(int(timestamp))
        elif operation == 'LOGOUT':
            id_to_logout_times[user_id].append(int(timestamp))

for id in id_to_login_times:
    logged_in_time_for_user = 0
    if len(id_to_login_times) != len(id_to_logout_times):
        print(f"Nieprawidłowe dane w pliku. Różna ilość LOGIN i LOGOUT: {len(id_to_login_times)} != {len(id_to_logout_times)}")
        break

    for login, logout in zip(id_to_login_times[id], id_to_logout_times[id]):
        if login > logout:
            print(f'Nieprawidłowe dane wejściowe w pliku dla: user-{id}. Logout: {logout}, Login: {login}')
            break

        logged_in_time_for_user += logout - login

    id_to_logged_in_time[id] = logged_in_time_for_user

for id in sorted(id_to_logged_in_time.keys()):
    print(f'user-{id:2}: {id_to_logged_in_time[id]:5} s')
