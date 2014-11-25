vizualization-imagen
====================
Allow make a  daily progress visualization

Steps:

# 1. Download Data

- Active JOSM as remote mode

![screenshot from 2014-11-25 10 22 03](https://cloud.githubusercontent.com/assets/1152236/5185379/138afea8-748d-11e4-801a-19d7dbc2b99e.png)


- Download the place where you worked. and since the exact date until today


![screenshot from 2014-11-25 10 19 53](https://cloud.githubusercontent.com/assets/1152236/5185328/a2dd6b1e-748c-11e4-9ae9-efb4625ab0ad.png)

Save data as file.osm on same directory where the files [converts-way.py](https://github.com/Rub21/vizualization-imagen/blob/master/converts-way.py) are . 

# 2. Process Data

Run the nest line: 

`python converts-way.py file.osm file.geojson`

# 3. Make imgen on Tilemill

- Make a new project and copy and paste the code on Tilemill

https://github.com/Rub21/vizualization-imagen/blob/master/styles.css

![screenshot from 2014-11-25 10 35 18](https://cloud.githubusercontent.com/assets/1152236/5185647/eb198a82-748e-11e4-8e7f-da2b6ed4712d.png)


- Export as imagen and edited with an image editor. like:

![screenshot from 2014-11-25 11 03 29](https://cloud.githubusercontent.com/assets/1152236/5186183/b6822596-7492-11e4-8147-9a34bc5b5f68.png)

