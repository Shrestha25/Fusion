from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from applications.gymkhana.api.views import clubname,Club_Details
from . import views
from rest_framework.authtoken.views import obtain_auth_token



app_name = 'gymkhana'

urlpatterns = [
    #academic administration
    url(r'^club_approve/$', views.club_approve, name='club_approve'),
    url(r'^club_reject/$', views.club_reject, name='club_reject'),
    # This is post method which takes username and password to generates/return Token
    url(r'^login/$', obtain_auth_token, name='login'),
    # api for "clubdetails" method="get" with TokenAuthentication
    url(r'^clubdetails/$', Club_Details.as_view()),
    # api for "clubname" method="get" with TokenAuthentication
    url(r'^clubname/$', clubname.as_view()),
    url(r'^$', views.gymkhana, name='gymkhana'),
    url(r'^delete_requests/$', views.delete_requests, name='delete_requests'),
    url(r'^form_avail/$', views.form_avail, name='form_avail'),
    url(r'^registration_form/$', views.registration_form, name='registration_form'),
    url(r'^new_club/$', views.new_club, name='new_club'),

    #club_head 
    url(r'^approve/$', views.approve, name='approve'),
    url(r'^reject/$', views.reject, name='reject'),
    url(r'^cancel/$', views.cancel, name='cancel'),
    url(r'^new_event/$', views.new_event, name='new_event'),
    url(r'^new_session/$', views.new_session, name='new_session'),
    url(r'^event_report/$', views.event_report, name='event_report'),
    url(r'^club_event_report/$', views.club_report, name='club_report'),
    url(r'^change_head/$', views.change_head, name='change_head'),
    url(r'^club_budget/$', views.club_budget, name='club_budget'),
    url(r'^act_calender/$', views.act_calender, name='act_calender'),
    url(r'^date_sessions/$', views.date_sessions, name='date_sessions'),
    url(r'^date_events/$', views.date_events, name='date_events'),
    url(r'^delete_sessions/$', views.delete_sessions, name='delete_sessions'),
    url(r'^delete_events/$', views.delete_events, name='delete_events'),
    url(r'^(?P<event_id>\d+)/edit_event/$', views.edit_event, name='edit_event'),
    url(r'^(?P<session_id>\d+)/editsession/$', views.editsession, name='editsession'),
    url(r'^delete_memberform/$', views.delete_memberform, name='delete_memberform'),
    url(r'^voting_poll/$', views.voting_poll, name='voting_poll'),
    url(r'^delete_poll/(?P<poll_id>\d+)/$', views.delete_poll, name='delete_poll'),

    #student
    url(r'^registration_form/$', views.registration_form, name='registration_form'),
    url(r'^delete_requests/$', views.delete_requests, name='delete_requests'),
    url(r'^club_membership/$', views.club_membership, name='membership'),
    url(r'^(?P<poll_id>\d+)/$', views.vote, name='vote'),
    url(r'^$', views.gymkhana, name='gymkhana'),

    #data recieving
    url(r'^form_avail/$', views.form_avail, name='form_avail'),
    url(r'^faculty_data/$', views.facultyData, name='faculty_data'),
    url(r'^students_data/$', views.studentsData, name='students_data'),
    url(r'^get_venue/$', views.getVenue, name='get_venue'),

    #core_team
    url(r'^core_team/$', views.core_team, name='core_team'),
    url(r'^festbudget/$', views.fest_budget, name='fest_budget'),
   
]

