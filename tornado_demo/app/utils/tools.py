from functools import wraps

##验证登陆
def auth(fun):
    def wrapper(self,*args,**kwargs):
        user = self.session.get('user')
        if user:
            return fun(self,*args,**kwargs)
        else:
            self.redirect('/login/')
    return wrapper