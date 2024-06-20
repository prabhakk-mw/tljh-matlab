#tljh_matlabplugin README

Command to install plugin:
```bash
docker run   --privileged   --detach   --name=tljh-dev   --publish 12000:80   --mount type=bind,source="$(pwd)",target=/srv/src  tljh-systemd
docker exec -it tljh-dev /bin/bash
python3 /srv/src/bootstrap/bootstrap.py --admin admin:password --plugin /srv/src/tljh_matlabplugin/
```
