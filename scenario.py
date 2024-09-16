#Ethan Morris
#senario 1
#5th Hour

steppamon = {
    "cheif kef": {
        "attack" : [80] ,
        "health" :  [20],
    } ,
    "lil yachty" : {
        "attack" : [50] ,
        "heath"  :  [20] ,
    } ,
    "travis scott" :{
        "attack": [90210]  ,
        "health": [3500]
    } ,
    "bll drizzy" :{
        "attack": [10] ,
        "health" : [20]
    } ,
    "kid cudi" :{
        "attack" : [40],
        "health" : [20]
    }
}
print('cheif kef dps change')
steppamon["cheif kef"]["attack"] = int(input())
steppamon["lil yachty"]["attack"] = int(input())
steppamon["travis scott"]["attack"] = int(input())
steppamon["bll drizzy"]["attack"] = int(input())
steppamon["kid cudi"]["attack"] = int(input())
print(steppamon)



