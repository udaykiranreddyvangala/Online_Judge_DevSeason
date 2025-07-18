from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CodeSubmissionForm
from django.conf import settings
import os
import uuid
import subprocess
from pathlib import Path
# Create your views here.

def submit(request):
    
    if request.method=='POST':
        form=CodeSubmissionForm(request.POST)
        
        if form.is_valid():
            submission=form.save()
            
            output=run_code(
                submission.language,submission.code,submission.input_data
            )
            submission.output_data=output
            submission.save()
            return render(request,"result.html",{"submission":submission})
        
        form=CodeSubmissionForm()
        return render(request,"index.html",{"form":form})
    
def run_code(language,code,input_data):
    project_path=Path(settings.BASE_DIR)
    
    directories=["codes","inputs","outputs"]
    
    for directory in directories:
        dir_path=project_path/directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True,exist_ok=True)
        
    codes_dir=project_path/"codes"
    inputs_dir=project_path/"inputs"
    outputs_dir=project_path/"outputs"
        
    unique=str(uuid.uuid4())
        
    code_file_name=f"{unique}.{language}"
    input_file_name=f"{unique}.txt"
    output_file_name=f"{unique}.txt"
        
    code_file_path=codes_dir/code_file_name
    input_file_path=codes_dir/input_file_name
    output_file_path=codes_dir/output_file_name
        
    with open(code_file_path,"w") as code_file:
        code_file.write(code)
        
    with open(input_file_path,"w") as input_file:
        input.write(input)
        
    with open(output_file_path,"w") as output_file:
        pass
    
    if language=="cpp":
        executable_path = codes_dir / (unique + ".exe")
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)]
        )
        
        if compile_result.returncode==0:
            with open(input_file_path,"r") as input_file:
                with open(output_file_path,"w") as output_file:
                    subprocess.run([str(executable_path) + ".exe"], stdin=input_file, stdout=output_file, shell=True)
                    
    elif language=="py":
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    ["python", str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                )
    
    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()

    return output_data