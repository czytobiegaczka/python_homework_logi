# TODO: Add validation (multiple logins or logouts in the row, 
# logouts before logins, logouts without logins and the other way around)
def calculate_logged_in_time_for_users(file):
    id_to_logged_in_time = {}
    id_to_login_times = {}
    id_to_logout_times = {}

    for line in file:
        """
            Jezeli wiemy ile elementow ma tablica albo tuple 
            mozemy rozbic go przy zapisywaniu np.:
            ``` 
            t = (1, 2)
            one, two = t
            ```
            to `one`` bedzie rowne 1 a `two`` 2
        """
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
        # `assert` sprawdza czy warunek jest spelniony jezeli nie wyrzuca blad
        assert len(id_to_login_times) == len(id_to_logout_times),\
            f"There needs to be the same amount of logins as logouts {len(id_to_login_times)} != {len(id_to_logout_times)} for given user: {id}"
        
        """
            `zip` bierze dwa ciagi wartosci i sklada je w taki sposob ze jezeli:
            ```
            a = [1,2,3]
            b = ['a','b','c']
            ```
            to
            `zip(a,b)` bedzie rowny [(1,'a'), (2,'b'), (3,'c')]
        """
        for login, logout in zip(id_to_login_times[id], id_to_logout_times[id]):
            assert logout > login, "Invalid entries in file"
            logged_in_time_for_user += logout - login
        id_to_logged_in_time[id] = logged_in_time_for_user

    return id_to_logged_in_time


if __name__ == '__main__':
    # `sys.argv` zawiera nazwe uruchomionego pliku i podane w konsoli argumenty
    # path = sys.argv[1] if len(sys.argv) == 2 else "logs.txt"
    path = "logs.txt"
    with open(path) as log_file:
        id_to_logged_in_time = calculate_logged_in_time_for_users(log_file)

    for id in sorted(id_to_logged_in_time.keys()):
        print(f'user-{id}: {id_to_logged_in_time[id]}s')
