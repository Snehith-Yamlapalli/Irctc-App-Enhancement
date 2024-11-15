# IRCTC Train Status
This project mainly try something new to get juicy info out of Api provided by google {Whereismytrain}
### How to use it

Make sure you have python3 and pip3 installed
- Run ```pip3 install -r requirements.txt```
- Run ```python3 app.py```

### Apis used for fetching station data
* https://api.railyatri.in/api/common_city_station_search.json
### Api used for train details
* https://whereismytrain.in/cache/live_status?train_no=TRAINNO&date=DATE(in dd-mm-yyyy format)&lang=hi
### Url used for pnr status
* https://www.confirmtkt.com/pnr-status/YOURPNRNum

**For more info see code**
Run The **IRTC Main Page.html** (in the **templates folder**) to live server from your VS-Code and you can find everything from.
This is just a front-end model.
