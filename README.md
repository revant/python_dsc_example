### Generate keys for local development

refer: https://stackoverflow.com/a/14267011

```shell
mkdir -p keys
openssl genrsa 2048 > keys/private.pem
openssl req -x509 -subj "/C=IN/ST=Maharashtra/L=Mumbai/O=Acme Ltd./CN=example.com" -days 1000 -new -key keys/private.pem -out keys/public.pem
openssl pkcs12 -export -in keys/public.pem -inkey keys/private.pem -out keys/secret.pfx -passout pass:12345678
```

### Setup python environment

```shell
python -m venv env
```

### Install requirements

```shell
./env/bin/pip install --upgrade pip
./env/bin/pip install -r requirements.txt
```

### Generate signed.pdf from document.pdf

```shell
./env/bin/python sign_pdf.py
```

### Cleanup

```shell
rm -rf env keys signed.pdf
```
