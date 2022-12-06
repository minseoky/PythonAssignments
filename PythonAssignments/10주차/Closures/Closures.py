#32194579 최민석
def has_permission(page):
    def inner(username):
        if (page == 'Admin Area' and username == 'Admin'):
            return 'Admin does have access to Admin Area'
        else:
            return 'TestUserdoes NOT have access to Admin Area'
    return inner

func = has_permission('Admin Area')
print(func('Admin'))
print(func('Tester'))
func1 = has_permission('Other_Area')
print(func1('Admin'))
print(func1('Tester'))