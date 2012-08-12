from flask import Flask, render_template, request
import yql
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('template.html')

@app.route('/query', methods=['GET'])
def query():
    error = None
    if request.method == 'GET':
	#        if valid_login(request.form['city']):
		print 'reached query!!  ' #+ request.form['num']
		x = {}
		x['city'] = request.args.get('city', '')
		x['num'] = request.args.get('num', '')
		print 'yoyoyo'
		return my_link(x)
	#else:
    #        error = 'Invalid username/password'
    # the code below this is executed if the request method
    # was GET or the credentials were invalid
    #return render_template('login.html', error=error)  
  
  
  
  
#@app.route('/my-link/')
def my_link(x):
  print 'I got clicked!'
  y = yql.Public()
  query = 'USE "http://www.datatables.org/twitter/twitter.search.xml";SELECT text,from_user FROM twitter.search WHERE q= "#'+x['city']+'" and to_user_id="0" limit ' + x['num']
  #query = 'select * from flickr.photos.search where text="panda" and api_key="b957a978ebcb9b565ba842df84c0a029" limit 3';
  result = y.execute(query)
  #result.rows
 # for row in result.rows:
 #   print row.get('from_user') + ' ----> ' + row.get('text')
 #   print ' '
  return render_template('result.html',result=result)

if __name__ == '__main__':
  app.debug = True
  app.run()