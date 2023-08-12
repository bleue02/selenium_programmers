def get_login_option(option):
    programmers, Google, Kakao, GitHub, Facebook = text_color()
    if option == 1:
        return f"If you have a {programmers} account, please press 1"
    elif option == 2:
        return f"If you do not have a {programmers} account, please press 2"
    elif option == 3:
        return f"Press 3 to log in with your {Google} account"
    elif option == 4:
        return f"Press 4 to log in with your {Kakao} account"
    elif option == 5:
        return f"Press 5 to log in with your {GitHub} account"
    elif option == 6:
        return f"Press 6 to log in with your {Facebook} account"
    else:
        return "Invalid login option."

def text_color():
    programmers = '\033[35m"P\033[0m\033[35mr\033[0m\033[35mo\033[0m\033[35mg\033[0m\033[35mr\033[0m\033[35ma\033[0m\033[35mm\033[0m\033[35me"\033[0m'
    Google = '\033[34m"G\033[0m\033[31mo\033[0m\033[33mo\033[0m\033[34mg\033[0m\033[32ml\033[0m\033[31me"\033[0m'
    Kakao = '\033[33m"Kakao"\033[0m'
    GitHub = '\033[30m"GitHub"\033[0m'
    Facebook = '\033[34m"F\033[0m\033[34ma\033[0m\033[34mc\033[0m\033[34me\033[0m\033[34mb\033[0m\033[34mo\033[0m\033[34mo\033[0m\033[34mk"\033[0m'
    return programmers, Google, Kakao, GitHub, Facebook

def login_info_xpath(user_select):
    if user_select == 1:
        return {
            '1_Id_Box': '/html/body/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/input',
            '1_Pswd_Box': '/html/body/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[4]/input',
            '1_Submit_Box': '/html/body/div/div/div[2]/div/div[2]/div[1]/div/div[2]/button'
        }
    elif user_select == 2:
        return {
            '2_Id_Box': '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input',
            '2_Pswd_Box': '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input',
            '2_Submit_Box': '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'
        }

    elif user_select == 4:
        return {
            '4_Id_Box': '/html/body/div/div/div/main/article/div/div/form/div[1]/div/input',
            '4_Pswd_Box': '/html/body/div/div/div/main/article/div/div/form/div[2]/div/input',
            '4_Submit_Box': '/html/body/div[1]/div/div/main/article/div/div/form/div[4]/button[1]'
        }
    elif user_select == 5:
        return {
            '5_Id_Box': '/html/body/div[1]/div[3]/main/div/div[3]/form/input[2]',
            '5_Pswd_Box': '/html/body/div[1]/div[3]/main/div/div[3]/form/div/input[1]',
            '5_Submit_Box': '/html/body/div[1]/div[3]/main/div/div[3]/form/div/input[13]'
        }
    elif user_select == 6:
        return {
            '6_Id_Box': '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input',
            '6_Pswd_Box': '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input',
            '6_Submit_Box': '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button'
        }
    else:
        return None


def login_info(user_select):
    return {
        '1': 'https://programmers.co.kr/account/sign_in',
        '2': 'https://programmers.co.kr/account/sign_up',
        # '3': 'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?response_type=code&client_id=697220841411-gonnvfdbvgnlut7mhb81buraqh61fj50.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprogrammers.co.kr%2Fusers%2Fauth%2Fgoogle%2Fcallback&state=a1b36798c479e0ae6c88d4bb4aef6d4b932a6895e76b3005&scope=email&access_type=offline&service=lso&o2v=1&flowName=GeneralOAuthFlow',
        '4': 'https://accounts.kakao.com/login/?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fprogrammers.co.kr%252Fusers%252Fauth%252Fkakao%252Fcallback%26state%3Da33ab1f12dc05347f92feb1226f561690f9589135bd5bf4a%26scope%255B%255D%3Daccount_email%26through_account%3Dtrue%26client_id%3Dab64d75703ee3d2f08f4c2e0ffe1dee7#webTalkLogin',
        '5': 'https://github.com/login?client_id=25a33d959e956122e7c2&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D25a33d959e956122e7c2%26redirect_uri%3Dhttps%253A%252F%252Fprogrammers.co.kr%252Fusers%252Fauth%252Fgithub%252Fcallback%26response_type%3Dcode%26scope%3Duser%253Aemail%252Cread%253Aorg%252Cread%253Auser%26state%3Dac338d362977d311fadbc1a1a543bb2c3805ac49527d5e33',
        '6': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=339079816467879&kid_directed_site=0&app_id=339079816467879&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D339079816467879%26redirect_uri%3Dhttps%253A%252F%252Fprogrammers.co.kr%252Fusers%252Fauth%252Ffacebook%252Fcallback%26state%3Dc76bfd3caab07bee76da98bd9d3c387c69b6410823b19ce6%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7b5f2a61-85c6-4021-9f89-ad57dbfeaeb2%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fprogrammers.co.kr%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=ko_KR&pl_dbl=0&refsrc=deprecated&_rdr'
    }.get(user_select, None)

def login_google_info():
    return {'3': 'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?response_type=code&client_id=697220841411-gonnvfdbvgnlut7mhb81buraqh61fj50.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprogrammers.co.kr%2Fusers%2Fauth%2Fgoogle%2Fcallback&state=a1b36798c479e0ae6c88d4bb4aef6d4b932a6895e76b3005&scope=email&access_type=offline&service=lso&o2v=1&flowName=GeneralOAuthFlow',}

def login_info_google_xpath():
    return {
        'google_Id_Box': '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]',
        'google_Submit_Box': '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'
    }
