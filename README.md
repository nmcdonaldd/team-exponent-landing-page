# dashboard0

 - Start with Flask Chat App environment from last quarter
(follow the guide if you haven't gotten it working: https://piazza.com/class/iwz65whqk5q635?cid=157)
 - Create 1 route: GET /hello/\<username\>
 - Create 3 files: 1 template file, 1 view file, and 1 CSS file
 - Pro tip: This will be a lot easier if you use Ubuntu Linux...
 
 
Example:

	@app.route('/hello/<username>')
	def baby_route(username):
		return render_template('home/hello.html', the_name=username)
