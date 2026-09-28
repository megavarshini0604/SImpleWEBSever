from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>My Django Web Page</h1>
        <h2>Name: Megavarshini.A</h2>
        <h2>Register Number: 26019284</h2>
        <h3>TCP/IP Protocol Suite:</h3>
        <ul>
            <li>Application Layer: HTTP, HTTPS, FTP, DNS</li>
            <li>Transport Layer: TCP, UDP</li>
            <li>Internet Layer: IP, ICMP, ARP</li>
            <li>Link Layer: Ethernet, Wi-Fi</li>
        </ul>
    """)