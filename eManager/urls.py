from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'emanager'

urlpatterns = [
	# Events
	url(r'^$', views.EventsListView.as_view(), name='index'),
	url(r'^events/add/$', views.EventCreateView.as_view(), name='EventCreateView'),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventDetailsView.as_view(), name='event_detail'),
    url(r'^events/(?P<pk>[0-9]+)/comment/(?P<comment_id>[0-9]+)/', views.EventDetailsView.as_view(), name='event_detail_with_comment'),
    url(r'^events/(?P<pk>[0-9]+)/edit/$', views.EventEditView.as_view(), name='EventEditView'),
    url(r'^events/(?P<pk>[0-9]+)/delete/$', views.DeleteEvent, name='DeleteEvent'),
    # Organization
    url(r'^organizations/add/$', views.OrganizationCreateView.as_view(), name='OrganizationCreateView'),
    # Profile
    url(r'^profile/$', views.UserProfileView.as_view(), name='UserProfileView'),
    url(r'^profile/organizations/$', views.UserOrganizationsView.as_view(), name='UserOrganizationsView'),
    url(r'^profile/events/$', views.UserEventsView.as_view(), name='UserEventsView'),
    url(r'^profile/comments/$', views.UserCommentsView.as_view(), name='UserCommentsView'),
    # Registration and authetication
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    # Comments
    url(r'^add_comment/(?P<pk>[0-9]+)/$', views.AddComment, name='AddComment'),
    url(r'^delete_comment/(?P<pk>[0-9]+)/$', views.DeleteComment, name='DeleteComment'),
    url(r'^change_comment/(?P<pk>[0-9]+)/$', views.ChangeComment, name='ChangeComment'),
]