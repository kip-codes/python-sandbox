# File: user_profile
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 11/11/2017 at 4:06 PM
#
# For inquiries about the file please contact the author.


def build_profile(first, last, **user_info):
    #Build a dictionary containing everything we know about a user.
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

if __name__ == '__main__':
    user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
    print(user_profile)


    myProfile = build_profile('kevin', 'ip', clan='otaku', lazy='yes', cat='fat')
    print(myProfile)