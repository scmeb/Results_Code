import iris 
import sys
import matplotlib.pyplot as plt
import iris.plot as iplt
import iris.quickplot as qplt
import numpy
from iris.experimental.equalise_cubes import equalise_attributes
from iris.util import unify_time_units
import os

iris.FUTURE.netcdf_promote = True

filename = []

for root, dirs, files in os.walk(r'/home/cserv1_a/soc_pg/scmeb/Documents/Moist_Convection/Soundings/AMMA_July_August/ncfiles'):
    for file in files:
        if file.endswith('.nc'):
            filename.append(''.join(['/home/cserv1_a/soc_pg/scmeb/Documents/Moist_Convection/Soundings/AMMA_July_August/ncfiles/',file]))


print(filename)


cubes = iris.load(filename,'Potential Temperature')
#cubes = iris.load(filename)
print(cubes)
equalise_attributes(cubes)
unify_time_units(cubes)
Merge_cube = cubes.concatenate()

print(Merge_cube)
print(sys.getsizeof(Merge_cube[1]))

potential_temp = Merge_cube[1]

#print(potential_temp2)
#qplt.plot(Merge_cube[0])
print(potential_temp[:,0,0,0])
qplt.plot(potential_temp[:,0,0,0])
plt.show()
