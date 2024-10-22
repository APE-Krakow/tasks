from datetime import datetime
import time

def log_output_and_time(func):
    '''Log the output and excecution time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\n')
        start_time = time.time()
        
        func()
        
        print("\n%s seconds" % (time.time() - start_time))
        print(f'{"-"*30}')
    
    return wrapper
