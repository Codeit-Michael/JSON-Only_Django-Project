from django.shortcuts import render

# Create your views here.
db = {
	"12": {
		"task": "wash dishes"
	},
	"13": {
		"task": "something else"
	}
}


def hello(request):
	return db

# YOUR IDEA DOESNT WORK AT ALL. YOU NEED THE SERIALIZERS MODULE TO DO THIS