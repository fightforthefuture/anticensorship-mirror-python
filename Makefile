all: GeoLite2-City.mmdb 

clean:
	rm GeoLite2-City.mmdb

.PHONY: all clean

GeoLite2-City.mmdb:
	curl -O http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz
	gunzip GeoLite2-City.mmdb.gz
