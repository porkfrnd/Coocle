from googlesearch import search
def searcher(query):
	result = []
	for j in search(query, tld="co.in", num=10, stop=10, pause=2):
		result.append(j)
	return result