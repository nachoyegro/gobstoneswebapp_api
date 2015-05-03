from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
# Create your views here.
import os
import tempfile
from utils import run_program

class IndexView(View):
    
    def post(self, request, *args, **kwargs):
        interpreter = kwargs.get('interpreter', 'gbs')
        program = request.POST.get('program', '')
        board = request.POST.get('board', '')    
        options = request.POST.get('options', '')
        
        result = run_program(interpreter, program, board, options + " --output-type json")
        return HttpResponse(repr(result))