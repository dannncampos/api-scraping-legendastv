"""Parser do Crawler Legendas TV"""
from lxml import html


def has_more_pages(html_text):
    """Has more pages validator

    Arguments
        html_text {html}: The entire HTML of the page

    Returns:
        boolean: has more pages
    """
    if html.fromstring(html_text).xpath("//a[@class='load_more']"):
        return True
    return False


def extract_subtitle_info(html_text):
    """
    Extract Subtitle Information

    Arguments:
        html_text {html} -- The entire Html of the page

    Returns:
        list: list with subtitle's info
    """
    info = []

    div_parts = html.fromstring(html_text).xpath("//article//div[@class='f_left']")

    for each_div in div_parts:
        paragraph = each_div.xpath("./p")
        link_download = "http://legendas.tv/downloadarquivo/" + paragraph[0].xpath("./a/@href")[0].split('/')[2]
        title = paragraph[0].xpath("./a/text()")[0]
        author = paragraph[1].xpath("./a/text()")[0]
        more_info = paragraph[1].xpath("./text()")
        quantity_rating = paragraph[1].xpath("./text()")[0].split(',')
        quantity = quantity_rating[0]
        rating = quantity_rating[1]
        sending_date = more_info[1]
        language = each_div.xpath(".././img/@title")

        data = {
            'link_download': link_download,
            'title': title,
            'author': author,
            'quantity': quantity,
            'rating': rating,
            'sending_date': sending_date,
            'language': language[0],
        }

        info.append(data)

    return info
