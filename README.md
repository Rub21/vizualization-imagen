vizualization-imagen
====================
Always that you want to see how was your progress and you want to share as image [like this]()

Steps:

# 1. Clone repository
	
	`$ git clone https://github.com/Rub21/vizualization-imagen.git`
	

# 2. Download Data

- Firstly you have to active JOSM as [remote mode](https://cloud.githubusercontent.com/assets/1152236/5185379/138afea8-748d-11e4-801a-19d7dbc2b99e.png)


- Download a place where you've worked and since the exact date

Example: User [ediyes](http://www.openstreetmap.org/user/ediyes) have worked at in Ayacucho since 01/09/2014 00:00:00, 
for dowloand the data you have to set on [app](http://rub21.github.io/download-osm-data/#13.00/-13.1660/-74.2153)

**Focus in Ayacucho**

[Focus in Ayacucho](https://cloud.githubusercontent.com/assets/1152236/5608852/3521968a-945e-11e4-932e-19ca396adef6.png)

**Setting the user, time and types of data**

![Setting the user, time and types of data](https://cloud.githubusercontent.com/assets/1152236/5608908/81cd9bae-945f-11e4-848a-bae1161f4000.png)


Save data as ayacucho.osm on directory **vizualization-imagen**


# 3. Process Data

If you use Windows as SO. you have to configure context environment for python. on Linux it come for default.
open the terminal and go to **vizualization-imagen** directory and execute:

`$ cd vizualization-imagen`

`$ python converts-way.py ayacucho.osm ayacucho.geojson`

 At last you are going to have onw file called ayacucho.geojson **vizualization-imagen** directory

# 4. Project on Tilemill

- Create a new project on tilemill and paste the next code on tilemill:

```css
Map { background-color:#000; }
#countries {
	line-color:#555;
	line-join:round;
	line-width:0.5;
}
@grey: #2d2c2c;
@blue : #0171C5;
@magenta: #ff0094;
@green: #0F0;
@red: #DA6068;
@morado:#9900FF;
@yellow: #FF0;
@aqua:#00FFFF;
@fuxia:#FF00FF;


#osm{
	line-color:@grey;
}
#osm[user='ediyes']{
    line-width:0.8;
    [version='1']{
      line-color:@yellow;
    }
	line-color:@yellow*0.4;
}

```
**Change you user name and your prefer color**


https://github.com/Rub21/vizualization-imagen/blob/master/styles.css

![screenshot from 2014-11-25 11 03 29](https://cloud.githubusercontent.com/assets/1152236/5186183/b6822596-7492-11e4-8147-9a34bc5b5f68.png)


- Export as imagen and edited with an image editor. like:

![visualizacion_c7f118](https://cloud.githubusercontent.com/assets/5991158/4525793/41fc1828-4d58-11e4-818d-dd790e83914e.png)
