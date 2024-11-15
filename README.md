# IRCTC Application Enhancement
Theproject aims to upgrade the IRCTC application by enhancing its booking capacity and incorporating an intuitive seat selection feature.
1) We increased the booking capacity to 12 members .
2) Seat selection feature will provide passengers with the flexibility to choose their preferred seats based on specific factors
- like proximity to exits
-  availability of window seats
-   location within the coach.
3) And you can Upgrade your ticket from lower tier to upper tier.
  
 **By implementing
 these upgrades, the IRCTC app is positioned to deliver a more reliable
 and satisfying user experience, leading to improved customer satisfaction**

### How to run the code

Make sure you have python3 and pip3 installed
- Run ```pip3 install -r requirements.txt```
- Run ```python3 app.py```
- Go to the templates folder and run the **IRCTC Main Page.html** with live server.


### Apis used for fetching station data
* https://api.railyatri.in/api/common_city_station_search.json
### Api used for train details
* https://whereismytrain.in/cache/live_status?train_no=TRAINNO&date=DATE(in dd-mm-yyyy format)&lang=hi
### Url used for pnr status
* https://www.confirmtkt.com/pnr-status/YOURPNRNum

**For more info**
Check the Templates folder
