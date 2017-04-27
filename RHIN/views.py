#coding=utf-8

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cargo, Funcionario, User, Ferias
from django.core.serializers import serialize

# Create your views here.

def main(request):
	return render( request, 'RHIN/base.html', {} )


# view de cadastro de um novo funcionário
def addWorker(request):

	# Listando todos os cargos
	cargos = Cargo.objects.all()

	if request.method == "POST":
		data =request.POST
		worker = Funcionario(
			first_name=data.get("first_name"),
			last_name=data.get("last_name"),
			cpf=data.get("cpf"),
			cep=data.get("cep"),
			address=data.get("address"),
			city=data.get("city"),
			phone1=data.get("phone1"),
			phone2=data.get("phone2"),
			born_date='2017-05-20',
			gender=1,
			sal=data.get("sal"),
			cargo_id=data.get("cargo")
		)


		try:
			# registrando novo funcionario
			worker.save()

			return render(request, 'RHIN/registrar-funcionario.html', {
				'cargos' : cargos,
				'message' : "Funcionário registrado com sucesso",
				'type': "success"
			})
			
		except Exception as e:
			return HttpResponse(e)
		

		



	return render(request, 'RHIN/registrar-funcionario.html', {
		'cargos' : cargos,
		'message' : '',
		'type' : ''
	})

# lista todos os funcionários registrados
def listWorkers(request):
	
	# listando todos os funcionários
	funcs = Funcionario.objects.all()
	workers = []

	for f in funcs:
		cargo = Cargo.objects.get(pk=f.cargo_id).description
		workers.append({'id':f.id, 'first_name' : f.first_name, 'last_name':f.last_name, 'phone1':f.phone1, 'phone2':f.phone2, 'sal':f.sal, 'cargo':cargo})


	return render(request, 'RHIN/listagem-funcionarios.html', {
		'workers' : workers
	})




def handleForm(request):

	if request.method == "POST":
		print(request.POST)
		data = request.POST

		first_name = data.get("first_name")

		return render(request, 'RHIN/formTest.html', {
			'nome' : first_name
		})
		

	return HttpResponse("handle...")



def detailsWorker(request, funcionario_id):

	# Listando todos os cargos
	cargos = Cargo.objects.all()
	worker = Funcionario.objects.get(pk=funcionario_id)

	return render( request, 'RHIN/detalhes-funcionario.html', {
		'worker' : worker,
		'cargos' : cargos
	})

	# return HttpResponse("Funcionario <strong>%s %s</strong>"%(worker.first_name, worker.last_name))

def testeSession(request):
	request.session['username']='edy';
	return HttpResponse("")

def showSession(request):
	return HttpResponse(request.session['username'])



def login(request):

	context={}

	if request.method=='POST':
		data = request.POST
		context={
			'login' : {
				'username' : data['username']
			}
		}

		try:
			getUser = User.objects.get(username__exact=data['username'], password__exact=data['password'])
			# request.session['user'] = serialize('json', getUser)
			request.session['auth'] = True
			request.session['userid'] = getUser.id
			request.session['username'] = getUser.username
			return redirect('/')
		except Exception as e:
			print(e)


	return render(request, 'RHIN/login.html', context)

def logout(request):

	try:
		del request.session['auth']
	except Exception as e:
		print(e)

	return redirect('/login')


def addCargo(request):
	
	#tratando requisicao POST
	if request.method == 'POST':
		data = request.POST

		cargo = Cargo(
			description=data['description'],
			floor_sal=data['floor_sal'],
			flg_active=1
		)



		try:
			# registrando novo funcionario
			cargo.save()

			return render(request, 'RHIN/cadastros/cadastrar-cargo.html', {
				'message' : "Cargo registrado com sucesso",
				'type': "success"
			})
			
		except Exception as e:
			return HttpResponse(e)


	return render( request, 'RHIN/cadastros/cadastrar-cargo.html', {} )

def listCargos(request):

	cargos = Cargo.objects.all()

	return render( request, 'RHIN/listagens/listagem-cargos.html', {
		'cargos' : cargos
	})


def addAfastamento( request, id_funcionario ):
	
	return render( request, 'RHIN/cadastros/cadastrar-afastamento.html', {'id_funcionario':id_funcionario} )

def registerAfastamento(request):
	if request.method=='POST':
		data = request.POST

		ferias = Ferias(
			start=data['start'],
			end=data['end'],
			description=data['description'],
			flg_type=data['type'],
			funcionario=Funcionario(pk=data['id_funcionario'])
		)

		try:
			
			#
			ferias.save()
			return redirect('/funcionario/consultar')

		except Exception as e:
			return HttpResponse(e)

		print(data['description'])


	return HttpResponse("Method Error")


def reportFerias(request):

	ferias = Ferias.objects.filter(flg_type=0)
	return render(request, 'RHIN/listagens/ferias.html', {'ferias':ferias})

def reportAfastamentos(request):
	ferias = Ferias.objects.filter(flg_type=1)
	return render(request, 'RHIN/listagens/afastamentos.html', {'ferias':ferias})