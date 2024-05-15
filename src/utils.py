import os

def check_paths():
    if not os.path.exists('output/no_helmets'):
        os.makedirs('output/no_helmets')

    if not os.path.exists('output/overloading'):
        os.makedirs('output/overloading')
    
    os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"       