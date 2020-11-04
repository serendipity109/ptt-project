pip install -r requirements.txt
cd ptt
scrapy crawl ptt -o gossip.json
cd ..
python preprocessing.py
python web.py