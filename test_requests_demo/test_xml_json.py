import requests
import xmltodict


def test_xml_res():
	r=requests.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
	res=xmltodict.parse(r.content)
	print(res)