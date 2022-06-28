Python package mlproject - module distance - function haversine <br>
input longitude and latitude for two different points on globe to find haversine distance between them. 
<br><br>
-includes a script to run function directly from the terminal<br>
-includes a testing suite using the code coverage package<br>
-package created with packgenlite<br>

Try it out !
<br><br>
install in terminal: <br>
<b>pip install git+ssh://git@github.com/alandavidgrunberg/mlproject</b>
<br><br>
try in Python: <br>
<b>from mlproject import distance</b><br>
<b>distance.haversine(lon1,lat1,lon2,lat2)</b><br>
<i>(pass longitudes and latitude values as comma-seperated floats or integers)</i>
<br><br>
try script in Terminal: <br>
<b> mlproject-computedist --coords  lon1 lat1 lon2 lat3 </b><br>
<i>(pass longitude and latitude values without comma seperation)</i>
<br><br>
run tests in Terminal: <br>
<i>first, download entire package from GitHub, (not just pip install)<br>
then, from inside 'mlproject' directory:<br></i>
<b> make test </b>



