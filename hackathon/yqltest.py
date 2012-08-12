import yql
y = yql.Public()
query = 'USE "http://www.datatables.org/twitter/twitter.search.xml";SELECT text,from_user FROM twitter.search WHERE q="bangalore" or q="Bangalore" limit 3'
#query = 'select * from flickr.photos.search where text="panda" and api_key="b957a978ebcb9b565ba842df84c0a029" limit 3';
result = y.execute(query)
#result.rows
for row in result.rows:
	print row.get('from_user') + ' ----> ' + row.get('text')
	print ' '