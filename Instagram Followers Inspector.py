"""
=== Instagram Followers Inspector ===
Find your followings who do not follow back

=== an original project by ===
Authors: Chenxu Robin Mao, Abdulrahman Mubarak
"""
import pyautogui as pg
import instaloader
import pandas as pd

def scrap_followers_for_self(id, pswd):
    account = instaloader.Instaloader()
    account.login(id, pswd)
    profile = instaloader.Profile.from_username(account.context, id)
    followers = profile.get_followers()
    lst = []
    for i in followers:
        lst.append(i.username)
    return lst

def scrap_followings_for_self(id, pswd):
    account = instaloader.Instaloader()
    account.login(id, pswd)
    profile = instaloader.Profile.from_username(account.context, id)
    followers = profile.get_followees()
    lst = []
    for i in followers:
        lst.append(i.username)
    return lst

def scrap_followers_for_others(id, pswd, other):
    account = instaloader.Instaloader()
    account.login(id, pswd)
    profile = instaloader.Profile.from_username(account.context, other)
    followers = profile.get_followers()
    lst = []
    for i in followers:
        lst.append(i.username)
    return lst

def scrap_followings_for_others(id, pswd, other):
    account = instaloader.Instaloader()
    account.login(id, pswd)
    profile = instaloader.Profile.from_username(account.context, other)
    followers = profile.get_followees()
    lst = []
    for i in followers:
        lst.append(i.username)
    return lst

def find_diff(followings, followers):
    """Find followings that are not in followers."""
    res = []
    for i in followings:
        if i not in followers:
            res.append(i)
        pass
    return res

if __name__ == '__main__':
    print('\n')
    print('===Instagram Followers Inspector===')
    print('Robin and Abdul, 2023.04.07.')
    print('robin.mao@mail.utoronto.ca, Abdulrahman.mubarak@mail.utoronto.ca')
    print('\n')
    print('Note that all log info are not recorded.')
    account_id = input('account id: ')
    password = input('password: ')
    selforother = input(f'Are you retrieving data on yourself, {account_id}? (Y or N): ')

    if selforother == 'Y':
        print('\n')
        print('Retrieving data...Have some patient...')
        followers = scrap_followers_for_self(account_id, password)
        followings = scrap_followings_for_self(account_id, password)
        diff = find_diff(followings, followers)

    elif selforother == 'N':
        target = input('target instagram id: ')
        print('\n')
        print('Retrieving data...Have some patient...')
        followers = scrap_followers_for_others(account_id, password, target)
        followings = scrap_followings_for_others(account_id, password, target)
        diff = find_diff(followings, followers)

    else:
        diff = None
        print('Input invalid.')

    if diff:
        print('\n')
        print('=== data retrieved ===')
        print('Here they are, the usernames of people who doesn\'t follow you back, boss:')
        print(diff)
    else:
        print('Data invalid, please check input. (Check account privacy)')