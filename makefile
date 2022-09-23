image?=image
app?=app
tag?=tag

build:
	docker build . -t ${tag} 

run:
	docker run --publish 127.0.0.1:8000:8000 ${image}

push:
	git push master master