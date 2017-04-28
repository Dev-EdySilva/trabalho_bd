from RHIN.models import User
from django.shortcuts import render, redirect

class AuthMiddleware(object):
	"""docstring for MiddlewareTest"""
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):

		# user = User.objects.get(pk=1)

		try:
			data = (request.session['auth'])
			response = self.get_response(request)
			return response
		except Exception as e:
			path = request.path

			if path != '/login/' and path != '/auth/':
				return redirect('/login')
			
			return self.get_response(request)

		
		