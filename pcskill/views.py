from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'pcskill/home.html')

def test(request):
	return render(request, 'pcskill/sourse.html')

def one_1(request):
	return render(request, 'pcskill/1/1_1.html')

def one_2(request):
	return render(request, 'pcskill/1/1_2.html')

def one_3(request):
	return render(request, 'pcskill/1/1_3.html')

def one_4(request):
	return render(request, 'pcskill/1/1_4.html')

def one_5(request):
	return render(request, 'pcskill/1/1_5.html')

def two_1(request):
	return render(request, 'pcskill/2/2_1.html')

def two_2(request):
	return render(request, 'pcskill/2/2_2.html')

def two_3(request):
	return render(request, 'pcskill/2/2_3.html')

def two_4(request):
	return render(request, 'pcskill/2/2_4.html')

def three_1(request):
	return render(request, 'pcskill/3/3_1.html')

def three_2(request):
	return render(request, 'pcskill/3/3_2.html')

def four_1(request):
	return render(request, 'pcskill/4/4_1.html')

def four_2(request):
	return render(request, 'pcskill/4/4_2.html')

def four_3(request):
	return render(request, 'pcskill/4/4_3.html')

def four_4(request):
	return render(request, 'pcskill/4/4_4.html')

def four_5(request):
	return render(request, 'pcskill/4/4_5.html')

def four_6(request):
	return render(request, 'pcskill/4/4_6.html')

def exfour_1(request):
	return render(request, 'pcskill/4ex/4ex_1.html')

def exfour_2(request):
	return render(request, 'pcskill/4ex/4ex_2.html')

def exfour_3(request):
	return render(request, 'pcskill/4ex/4ex_3.html')

def exfour_4(request):
	return render(request, 'pcskill/4ex/4ex_4.html')

def exfour_5(request):
	return render(request, 'pcskill/4ex/4ex_5.html')

def exfour_6(request):
	return render(request, 'pcskill/4ex/4ex_6.html')

def exfour_7(request):
	return render(request, 'pcskill/4ex/4ex_7.html')