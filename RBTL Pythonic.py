# Andrew Potter. 2019.
# Reasoning between the lines: A logic of relational propositions.
# Dialogue and Discourse, 9(2), 80-110. 
# https://journals.uic.edu/ojs/index.php/dad/article/view/10690

# # Relational propositions as Pythonic Booleans

# basics
def neg(p):     return f'not {p}'
def conj(args): return '('+' and '.join(map(str, args))+')'
def disj(args): return '('+' or '.join(map(str, args))+')'
def exdisj(p,q): return conj((disj((p,q)),neg(conj((p,q)))))
def mimp(p,q):  return f'not ({p} and not {q})'
def meq(p,q):    return conj((mimp(p,q),mimp(q,p)))

# realized 
def mp(p,q):    return f'{mimp(conj((mimp(p,q),p)),q)}'
def djs(p,q): return mimp(conj((disj((p,q)),neg(p))),q)
#unrealized
#def mp(p,q):    return f'{conj((mimp(p,q),p))}'
#def djs(p,q): return conj((disj((p,q)),neg(p)))

# relations
def antithesis(s,n):    return djs(s,n)
def attribution(s,n):   return mp(s,n)
def background(s,n):    return mp(s,n)
def cause(s,n):         return mp(s,n)
def circumstance(s,n):  return mp(s,n)
def condition(s,n):     return mimp(s,n)
def concession(s,n):    return mp(neg(mimp(s,neg(n))),n)
def elaboration(s,n):   return mp(s,n)
def enablement(s,n):    return mp(s,n)
def evaluation(s,n):    return mp(n,s)
def evidence(s,n):      return mp(s,n)
def interpretation(s,n): return mp(n,s)
def justify(s,n):       return mp(s,n)
def means(s,n):         return mp(s,n)
def motivation(s,n):    return mp(s,n)
def nonvolitional_cause(s,n): return(cause(s,n))
def nonvolitional_result(s,n): return(cause(n,s))
def otherwise(s,n):     return exdisj(s,n)
def preparation(s,n):    return mp(s,n)
def purpose(s,n):       return mimp(s,n)
def restatement(s,n):   return mp(s,n)
def result(s,n):        return mp(s,n)
def solutionhood(s,n):  return mp(s,n)
def summary(s,n):       return mp(s,n)
def unconditional(s,n): return conj((n,neg(mimp(s,neg(n)))))
def unless(s,n):        return exdisj(s,n)
def volitional_cause(s,n):  return(cause(s,n))
def volitional_result(s,n): return(cause(n,s))

def contrast(s,n):      return exdisj(s,n)
def conjunction(*args): return conj(args)
def disjunction(*args): return disj(args)
def list(*args):        return conj(args)
def joint(*args):       return conj(args)
def multinuclear_restatement(*args): return conj(args)
def restatement_mn(*args):   return multinuclear_restatement(args)
def sequence(*args):    return conj(args)
def convergence(*args): return conj(args)

if __name__ == "__main__":
#    print('common cause')
#    print(motivation(evidence(evidence(justify(10,antithesis(concession(11,12),13)),antithesis(evidence(condition(4,circumstance(6,5)),concession(2,3)),elaboration(9,condition(8,7)))),1),14))

    print(contrast(1,2))
    print(evidence(1,2))
    print()
    for p in [True,False]:
        for q in [True, False]:
            print(p, q, eval(evidence(p,q)))

        
    
