from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Sub Application 1</h1>')

def start_app(request):
    init_string = ""
    for i in range(10):
        for j in range(10):
            string = f"<li>{i} * {j} = {i*j}</li>"
            init_string += string
    return HttpResponse(f"<ul>{init_string}</ul>")