#Recall

my_list = ['helloe','hi']

#create tuple
# use rounded brackets

rndm = ('Ms.Jackson',1958,True)
# can be indexed
print(rndm[1])
#cannot be changed = immutable
#dictionaries
#two ways to creat
#1
My_dict = dict()
#2
my_dict = {}

#dictionary works on a key value pair
#dictionary of bears
bear={'grizzly':'brown',
'black bear':'black',
'polar':'white',
'spirit':'white',}
#look up by key
print(bear['polar'])
print(bear.keys())
#add a value
bear['koala'] = 'grey'

print(bear)

#change value
bear['polar'] = 'cream'
print(bear)
#check to see if item is in dictionary - search key
n = input('enter a bear:')
if n in bear:
    print('in list. Fur colour is: ',bear[n])
else:
    print('not found')