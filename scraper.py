###############################################################################
# START HERE: Tutorial 3: More advanced scraping. Shows how to follow 'next' 
# links from page to page: use functions, so you can call the same code 
# repeatedly. SCROLL TO THE BOTTOM TO SEE THE START OF THE SCRAPER.
###############################################################################

import scraperwiki
import lxml.html

# scrape_table function: gets passed an individual page to scrape
def scrape_table(jim):
    rows = jim.cssselect("table.Trolley.table tr")  # selects all <tr> blocks within <table class="data">
    for row in rows:
        # Set up our data record - we'll need it later
        record = {}
        table_cells = row.cssselect("td")
        if table_cells:
            table_cellsurls = table_cells[1].cssselect("a") 
            record['HospitalURL'] = table_cellsurls[1].attrib.get('href')
            
            record['Date'] = table_cells[0].text
            record['Hospital'] = table_cells[1].text
            record['Region'] = table_cells[2].text
            record['Trolley Total'] = table_cells[3].text
            record['Ward Total'] = table_cells[4].text


            # Print out the data we've gathered
            print record, '------------'
            # Finally, save the record to the datastore - 'Artist' is our unique key
            scraperwiki.sqlite.save(["Hospital"], record)
        
# # scrape_and_look_for_next_link function: calls the scrape_table
# # function, then hunts for a 'next' link: if one is found, calls itself again
def scrape_and_look_for_next_link(starting_url):
    html = scraperwiki.scrape(starting_url)
    print html
    root = lxml.html.fromstring(html)
    scrape_table(root)
#     Below would find a next button on the page and select it, then loop through that page etc
#     next_link = root.cssselect("a.next")
#     print next_link
#     if next_link:
#         next_url = urlparse.urljoin(base_url, next_link[0].attrib.get('href'))
#         print next_url
#         scrape_and_look_for_next_link(next_url)

  # START HERE: define your starting URL - then call a function to scrape it
starting_url='http://inmo.ie/6022'
scrape_and_look_for_next_link(starting_url)

