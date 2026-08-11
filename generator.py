import hashlib

def Hash_Gen(file,Choose,comp_hash):
    error=''
    Choose=Choose.lower()

    try:

        if(Choose=='sha384'):
            m=hashlib.sha384()
        elif(Choose=='shake_256'):
            m=hashlib.shake_256()
        elif(Choose=='blake2b'):
            m=hashlib.blake2b()
        elif(Choose=='sha1'):
            m=hashlib.sha1()
        elif(Choose=='md5'):
            m=hashlib.md5()
        elif(Choose=='sha3_256'):
            m=hashlib.sha3_256()
        elif(Choose=='blake2s'):
            m=hashlib.blake2s()
        elif(Choose=='sha3_224'):
            m=hashlib.sha3_224()
        elif(Choose=='sha3_512'):
            m=hashlib.sha3_512()
        elif(Choose=='sha256'):
            m=hashlib.sha256()
        elif(Choose=='sha3_384'):
            m=hashlib.sha3_384()
        elif(Choose=='sha224'):
            m=hashlib.sha224()
        elif(Choose=='shake_128'):
            m=hashlib.shake_128()
        elif(Choose=='sha512'):
            m=hashlib.sha512()

    except FileNotFoundError:
        error = "Add Atleast One File or more"

    file_data=file.read()
    m.update(file_data)
    if(Choose=="shake_128" or Choose=="shake_256"):
        m=m.hexdigest(64)
    else:
        m=m.hexdigest()

    if(m==comp_hash):
        check=True
    else:
        check=False

    return{
        "Your_Hash":m ,
        "Compare_hash":check,
        "error_mesg":error
    }