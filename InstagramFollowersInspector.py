"""
=== Instagram Followers Inspector ===
Find your followings who do not follow back

=== an original project by ===
Authors: Chenxu Robin Mao, Abdulrahman Mubarak
"""
import instaloader


def scrap_followers(ins_id: str, pswd: str, other = None) -> List[str]:
    """ 
    Returns a list contains the usernames of the <ins_id> followers
    
    Precondition: <ins_id> is an instagram account username
    
    """
    if not other:
        other = ins_id
    account = instaloader.Instaloader()
    account.login(ins_id, pswd)
    profile = instaloader.Profile.from_username(account.context, other)
    follows = profile.get_followers()
    lst = []
    for i in follows:
        lst.append(i.username)
    return lst


def scrap_followings(ins_id: str, pswd: str, other = None) -> List[str]:
    """ 
    Returns a list contains the usernames of the <ins_id> followings
    
    Precondition: <ins_id> is an instagram account username
    
    """
    if not other:
        other = ins_id
    account = instaloader.Instaloader()
    account.login(ins_id, pswd)
    profile = instaloader.Profile.from_username(account.context, other)
    follows_back = profile.get_followees()
    lst = []
    for i in follows_back:
        lst.append(i.username)
    return lst


def find_diff(follows_back: list[str], follows: list[str]) -> list[str]:
    """
    Retunrs a sorted list contains the usernames who you are in <follows>
    but not in <follows_back>
    
    """
    res = list(set(follows) - set(follows_back))
    return sorted(res)

if __name__ == '__main__':
    while True:
        print('\n')
        print('===Instagram Followers Inspector===')
        print('by Robin and Abdul, 2023.04.07.')
        print('robin.mao@mail.utoronto.ca, Abdulrahman.mubarak@mail.utoronto.ca')
        print('\n')
        print('Note that all log info are not recorded.')
        account_id = input('account_id: ')
        password = input('password: ')
        selforother = input(f'Are you retrieving data on yourself, {account_id}? (Y or N): ')

        if selforother.upper() == 'Y':
            print('\n')
            print('Retrieving data...Have some patient...This can take up to a minute...')
            follows = scrap_followers(account_id, password)
            follows_back = scrap_followings(account_id, password)
            diff = find_diff(follows, follows_back)
        elif selforother.upper() == 'N':
            target = input('target instagram id: ')
            print('\n')
            print('Retrieving data...Have some patient...')
            follows = scrap_followers(account_id, password, target)
            follows_back = scrap_followings(account_id, password, target)
            diff = find_diff(follows, follows_back)
        else:
            diff = None
            follows = None
            follows_back = None
            print('Input invalid.')
        if diff:
            print('\n')
            print('=== data retrieved ===')
            print(f'Here they are, the usernames of the {len(diff)} people who doesn\'t follow you back, boss:')
            print(diff)
        else:
            print('Data invalid, please check input. (Check account privacy)')
