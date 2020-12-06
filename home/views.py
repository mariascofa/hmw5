from django.shortcuts import render

# Create your views here.

def hello (request):
    """This function will output the value
    that has been created in the template.
    If url path has been specified, this value will be displayed
    on the specified page."""

    return render (request,"index.html")
