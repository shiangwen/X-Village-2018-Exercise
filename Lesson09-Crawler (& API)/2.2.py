from requests_html import HTMLSession
session = HTMLSession()
response = session.get('https://www.imdb.com/title/tt4073790/?ref_=fn_al_tt_1')


elements = response.html.find('#wrapper #main_top [itemprop=director] .itemprop' )

for element in elements:
    print(element.text)



