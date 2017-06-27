import matplotlib.pyplot as plt
import numpy as np

list_conf =[]
CGPA = []
min_conf=raw_input("Give the minimum conf\n")
f = open("result.txt")
for line in f:
    conf = float(line.split()[2])
    CGPA.append(int(line.split()[1]))
    min_conf = float(min_conf)
    if conf > min_conf:
       list_conf.append(conf)
          

#print list    	

f.close()

labels = 'Remedial', 'Non-Remedial'
sizes = [len(list_conf),200]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()








c_six=0
c_sev=0
c_eig=0
c_nine=0

for number in CGPA:
	if number == 6:
	   c_six+=1
	elif number == 7:
		c_sev+=1
	elif number == 8:
	    c_eig+=1
	else:
		c_nine+=1

	



n_groups = 4

cgpa = (c_six, c_sev, c_eig, c_nine)
std_men = (2, 7, 4, 1)


fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, cgpa, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=std_men,
                 error_kw=error_config,
                 label='Count of students')



plt.xlabel('CGPA')
plt.ylabel('Count')
plt.title('CGPA Graph')
plt.xticks(index + bar_width / 2, ('6', '7', '8', '9'))
plt.legend()

plt.tight_layout()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.07*height,
                '%d' % int(height),
                ha='center', va='bottom')


autolabel(rects1)

plt.show()