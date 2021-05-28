docker run \
--name checkrunner \
-p 5000:5000 \
-e SERVER=host.docker.internal \
--rm \
-v /checks:/checks \
checkrunner:1.0.0

# docker run --name checkrunner -p 5000:5000 -e SERVER=host.docker.internal -it --entrypoint /bin/bash --rm -v E:\echo\checkrunner\checks:/checks checkrunner:1.0.0
# docker run --name checkrunner -p 5000:5000 -e SERVER=host.docker.internal --rm -v E:\echo\checkrunner\checks:/checks checkrunner:1.0.0 