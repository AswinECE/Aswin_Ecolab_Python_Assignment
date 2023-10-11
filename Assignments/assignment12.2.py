def supress_exception(exception = KeyError, result = False):
    def dummy_return(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if result is not None:
                    return result
                else:
                    raise e
        return inner
    return dummy_return

users = {'ASWIN S': 'aswintbe@gmail.com', 'SKPA':'ABCD' }
@supress_exception(KeyError, result=False)

def authenticate(user, password):
    print(f'Authenticating {user}')
    return users.get(user) == password

result = authenticate('ASWIN S', 'aswintbe@gmail.com')
print("Authentication:", result)
