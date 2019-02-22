class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        c_a=0
        c_b=0
        flag=0
        j=''
        a=list(a)
        b=list(b)
        k=0
        while a!=[] or b!=[]:
            if a!=[]:
                c_a=int(a.pop())
            if b!=[]:
                c_b=int(b.pop())
            k=c_a+c_b+flag
            if flag==1:
                flag=0
            if k==2:
                k=0
                flag=1
            elif k==3:
                k=1
                flag=1
            c_a=0
            c_b=0
            j+=str(k)
        if flag!=0:
            j+=str(flag)
        return j[::-1]
            
        
