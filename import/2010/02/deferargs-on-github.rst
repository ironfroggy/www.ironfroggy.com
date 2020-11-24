A time ago I wrote a library called DeferArgs and I used it when I was
still in Twisted code every day. I no longer have that fun, but I was
reminded of the code and decided to throw it onto GitHub for anyone who
cares for it.
http://github.com/ironfroggy/DeferArgs
An example usage, where foo could take any deferreds and would be called
when they all fire.
@deferargs
def foo():
    assert False
@catch(AssertionError)
def onAssert(error): 
    print "OOPS"     
@catch()             
def onOthers(error): 
    print "I WOULD BE REACHED FOR ANYTHING NOT CAUGHT ABOVE."
@cleanup                                                    
def \_(r):                                                   
    print "The result was: ", r
 
