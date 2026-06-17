'''
MATPLOTLIB
----------
---->this is a library in pytho for data visulization ,allowing users to create a variety of plots
##basic structure of MATPLOTLB
1.figure
2.axis
3.grid
4.title
5.legend

import matplotlib.pyplot as plt
sales =['A','B','C']
values= [25,30,45]
plt.bar(sales,values,color='yellow',edgecolor='red')
plt.xlabel('car models')
plt.ylabel('values')
plt.title('BMW sales')
plt.show()

import matplotlib.pyplot as plt
overs=[1,2,3,4,5]
scores= [4,9,17,20,8]
plt.plot(overs,scores,color='yellow')
plt.xlabel('overs')
plt.ylabel('score')
plt.title('score card')
plt.show()


import matplotlib.pyplot as plt
subjects = ['python','java','c']
students =[35,7,15]
plt.pie(students,labels=subjects,autopct='1.1f%%')
plt.legend(subjects)
plt.title('students in courses')
plt.show()


import matplotlib.pyplot as plt
y = [10,15,18,20,13]

plt.hist(y,color='pink')
plt.title('scatter plot')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

#scatter graph
import matplotlib.pyplot as plt
y = [10,15,18,20,13]
x = [7,8,6,5,3]
plt.scatter(y,color='pink')
plt.title('scatter plot')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()


#bar graph
import matplotlib.pyplot as plt
sales =['A','B','C']
values= [25,30,45]
plt.bar(sales,values,color='yellow',edgecolor='red')
plt.xlabel('car models')
plt.ylabel('values')
plt.title('suzuki sales')
plt.show()

#scatter graph
import matplotlib.pyplot as plt
sales = ['A','B','c']
values = [70,80,90]
plt.scatter(sales,values,color='pink')
plt.xlabel('car models')
plt.ylabel('values')
plt.title('tata cars ')
plt.show()
'''
#pie chart
import matplotlib.pyplot as plt
sales = ['A','B','C']
values =[50,60,70]
plt.pie(sales, labels=values,color='yellow')
plt.xlabel('car models')
plt.ylabel('values')
plt.title('honda')
plt.show()





