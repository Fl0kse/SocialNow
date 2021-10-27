# SocialNow

### Image
To build project
```
docker build --tag socialnow . 
```

To run project
```
docker run --name socialnow -d -p 8000:8000 socialnow
```

To remove all images
```
docker rm -vf $(docker ps -a -q)
```