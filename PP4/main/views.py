from django.http import HttpResponse
def test(request):
    return HttpResponse("Test")
def Task(request):
    return HttpResponse("Hello World!14")
    return HttpResponse(response_text, status=200)