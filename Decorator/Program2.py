def gun():
    print('In gun')
def run(y):
    print('In run')
    y()
def fun(y):
    print('In fun')
fun(run(gun))
