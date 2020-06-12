class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = dict()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users[user] = None

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def is_user_in_group(user, group, result=None):
        if result is not None:
            return result

        if user in group.get_users():
            return True

        for subgroup in group.get_groups():
            result = is_user_in_group(user, subgroup)
            if result:
                return result

        return False

if __name__ == '__main__':
    def test_case1():
        print("\ntest case 1..  Edge case")
        g0 = Group("Group 0")    
        g1 = Group("Group 1")
        g2 = Group("Group 2")

        print(is_user_in_group('user0' , g0))    #False
        print(is_user_in_group('user0' , g1))    #False
        print(is_user_in_group('user0' , g2))    #False
    
    def test_case2():
        print("\ntest case2..   Edge case")
        g0 = Group("Group 0")
        g1 = Group("Group 1")
        g2 = Group("Group 2")  
        g1.add_user("user0")

        g1.add_group(g2)
        g0.add_group(g1)
        """
    
                     Group0
                        |
                       Group 1
                      ___|__
                      |     |
                 user 0   Group 2
        """

        print(is_user_in_group("user0", g0))     #True
        print(is_user_in_group("user0", g1))     #True
        print(is_user_in_group("user0", g2))     #False
    

    def test_case3():
        print("\ntest case 3..")
        g0 = Group("Group 0")
        g1 = Group("Group 1")
        g2 = Group("Group 2")
        g2.add_user('user1')
        g1.add_group(g2)
        g0.add_group(g1)

        """
                Group 0
                   |
                Group 1
                   |
                Group 2
                   |
                 user1 
        """

        print(is_user_in_group('user1', g0))     # True
        print(is_user_in_group('user1', g1))     # True
        print(is_user_in_group('user1', g2))     # True
    


    test_case1()
    test_case2()
    test_case3()
