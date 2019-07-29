__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
This problem simulates the populations of roaches in a lab. Some fictitious characteristics for the sake of our 
problem are given below:

- They can be males or females. 
- Females give birth to more roaches after age of 4 weeks. From then they give    
  birth to 5 males and 8 females every week till they die.
- Males die at age of 40 weeks.
- Females die at 30 weeks (you can assume that 29 week old roaches give birth and then die the next week). 

Your job is to model their population as a generator. If you start with a given count of newly born males and females.  

Each successive invocation of the generator should yield (males, females) after another week. The example and the test
below is pretty clear and should clarify all issues. So read it carefully instead of asking questions on forums. 

For e.g. if you start with 5, 5. Then you get 
 - (5,5) [after 1 week], 
 - (5,5) [after 2 weeks] 
 - (5,5) [after 3 weeks] 
 - (5,5) [after 4 weeks]    (now they are 4 weeks old, from next week they start giving birth)
 - (30, 45) [after 5 weeks] (as roaches start giving birth at 4 weeks of age, 
                             so you have (25, 40) newly born roaches at this point)
 - (55, 85) [after 6 weeks]
  ....
  and so on.
  
Notes:
1. raise ValueError if any of the parameters are <=0
2. Model this is an infinite generator, so I can use it as long as I wish to model the population
3. Be sure to model it completely, account for the deaths also. Do not micro optimize.
 
'''
import itertools

co = 0
def get_population(males, females):
    if males<=0 or females<=0:raise ValueError
    if co==0:f=[females];t=[29]
    c1=0
    while(1):
        for i in range(len(f)):
            if t[i]==0:del t[i];del f[i]
            if t[i]>0 and t[i]<=25:males+=f[i]*5;females+=f[i]*8;c1+=1
            t[i]-=1
        if co>0:f.append(co*8);t.append(29)
        yield (males, females)

# write your own test cases.
def test_get_population():
    gen = get_population(5,5)
    # weeks 1 to 4
    assert [(5,5)]*4 == list(itertools.islice(gen, 4))
    # weeks 5 to 9, initial roaches start giving birth
    assert [(30,45), (55,85), (80, 125), (105, 165), (130, 205)] == list(itertools.islice(gen, 5))
    # write more tests yourself.
