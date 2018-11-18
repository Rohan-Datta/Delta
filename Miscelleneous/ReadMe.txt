To Load Data From The Dataset to MySQL Table:

LOAD DATA LOCAL INFILE '/home/abhishek/Desktop/Delta/Miscelleneous/laptops_with_photo_url.csv' INTO TABLE ItemsAPI_laptops
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

DEPENDENCIES :

django_mysql
colorthief
rest_framework