FROM python
COPY . /python/docker
EXPOSE 3000
CMD ["python","/python/docker/str_fun2_demo.py"]