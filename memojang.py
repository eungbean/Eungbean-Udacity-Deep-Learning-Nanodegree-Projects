nvidia-
docker run -it \
-p 6006:6006 -p 8888:8888 \
-h tf3 \
--name tf3 \
-v /Users/staryly/WORKSPACE/Git:/notebooks \
-v /Users/staryly/WORKSPACE:/data \
--ipc=host \
ufoym/deepo:cpu bash

#jupyter notebook 실행
docker exec tf3 \
jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token= --notebook-dir='/notebooks'

#jupyter-nbextensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

#jupyter_nbextensions_configurator
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user

#jupyter theme
pip install jupyterthemes
pip install --upgrade jupyterthemes
jt -t chesterish -T

jt -t chesterish -altp -cellw 88% -T

jt -t chesterish \
-fs 95 \ #Code Font-Size
-altp \ #Alt Prompt Layout
-tfs 11 \ #Text/MD Cell Fontsize
-nfs 115 \ #Notebook Font Size
-cellw 88% \ #셀너비
-T #툴바보임



#etcs
pip install tqdm