from flask import Flask, request, render_template
from generator import Hash_Gen

main=Flask(__name__)

Upload_folder='./uploads'

@main.route('/',methods=['GET','POST'])
def upload_file():

    result=None

    if request.method == 'POST':

        file=request.files.get('file')
        choose=request.form.get('Choose')
        comp_hash=request.form.get('comp_hash')

        if not file or file.filename == '':
            result={
                "error_mesg":"Please Upload a File."}
        elif choose == 'none':
            result={
                "error_mesg":"Please select an Hash Algorithm"
            }

        else:
            result=Hash_Gen(file,choose,comp_hash)

    return render_template('index.html',result=result)

if __name__=="__main__":
    main.run(debug=True)
