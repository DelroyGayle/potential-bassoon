from django.shortcuts import render

def showhomepage(request):
	return render(request, 'testmenu/index.html')    