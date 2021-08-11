from bs4 import BeautifulSoup as bs
import requests

class UrlScrapper():

    def __init__(self, url):
        self.url = url

    def scrape_url(self):
        html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>

                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">
            </head>
            <body>

                <div class="row">

                    <table class="table table-dark" >
                        <tr>
                            <th> Business Name </th>
                            <th> Address </th>
                            <th> Contact(s) </th>
                            <th> Website </th>
                            <th> Email </th>
                        </tr>
                    </table>
                    
                </div>

                <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
            </body>
            </html>
        """

        soup_html = bs(html, 'lxml')

        response =  requests.get(self.url)

        soup = bs(response.text, 'lxml')

        all_links = []

        div_tags = soup.find_all('div', class_='cmpny-lstng url')

        for anchor in div_tags:
            anchors = anchor.find_all('a')

            for href in anchors:
                all_links.append(href['href'])
            

        for anchor in all_links:
            count = 1
            response =  requests.get(anchor)
            soup = bs(response.text, 'lxml')
            business_data = soup.find('div', class_='box-682 bg-none')

            business_name = business_data.find('a', class_='edit_listing').previousSibling
            address = business_data.find('div', class_='cmpny-lstng-1').text
            contact = business_data.find_all('div', class_='cmpny-lstng-1')[1].text

            try:
                website = business_data.find('div', class_='cmpny-lstng url').a.text

                email_ = business_data.find('div', class_='subb-bx MT-15').p.text
                if '@' in email_:
                    email = email_
                else:
                    email = ''

                contact = contact + ',' +  business_data.find_all('div', class_='cmpny-lstng-1')[-1].text
            except:
                website = ' '
                email = ' '

            business_tag = soup_html.new_tag('td')
            business_tag.string = business_name

            address_tag = soup_html.new_tag('td')
            address_tag.string = address

            phone_tag = soup_html.new_tag('td')
            phone_tag.string = contact

            web_tag = soup_html.new_tag('td')
            web_tag.string = website

            email_tag = soup_html.new_tag('td')
            email_tag.string = email

            tr = soup_html.new_tag('tr')
            tr.append(business_tag)
            tr.append(address_tag)
            tr.append(phone_tag)
            tr.append(web_tag)
            tr.append(email_tag)

            soup_html.table.append(tr)

            count += 1

        with open('finelib_data.html', 'w') as html_file:
            html_file.write(soup_html.prettify())


url = 'https://www.finelib.com/cities/port-harcourt/accommodation'.strip()
inst = UrlScrapper(url)

inst.scrape_url()