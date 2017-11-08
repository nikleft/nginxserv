def query_app(environ, start_response)
	#logic
	status = '200 OK'
	headers = [ ('Content-Type','text/plain')]
	body = 'Hello World!'
	start_response(status,headers)
	return [body]
