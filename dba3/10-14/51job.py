#from utllib import request,error
from lxml import etree
url = 'http://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

def crawl_data(html):
    html = etree.HTML(html)
    html = etree.ElementTree(html)
    items = html.xpath('//div[@id="resultList"]/div[@class]')
    for i,item in enumerate(items):
        print(type(item))
        item = etree.ElementTree(item)
        print(type(item))
        
html = get_html(url)
crawl_data(html)