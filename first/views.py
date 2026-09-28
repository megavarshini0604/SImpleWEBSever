from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>My Django Web Page</h1>
        <h2>Name: Megavarshini.A</h2>
        <h2>Register Number: 26019284</h2>
    """)