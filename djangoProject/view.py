import datetime

from django.http import HttpResponse
from django.shortcuts import render


def get_time(request):


    uhrzeit = datetime.datetime.now()

    return HttpResponse(f'''
    <!DOCTYPE>
    <html>
    <body>
    {uhrzeit}
    </body>
    </html>
    ''')