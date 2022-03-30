id_to_logged_in_time = {}
id_to_login_times = {}
id_to_logout_times = {}

with open('logs.txt') as log_file:
    for line in log_file:
        username, operation, timestamp = line.split(';')
        prefix, user_id = username.split('-')
        user_id = int(user_id)

        if operation == 'LOGIN':
            if user_id not in id_to_login_times:
                id_to_login_times[user_id] = []
            id_to_login_times[user_id].append(int(timestamp))

        elif operation == 'LOGOUT':
            if user_id not in id_to_logout_times:
                id_to_logout_times[user_id] = []
            id_to_logout_times[user_id].append(int(timestamp))


for id in id_to_login_times.keys():
    logged_in_time_for_user = 0

    assert len(id_to_login_times) == len(id_to_logout_times), \
        f"There needs to be the same amount of logins as logouts {len(id_to_login_times)} != {len(id_to_logout_times)} for given user: {id}"

    for login, logout in zip(id_to_login_times[id], id_to_logout_times[id]):
        assert logout > login, "Invalid entries in file"
        logged_in_time_for_user += logout - login
    id_to_logged_in_time[id] = logged_in_time_for_user

for id in sorted(id_to_logged_in_time.keys()):
    print(f'user-{id:2}: {id_to_logged_in_time[id]:5} s')
