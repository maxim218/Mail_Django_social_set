from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.authorization, name='authorization'),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^reg_user/', views.reg_user, name='reg_user'),
    url(r'^callback/', views.callback, name='callback'),
    url(r'^auth_user/', views.auth_user, name='auth_user'),
    url(r'^my_page/', views.my_page, name='my_page'),
    url(r'^normal_user/', views.normal_user, name='normal_user'),
    url(r'^set_new_user_properties/', views.set_new_user_properties, name='set_new_user_properties'),
    url(r'^get_user_properties/', views.get_user_properties, name='get_user_properties'),
    url(r'^go_out_of_session/', views.go_out_of_session, name='go_out_of_session'),
    url(r'^add_record/', views.add_record, name='add_record'),
    url(r'^get_user_records/', views.get_user_records, name='get_user_records'),
    url(r'^users_list/', views.users_list, name='users_list'),
    url(r'^get_list_of_users/', views.get_list_of_users, name='get_list_of_users'),
    url(r'^watch_user/', views.watch_user, name='watch_user'),
    url(r'^get_name_and_sername_of_user/', views.get_name_and_sername_of_user, name='get_name_and_sername_of_user'),
    url(r'^get_records_of_user/', views.get_records_of_user, name='get_records_of_user'),
    url(r'^discuss_forums/', views.discuss_forums, name='discuss_forums'),
    url(r'^add_discuss_theme_to_db/', views.add_discuss_theme_to_db, name='add_discuss_theme_to_db'),
    url(r'^get_list_of_all_themas/', views.get_list_of_all_themas, name='get_list_of_all_themas'),
    url(r'^comment_theme/', views.comment_theme, name='comment_theme'),
    url(r'^get_all_comments_of_the_theme/', views.get_all_comments_of_the_theme, name='get_all_comments_of_the_theme'),
]
