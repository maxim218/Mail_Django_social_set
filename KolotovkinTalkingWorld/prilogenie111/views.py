from django.shortcuts import render
from django.http import HttpResponse
from .models import MyUsers
from .models import MyUsersInfo
from .models import MyRecords
from .models import MyTheme
from django.http import HttpResponseRedirect

def authorization(request):
    return render(request, 'prilogenie111/authorization.html', {})

def registration(request):
    return render(request, 'prilogenie111/registration.html', {})

def auth_user(request):
    a = str(request.POST['a'])
    b = str(request.POST['b'])
    my_records_arr = MyUsers.objects.filter(user_login=a, user_password=b)
    if len(my_records_arr) > 0:
        # AUTH_YES
        request.session["userLogin"] = a
        request.session["userPassword"] = b
        return HttpResponseRedirect("/my_page")
    else:
        # AUTH_NO
        return HttpResponseRedirect("/callback/auth_no")

def reg_user(request):
    a = str(request.POST['a'])
    b = str(request.POST['b'])

    my_records_arr = MyUsers.objects.filter(user_login=a)
    if len(my_records_arr) > 0:
        # REG_NO
        return HttpResponseRedirect("/callback/reg_no")
    else:
        # REG_YES
        MyUsers.objects.create(user_login=a, user_password=b)
        return HttpResponseRedirect("/callback/reg_yes")

def callback(request):
    return render(request, 'prilogenie111/callback.html', {})

def my_page(request):
    return render(request, 'prilogenie111/my_page.html', {})


def normal_user(request):
    if ("userLogin" in request.session) == False:
        print("False: no login")
        return HttpResponse(str("false"))

    if ("userPassword" in request.session) == False:
        print("False: no password")
        return HttpResponse(str("false"))

    a = str(request.session["userLogin"])
    b = str(request.session["userPassword"])

    my_records_arr = MyUsers.objects.filter(user_login=a, user_password=b)
    if len(my_records_arr) > 0:
        print("True: login and password OK")
        return HttpResponse(str("true"))
    else:
        print("False: no correct pair login and password")
        return HttpResponse(str("false"))

def control_user(request):
    if ("userLogin" in request.session) == False:
        print("False: no login")
        return False

    if ("userPassword" in request.session) == False:
        print("False: no password")
        return False

    a = str(request.session["userLogin"])
    b = str(request.session["userPassword"])

    my_records_arr = MyUsers.objects.filter(user_login=a, user_password=b)
    if len(my_records_arr) > 0:
        print("True: login and password OK")
        return True
    else:
        print("False: no correct pair login and password")
        return False

def set_new_user_properties(request):
    flag = control_user(request)
    if flag == False:
        return HttpResponseRedirect("/callback/auth_no")

    user_login = str(request.session["userLogin"])
    user_s1 = str(request.POST['t1'])
    user_s2 = str(request.POST['t2'])
    user_s3 = str(request.POST['t3'])

    my_records_arr = MyUsersInfo.objects.filter(user_login=user_login)
    if len(my_records_arr) == 0:
        MyUsersInfo.objects.create(user_login=user_login, user_s1=user_s1, user_s2=user_s2, user_s3="XXXXX")
    else:
        MyUsersInfo.objects.filter(user_login=user_login).update(user_login=user_login, user_s1=user_s1, user_s2=user_s2, user_s3="XXXXX")

    return HttpResponseRedirect("/callback/change_user_properties")

def get_user_properties(request):
    flag = control_user(request)
    if flag == False:
        return HttpResponseRedirect("/callback/auth_no")

    user_login = str(request.session["userLogin"])
    my_records_arr = MyUsersInfo.objects.filter(user_login=user_login)
    record = my_records_arr[0]
    answer = record.user_s1 + "@@@@@@~~~~~~" + record.user_s2
    return HttpResponse(str(answer))

def go_out_of_session(request):
    request.session["userLogin"] = "~~@@~~@@~~@@~~@@==="
    request.session["userPassword"] = "~~@@~~@@~~@@~~@@==="
    return HttpResponse(str("GO_OUT"))

def add_record(request):
    flag = control_user(request)
    if flag == False:
        return HttpResponseRedirect("/callback/auth_no")

    user_login = str(request.session["userLogin"])
    user_record = str(request.POST['tttt'])

    MyRecords.objects.create(user_login=user_login, user_record=user_record)
    return HttpResponseRedirect("/callback/add_record")

def get_user_records(request):
    flag = control_user(request)
    if flag == False:
        return HttpResponseRedirect("/callback/auth_no")

    user_login = str(request.session["userLogin"])

    my_records_arr = MyRecords.objects.filter(user_login=user_login).order_by('pk')
    my_records_arr = my_records_arr.reverse()


    answer_str = ""
    for xxx in my_records_arr:
        answer_str = answer_str + xxx.user_record + "~~@@~~@@~~@@~~@@==="

    return HttpResponse(str(answer_str))


def users_list(request):
    return render(request, 'prilogenie111/users_list.html', {})

def watch_user(request):
    return render(request, 'prilogenie111/watch_user.html', {})

def get_list_of_users(request):
    flag = control_user(request)
    if flag == False:
        return HttpResponseRedirect("/callback/auth_no")

    my_records_arr = MyUsers.objects.order_by('user_login')
    big_string = ""
    for xxx in my_records_arr:
        big_string = big_string + str(xxx.user_login) + "~~@@~~@@~~@@~~@@==="

    return HttpResponse(str(big_string))


def get_name_and_sername_of_user(request):
    flag = control_user(request)
    if flag == False:
        return HttpResponseRedirect("/callback/auth_no")

    user_login = str(request.GET['login_login'])

    my_records_arr = MyUsersInfo.objects.filter(user_login=user_login)
    record = my_records_arr[0]
    answer = record.user_s1 + "@@@@@@~~~~~~" + record.user_s2
    return HttpResponse(str(answer))


def get_records_of_user(request):
    flag = control_user(request)
    if flag == False:
        return HttpResponseRedirect("/callback/auth_no")

    user_login = str(request.GET['login_login'])

    my_records_arr = MyRecords.objects.filter(user_login=user_login).order_by('pk')
    my_records_arr = my_records_arr.reverse()

    answer_str = ""
    for xxx in my_records_arr:
        answer_str = answer_str + xxx.user_record + "~~@@~~@@~~@@~~@@==="

    return HttpResponse(str(answer_str))

def discuss_forums(request):
    return render(request, 'prilogenie111/discuss_forums.html', {})

def add_discuss_theme_to_db(request):
    flag = control_user(request)
    if flag == False:
        return HttpResponseRedirect("/callback/auth_no")

    user_login = str(request.session["userLogin"])
    theme_text = str(request.POST['tttt'])

    MyTheme.objects.create(user_login=user_login, theme_text=theme_text)
    return HttpResponseRedirect("/callback/create_theme_ok")

def get_list_of_all_themas(request):
    flag = control_user(request)
    if flag == False:
        return HttpResponseRedirect("/callback/auth_no")

    my_records_arr = MyTheme.objects.order_by('pk')
    my_records_arr = my_records_arr.reverse()

    answer_str = ""
    for xxx in my_records_arr:
        if len(xxx.theme_text) > 0:
            answer_str = answer_str + (str(xxx.pk) + "------~~~~~~-~-~-~--" + "Пользователь " + xxx.user_login + "---@@@@@~~~~~~~~~~~@-@-@@@-@@@@-----") + xxx.theme_text + "~~@@~~@@~~@@~~@@==="

    return HttpResponse(str(answer_str))

def comment_theme(request):
    return render(request, 'prilogenie111/comment_theme.html', {})

def get_all_comments_of_the_theme(request):
    flag = control_user(request)
    if flag == False:
        return HttpResponseRedirect("/callback/auth_no")

    theme_number = int(request.GET['theme_number'])

    themes = MyTheme.objects.filter(pk=theme_number)
    theme = themes[0]
    user_login = str(theme.user_login)
    theme_text = str(theme.theme_text)

    result_string = user_login + "------~~~~~~-~-~-~--" + theme_text + "------~~~~~~-~-~-~--"

    return HttpResponse(str(result_string))