from django.conf.urls import url
from . import views

app_name="RHIN"
urlpatterns = [
	url(r'^$', views.main, name='main'),
	# url(r'^details/([a-zA-z0-9]{1,})/$', views.details, name='details'),
	url(r'^funcionario/cadastrar/$', views.addWorker, name='addWorker'),
	url(r'^funcionario/consultar/$', views.listWorkers, name='listWorkers'),
	# url(r'^funcionario/register/$', views.registerWorker, name='registerWorker'),
	url(r'^funcionario/detalhes/([0-9]{1,})/$', views.detailsWorker, name='detailsWorker'),
	url(r'^funcionario/registrar-afastamento/([0-9]{1,})/$', views.addAfastamento, name='addAfastamento'),
	url(r'^funcionario/registrar-afastamento/$', views.registerAfastamento, name='registerAfastamento'),
	url(r'^handleForm/$', views.handleForm, name='handleForm'),
	url(r'^testeSession/$', views.testeSession, name='testeSession'),
	url(r'^showSession/$', views.showSession, name='showSession'),

	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),

	url(r'cargo/cadastrar', views.addCargo, name='addCargo'),
	url(r'cargo/consultar', views.listCargos, name='listCargos'),

	url(r'relatorios/ferias/', views.reportFerias, name='reportFerias'),
	url(r'relatorios/afastamentos/', views.reportAfastamentos, name='reportAfastamentos'),
	

	url(r'ws/teste/', views.testeAjaxRequest, name='testeAjaxRequest'),
	url(r'^horario/cadastrar/$', views.addHorario, name='addHorario'),
	url(r'^ws/registrar-horario/$', views.registerHorario, name='registerHorario'),
]