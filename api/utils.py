import os, tempfile
from django.conf import settings

class WebApiException(Exception):
    pass

def interpreter_path(interpreter):
    return os.path.join(settings.BASE_DIR, 'pygobstones','language', 'v' + interpreter, "gbs.py")

def run_program(interpreter, program, board, options):
    tempf = tempfile.NamedTemporaryFile(delete=False, suffix=".gbs")
    tempf.write(program)
    tempf.flush()
    tempf.close()       
    result = os.popen('%s %s %s %s' % (interpreter_path(interpreter), 
                                       tempf.name, 
                                       board, 
                                       options)).read()
    os.unlink(tempf.name) 
    return result   


