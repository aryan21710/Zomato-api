
from pyzomato import Pyzomato
import traceback
import re

mykey='7dcf7b79d4c7bdfd5ffe013ae7361388'
p=Pyzomato(mykey)

print ('ZOMATO API OBJECT CREATED:-',p)


def searchRestaurant(details,r):
    f=open('ResDetails','w')
    #print ('RESTAURANT ENTERED:-',r)
    if 'restaurants' in details.keys():
        lstRes=details['restaurants']
        for i in lstRes:
            if 'restaurant' in i.keys():
                d=i['restaurant']
                '''
                f.write('*' * 60)
                f.write('d is:-'+ '\n')
                f.write(str(d))
                f.write('\n\n')
                f.write('d.keys :-'+ str(d.keys()))
                f.write('\n\n')
                '''
                flag=False
                for k,v in d.items():
                    if 'name' in d and 'average_cost_for_two' in d \
                        and 'user_rating' in d and 'location' in d:
                        n=str(d['name'].upper())
                        avg=str(d['average_cost_for_two'])
                        #print ('NAME OF THE RESTAURANT:-',n)
                        regout=re.search(r,n)
                        if regout:
                            addr=d['location']['address']
                            rating=d['user_rating']['aggregate_rating']
                            avgPrice=d['average_cost_for_two']
                            print ('FOUND YOUR RESTAURANT, DETAILS ARE AS FOLLOWS:-\n',)
                            print ('*' * 60)
                            print ('NAME OF THE RESTAURANT:-',n)
                            print ('AVERAGE COST FOR TWO:-',avgPrice)
                            print ('RATING:-',str(rating))
                            print ('ADDRESS:-',str(addr))
                            print ('*' * 60)
                            flag=True
                            break

        if flag:
            print ('RESTAURANT DETAILS NOT FOUND... PLEASE ENTER THE CORRECT RESTAURANT NAME\n')


    f.close()






c=raw_input('PLEASE ENTER THE CITY TO WHICH YOUR RESTAURANT BELONGS:-\n\n')
r=raw_input('PLEASE ENTER THE NAME OF THE RESTAURANT WHICH YOU WANT TO LOOK FOR:-\n\n')
#c='bangalore'
#r="Ebony"
try:
   details=p.search(q=r,city=c,count=10)
   #print ('\n\n THE DETAILS OF THE RESTAURANT ARE AS FOLLOWS:-',details)
   searchRestaurant(details,r.upper())
except Exception as exc:
    print ('INVALID DETAILS ENTERED:-',exc)
    print ('TRACEBACK :-',traceback.format_exc())





