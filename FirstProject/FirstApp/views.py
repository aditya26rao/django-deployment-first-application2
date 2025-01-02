from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.
def welcome(request):
    return HttpResponse("<h1> Hello User , Welcome to Django Homepage </h1>")

def show(request):
    ss='''
    <!--
	HTML Webpage to display "Welcome-Message" with different Headings 
	(F:\SAISIR\HTML\Welcome.html)
-->

<html>
	<head>
		<title>***Welcome-Page***</title>
		<style>
			h1{
				color:Blue;
			}
			h2{
				color:Green;
			}
			h3{
				color:Red;
			}
			h4{
				color:Orange;
			}
			h5{
				color:Pink;
			}
			h6{
				color:violet;
			}
			h1,h3,h5{
				background-color:yellow;
			}
			h2,h4,h6{
				background-color:lightgreen;
			}
		</style>
	</head>
	<body>
		<center>
			<h1>Welcome to DJANGO HTML webpage</h1>
			<hr color="brown" width="95%"/>
			<h2>Welcome to DJANGO HTML webpage</h2>
			<hr color="brown" width="85%"/>
			<h3>Welcome to DJANGO HTML webpage</h3>
			<hr color="brown" width="75%"/>
			<h4>Welcome to DJANGO HTML webpage</h4>
			<hr color="brown" width="65%"/>
			<h5>Welcome to DJANGO HTML webpage</h5>
			<hr color="brown" width="55%"/>
			<h6>Welcome to DJANGO HTML webpage</h6>
			<hr color="brown" width="45%"/>
		</center>
	</body>
</html>
    '''
    return HttpResponse(ss)


def senddatetime(request):
    print("dtime url is requested and sendatetime() is executed");
    ct=time.ctime()
    print("Client Request Date and Time on server ::",ct);
    ss='''
    <html>
    <head>
    <title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightgreen;
					border:2px Solid Brown;
				}
			</style>

    </head>
    <body>
    </body>
    	<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='70%'/>
				<h3>''',ct,'''</h3>
				<hr color='brown' width='60%'/>
			</center>

    </html>
    '''
    return HttpResponse(ss);
    
def demo(request):
    return HttpResponse("<h1>Hello User this Webpage has same data for Multi URLs</h1>");

def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
    </center>''';
    return HttpResponse(htmldata);


