FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \
	python3.6 \
	python3-pip
RUN pip3 install flask scikit-learn==0.22.2
ADD app.py /root
ADD a_model /root
WORKDIR /root
ENTRYPOINT ["python3"]
CMD ["app.py"]
