from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from get_price.models import Userfile
from django.template import RequestContext
from django import forms
import requests
from django.contrib import messages
from django.utils import timezone
from .models import Userfile,Pack
import urllib

# Create your views here.


class Result:
    def __init__(self,danjia,chengben,banfei,flag1):
        self.unit_price = danjia
        self.cost = chengben
        self.edition_fee = banfei
        self.flag = flag1

class Last_result:
    def __init__(self,A='0',B='0',C='0',D='0',E='0',F='0',G='0',H='0',I='0',J='0',K='0',L='0',M='0',N='0',O='0',P='0',Q='0',R='0',S='0',T='0',U='0',V='0',W='0',X='0',Y='0',Z='0'):
        if A == 'None':
            A = '0'
        if B == 'None':
            B = '0'
        if C == 'None':
            C = '0'
        if D == 'None':
            D = '0'
        if E == 'None':
            E = '0'
        if F == 'None':
            F = '0'
        if G == 'None':
            G = '0'
        if H == 'None':
            H = '0'
        if I == 'None':
            I = '0'
        if J == 'None':
            J = '0'
        if K == 'None':
            K = '0'
        if L == 'None':
            L = '0'
        if M == 'None':
            M = '0'
        if N == 'None':
            N = '0'
        if O == 'None':
            O = '0'
        if P == 'None':
            P = '0'
        if Q == 'None':
            Q = '0'
        if R == 'None':
            R = '0'
        if S == 'None':
            S = '0'
        if T == 'None':
            T = '0'
        if U == 'None':
            U = '0'
        if V == 'None':
            V = '0'
        if W == 'None':
            W = '0'
        if X == 'None':
            X = '0'
        if Y == 'None':
            Y = '0'
        if Z == 'None':
            Z = '0'
        self.dict = {'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,'L':L,'M':M,'N':N,'O':O,'P':P,'Q':Q,'R':R,'S':S,'T':T,'U':U,'V':V,'W':W,'X':X,'Y':Y,'Z':Z,}

def Formula(pack,A='0',B='0',C='0',D='0',E='0',F='0',G='0',H='0',I='0',J='0',K='0',L='0',M='0',N='0',O='0',P='0',Q='0',R='0',S='0',T='0',U='0',V='0',W='0',X='0',Y='0',Z='0'):
    if A != 'None':
        A = int(A)
    if B != 'None':
        B = int(B)
    if C != 'None':
        C = int(C)
    if D != 'None':
        D = int(D)
    if E != 'None':
        E = int(E)
    if F != 'None':
        F = int(F)
    if G != 'None':
        G = int(G)
    if H != 'None':
        H = int(H)
    if I != 'None':
        I = int(I)
    if J != 'None':
        J = int(J)
    if K != 'None':
        K = int(K)
    if L != 'None':
        L = int(L)
    if M != 'None':
        M = int(M)
    if N != 'None':
        N = int(N)
    if O != 'None':
        O = int(O)
    if P != 'None':
        P = int(P)
    if Q != 'None':
        Q = int(Q)
    if R != 'None':
        R = int(R)
    if S != 'None':
        S = int(S)
    if T != 'None':
        T = int(T)
    if U != 'None':
        U = int(U)
    if V != 'None':
        V = int(V)
    if W != 'None':
        W = int(W)
    if X != 'None':
        X = int(X)
    if Y != 'None':
        Y = int(Y)
    if Z != 'None':
        Z = int(Z)

    area = eval(str(pack.area))
    cost = eval(str(pack.cost))
    banfei = eval(str(pack.edition_fee))

    if(banfei < 230):
        banfei = 230*C
    else:
        banfei = banfei * C


    if(N<10000):
        price = cost*float(pack._5000_10000)
    elif(N>=10000 and N<20000):
        price = cost*float(pack._10000_20000)
    elif(N>=20000 and N<50000):
        price = cost*float(pack._20000_50000)
    elif(N>=50000):
        price = cost*float(pack._50000)

    result = Result("%.3f"%price,"%.3f"%cost,"%.3f"%banfei,1)
    return result


def signin_page(request):
    if request.method == "GET":
        return render(request,'sign_in.html')
    else:
        userid = request.POST.get("user_id", None)
        password = request.POST.get("password", None)

        try:
           user = Userfile.objects.get(user_id=userid)
           pw = user.password
           if pw == password:
               return HttpResponseRedirect( userid +'/')
           else:
               messages.error(request,"密码错误！")
               return render(request,'sign_in.html')
        except:
            messages.error(request,"用户不存在！")
            return render(request,'sign_in.html')

def home_page(request,user_id):
    if request.method == "GET":
        packs = Pack.objects
        return render(request,'home.html',{'user_id':user_id,'packs':packs})

def pack_page(request,user_id,pack_name):
     if request.method == "GET":
        #pack_name = urllib.parse.unquote(pack_name)   #url编码转中文
        result = Result(0,0,0,0)
        pack = get_object_or_404(Pack, name = pack_name)
        cons = eval(pack.contrast)
        last_result = Last_result()
        return render(request,'category.html',{'user_id':user_id,'pack':pack,'result':result,'cons':cons,'last_result':last_result})
     else:
        try:
            pack = get_object_or_404(Pack, name = pack_name)
            cons = eval(pack.contrast)
            a = request.POST.get("A", None)
            b = request.POST.get("B", None)
            c = request.POST.get("C", None)
            d = request.POST.get("D", None)
            e = request.POST.get("E", None)
            f = request.POST.get("F", None)
            g = request.POST.get("G", None)
            h = request.POST.get("H", None)
            i = request.POST.get("I", None)
            j = request.POST.get("J", None)
            k = request.POST.get("K", None)
            l = request.POST.get("L", None)
            m = request.POST.get("M", None)
            n = request.POST.get("N", None)
            o = request.POST.get("O", None)
            p = request.POST.get("P", None)
            q = request.POST.get("Q", None)
            r = request.POST.get("R", None)
            s = request.POST.get("S", None)
            t = request.POST.get("T", None)
            u = request.POST.get("U", None)
            v = request.POST.get("V", None)
            w = request.POST.get("W", None)
            x = request.POST.get("X", None)
            y = request.POST.get("Y", None)
            z = request.POST.get("Z", None)
            last_result = Last_result(A=str(a),B=str(b),C=str(c),D=str(d),E=str(e),F=str(f),G=str(g),H=str(h),I=str(i),J=str(j),K=str(k),L=str(l),M=str(m),N=str(n),O=str(o),P=str(p),Q=str(q),R=str(r),S=str(s),T=str(t),U=str(u),V=str(v),W=str(w),X=str(x),Y=str(y),Z=str(z))
            result = Formula(pack,A=str(a),B=str(b),C=str(c),D=str(d),E=str(e),F=str(f),G=str(g),H=str(h),I=str(i),J=str(j),K=str(k),L=str(l),M=str(m),N=str(n),O=str(o),P=str(p),Q=str(q),R=str(r),S=str(s),T=str(t),U=str(u),V=str(v),W=str(w),X=str(x),Y=str(y),Z=str(z))
            return render(request,'category.html',{'user_id':user_id,'pack':pack,'result':result,'cons':cons,'last_result':last_result})
        except:
            messages.error(request,"输入不可为空！")
            result = Result(0,0,0,0)
            return render(request,'category.html',{'user_id':user_id,'pack':pack,'result':result,'cons':cons,})
            
def staff_informations_page(request,user_id):
    if request.method == "GET":
        user = get_object_or_404(Userfile, user_id = user_id)
        return render(request,'staff_informations.html',{'user':user,})



