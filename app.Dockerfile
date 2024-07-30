FROM python:3.12

# RUN pip install fluvio

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH /root/.cargo/bin:$PATH
RUN pip install git+https://github.com/infinyon/fluvio-client-python.git@e72d63c4d15f5606b341d2bcf2da3d9bc3e43f5a

COPY app.py app.py

CMD ["python", "./app.py"]