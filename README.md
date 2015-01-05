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

- Export imagen:
![](https://cloud.githubusercontent.com/assets/1152236/5613122/4e54097c-94ad-11e4-8b24-73a259da6b71.png)


The size of imagen will be, **width = 1200px**

![screenshot from 2015-01-05 07 34 21](https://cloud.githubusercontent.com/assets/1152236/5613145/96500c26-94ad-11e4-9147-5ff5a6cf7ac7.png)

The file is save in: `/path/to/MapBox/export/`


# 4. Editing imagen

Open your imagen(ayacucho.jpeg) with any Editor of imagen, inthis case I going to use [GIMP](http://www.gimp.org/)

![ediyes](https://cloud.githubusercontent.com/assets/1152236/5613329/b6935c88-94b0-11e4-8cb5-abea20cee446.jpeg)

- Title size(**Ayacucho, Perú**): 70pt
- Date size (**September 01st to September 15th, 2014**): 25pt
- User size (**ediyes**): 25pt**
- Version = 1 size (**Version = 1**): 20pt
- Version > 1 size (**Version > 1**): 20pt

If you worked just one day in a your visualization should be look like this:

![](https://cloud.githubusercontent.com/assets/1152236/3346517/55119694-f8c7-11e3-8d34-e777e9ef8691.jpeg)