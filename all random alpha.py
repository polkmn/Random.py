import random
import string
def ran_list():
    """random for n item""" 
    n = input()
    req = raw_input().split()
    for i in range(1, n+1):
        print str(i)+':' + req[random.randint(0, len(req)-1)]
#-------------------------------------------------
def ran_min_max():
    """random number min to max"""
    minn = input()
    maxx = input()
    print randint(i, j)
#-------------------------------------------------
def ran_str():
    """random password"""
    n = input()/2
    digits = "".join([random.choice(string.digits) for i in range(n)])
    chars = "".join([random.choice(string.letters) for i in range(n)])
    result = digits + chars
    print ''.join(random.sample(result, len(result)))
#--------------------------------------------------
def random_choice():
    """ random simply """
    list_t = t.get()
    listt = list_t.split()
    ress = random.choice(listt)
#--------------------------------------------------
def random_a_to_z():
    #print random.choice(string.ascii_lowercase)
    #print random.choice(string.ascii_uppercase)
random_a_to_z()
#--------------------------------------------------