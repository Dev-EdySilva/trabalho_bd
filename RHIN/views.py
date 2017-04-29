#coding=utf-8

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Cargo, Funcionario, User, Ferias, Horario, DiaHorario
from django.core.serializers import serialize

import json

# Create your views here.

def main(request):
	return render( request, 'RHIN/base.html', {} )



def updateFuncionario(request):

	if request.method == 'POST':
		data = request.POST

		funcionario = Funcionario.objects.get(pk=data['funcionario_id'])

		funcionario.first_name=data['first_name']
		funcionario.last_name=data['last_name']
		funcionario.cpf=data['cpf']
		funcionario.rg=data['rg']
		funcionario.cep=data['cep']
		funcionario.address=data['address']
		funcionario.city=data['city']
		funcionario.phone1=data['phone1']
		funcionario.phone2=data['phone2']
		funcionario.cargo=Cargo.objects.get(pk=data['cargo'])
		funcionario.horario=Horario.objects.get(pk=data['horario'])

		try:
			funcionario.save()
			return redirect('/funcionario/consultar')
		except Exception as e:
			return HttpResponse("")

		

		return HttpResponse("")
	


# view de cadastro de um novo funcionário
def addWorker(request):

	# Listando todos os cargos
	cargos = Cargo.objects.all()

	# listagem de horarios
	hours = Horario.objects.all()

	if request.method == "POST":
		data =request.POST
		print(data)

		# 99/99/9999

		dt = data['born_date'].split('/')
		born_date=dt[2]+'-'+dt[1]+'-'+dt[1]

		funcionario = Funcionario(
			first_name=data['first_name'],
			last_name=data['last_name'],
			cpf=data['cpf'],
			cep=data['cep'],
			address=data['address'],
			city=data['city'],
			phone1=data['phone1'],
			phone2=data['phone2'],
			rg=data['rg'],
			salario=data['sal'],
			born_date=born_date,
			gender=data['gender'],
			cargo=Cargo.objects.get(pk=data['cargo']),
			horario=Horario.objects.get(pk=data['horario'])
		)

		



		try:
			# registrando novo funcionario
			funcionario.save()
			

			return render(request, 'RHIN/cadastros/cadastrar-funcionario.html', {
				'cargos' : cargos,
				'horarios' : hours,
				'message' : "Funcionário registrado com sucesso",
				'type': "success"
			})
			
		except Exception as e:
			return HttpResponse(e)
		

		



	return render(request, 'RHIN/cadastros/cadastrar-funcionario.html', {
		'cargos' : cargos,
		'horarios' : hours,
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
		workers.append({'id':f.id, 'first_name' : f.first_name, 'last_name':f.last_name, 'phone1':f.phone1, 'phone2':f.phone2, 'salario':f.salario, 'cargo':cargo})


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

	# listagem de horarios
	hours = Horario.objects.all()

	return render( request, 'RHIN/detalhes-funcionario.html', {
		'worker' : worker,
		'cargos' : cargos,
		'horarios' : hours
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

def addHorario(request):
	if request.method=='POST':
		pass

	cargos = Cargo.objects.all()	
	return render(request, 'RHIN/cadastros/cadastrar-horario.html', {'cargos':cargos})



def registerHorario(request):

	if request.is_ajax():
		if request.method == 'POST':
			
			jsonData = json.loads( request.POST['data'] )

			print(jsonData)

			try:
				h = Horario(descricao_turno=jsonData['description'])
				h.save()

				dias = jsonData['dias']

				for dia in dias:
					DiaHorario.objects.create(
						inicio1=dia['inicio1'],
						fim1=dia['fim1'],
						inicio2=dia['inicio2'],
						fim2=dia['fim2'],
						dia=dia['dia'],
						horario=h
					)

				return JsonResponse({'message':'Horário registrado com sucesso', 'code':1})

			except Exception as e:
				return JsonResponse({'message':'Falha ao registrar', 'code':0})

	

	return HttpResponse("Method not allowed")



def lisagemHorarios(request):

	hours = Horario.objects.all()
	
	

	return render(request, 'RHIN/listagens/listagem-horarios.html', {'data' : hours})


def testeAjaxRequest(request):
	return HttpResponse("TESTANDO")