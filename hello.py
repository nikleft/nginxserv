def wsgiapp(environ, start_response):
	#logic
	status = '200 OK'
	headers = [ ('Content-Type','text/plain')]
	body =[str(i)+'\n' for i in environ['QUERY_STRING'].split("&")]
	start_response(status,headers)
	return body
#bytes(i+'\n','ascii')
#body = [bytes((i+'\n','ascii')) for i in environ['QUERY_STRING'].split('&')]
