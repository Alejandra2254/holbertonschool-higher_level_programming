#!/usr/bin/python3
'''module to find the peak function'''

def find_peak(list_of_integers):
    '''Find the peak in a list'''
   #!/usr/bin/python3
""" Find the Peak"""
def find_peak(list_of_integers):
    if list_of_integers == []:
        return
    max = 0
    for n in list_of_integers:
        if n > max:
            max = n
    return (max)
    
    
