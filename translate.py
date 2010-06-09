import urllib
import urllib.request
import urllib.parse
import re	
 
def translate(text, sl, tl):
	""" Переводит из исходного языка (sl) в язык назначения (tl) """ 

	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)')]
	

	tr_p = opener.open(
	"http://translate.google.com/translate_t?" + 
        urllib.parse.urlencode({'sl': sl, 'tl': tl}),
        data=urllib.parse.urlencode({'hl': 'en',
				'ie': 'UTF8',
				'text': text,
				'sl': sl, 'tl': tl})
	).read().decode()
	

	PATTERN = r"""<span id=result_box class="short_text"><span .*?>(.*?)</span>"""
	par_p = (re.compile( PATTERN )).search( tr_p ).group(1)
	
	return par_p
    
