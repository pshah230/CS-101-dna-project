#!/usr/bin/env python
# coding: utf-8

# In[7]:


def reverse_complement(dna):
    reverse=dna[::-1]
    complement = ''
    for symbol in reverse:
        if symbol == 'A':
            complement = complement + 'T'
        elif symbol == 'C':
            complement = complement + 'G'
        elif symbol == 'G':
            complement = complement + 'C'
        elif symbol == 'T':
            complement = complement + 'A'
    return complement


# In[8]:


print (reverse_complement('AAAGGCTTTCCT'))


# In[9]:


from math import factorial
def nCr(n, r):
    return (factorial(n) / (factorial(r)
                       * factorial(n - r)))
def mendels_law(hom, het, rec):
    if hom >= 2 and het>=2 and rec>=2:
        total1 = (nCr(hom, 2) * 4) + (hom * het * 4) + (hom * rec * 4) + (het * rec * 4) + (nCr(het, 2) * 4) + (
                    nCr(rec, 2) * 4)
        dominant1 = (nCr(hom, 2) * 4) + (hom * rec * 4) + (hom * het * 4) + (het * rec * 2) + (nCr(het, 2) * 3)
        p = dominant1 / total1
        return p

    elif hom<2 and het<2 and rec<2 :
        total2 = (hom*het*4)+(hom * rec * 4)+ (rec*het*4)
        dominant2 = (hom * rec * 4) + (hom * het * 4) + (het * rec * 2)
        z= dominant2 / total2
        return z
    elif hom<2 and het<2 and rec>=2 :
        total3= (hom*het*4)+(hom * rec * 4)+ (rec*het*4)+(nCr(rec, 2) * 4)
        dominant3 = (hom * rec * 4) + (hom * het * 4) + (het * rec * 2)
        s=dominant3/total3
        return s
    elif hom<2 and het>=2 and rec<2:
        total4 = (hom*het*4)+(hom * rec * 4)+ (rec*het*4) + (nCr(het, 2) * 4)
        dominant4 = (hom * rec * 4) + (hom * het * 4) + (het * rec * 2) + (nCr(het, 2) * 3)
        t = dominant4/total4
        return t
    elif hom>=2 and het<2 and rec<2:
        total5 = (hom*het*4)+(hom * rec * 4)+ (rec*het*4) + (nCr(hom, 2) * 4)
        dominant5 = (hom*het*4)+(hom * rec * 4)+ (rec*het*2) + (nCr(het, 2) * 4)
        u = dominant5/total5
        return u


# In[ ]:




