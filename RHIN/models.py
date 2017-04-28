from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cargo(models.Model):
	"""docstring for Cargo"""
	
	description = models.CharField(max_length=100, default='')
	floor_sal = models.FloatField(default=None) # piso salarial
	flg_active = models.IntegerField(default=0)


	def __str__(self):
		return self.description

	class Meta():
		
		db_table="cargo"



class Horario(models.Model):
	
	class Meta():
		db_table='horario'

	descricao_turno = models.CharField(max_length=120, default="")
	

	def __str__(self):
		return self.descricao_turno

class DiaHorario(models.Model):
	
	class Meta():
		db_table='dia_horario'

	inicio1=models.TimeField(default=None)
	fim1=models.TimeField(default=None)
	inicio2=models.TimeField(default=None)
	fim2=models.TimeField(default=None)
	dia =  models.IntegerField(default=None)
	horario = models.ForeignKey(
		Horario,
		on_delete=models.CASCADE
	)
		


class Funcionario(models.Model):
	"""docstring for Funcionario"""

	# atributos
	first_name=models.CharField(max_length=100, default="")
	last_name=models.CharField(max_length=100, default="")
	cpf = models.CharField(max_length=14, default="")  # 123.123.123-12
	cep = models.CharField(max_length=9, default="") # 61949-010 
	address = models.CharField(max_length=40, default="")
	city = models.CharField(max_length=30, default="")
	phone1 = models.CharField(max_length=15, default="") # (85) 98974-0984
	phone2 = models.CharField(max_length=15, default="") # (85) 98974-0984
	born_date = models.DateField(default=None)
	gender = models.IntegerField(default=None)
	rg = models.CharField(max_length=30, default="")
	cargo = models.ForeignKey(
		'Cargo',
		on_delete=models.CASCADE
	)

	horario = models.ForeignKey(
		Horario,
		on_delete=models.CASCADE
	)

	salario = models.FloatField(default=None)




	class Meta:
		db_table="funcionario"
			


	def __str__(self):
		return self.first_name+" "+self.last_name


class Ferias(models.Model):
	"""docstring for Ferias"""
	
	start = models.DateField()
	end = models.DateField()
	description = models.CharField(max_length=300)
	flg_type = models.IntegerField(default=0) # 0 - erias | 1 - afastamento
	funcionario = models.ForeignKey(
		'Funcionario',
		on_delete=models.CASCADE
	)


	def __str__(self):
		return self.description

	class Meta:
		
		db_table="afastamento"


class User(models.Model):
	"""docstring for User"""
	
	username = models.CharField(max_length=120, default='')
	password = models.CharField(max_length=50, default='')
	is_active = models.IntegerField(default=1)
	# funcionario = models.ForeignKey(
	# 	'Funcionario',
	# 	on_delete=models.CASCADE
	# )

	def __str__(self):
		return self.username

	class Meta:
		"""docstring for Met"""
		
		db_table='user'



			
		
			
		
			
		
		