#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jwt
#from authlib.jose import jwt
import time

secret = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCrQwFGjBYn6605
gc/MfxTQWgfaGaJgR9ksothsglDDmh0xi223C3SCRXv5Z+KC12he9ZPiEjIYaOag
cmh0/PSVI8kOGo09y9fJ5PBHpImBS8flz37waKaCPw4xA6LTDTRh1B+XUVKIlFJ1
DeOepzpXAssLnal0u7beGwfTnFsf5vEf240cXNXIW36+gJr2aDz1pT2godzhAkF0
mTnn7ZPM/NkpdaQ1mGhkD48JHYXfeEHPY1KYCo+sIGuxwcLFIKm2tsOd1R2OYEIO
ip5QxMUOMiqmz4jO7N63hBxtLCH2LUY13t2kChCs8MfH+Ab3sGodx5s0E6FcwB5S
dPAqZpEVAgMBAAECggEAIjz9DkuHSmfVc7+9+VYWpSi6lSG20qTKiB/uQJM07kXr
PDJxtrx1iG23wT7BjALgfMt/yxx0I2klYkI9G9ZOV1qWIVmxjv8nntdEKi58xvqN
diYrbIifcT6F6cqeTK9BH6W2wxug8mkkqv4h2V/5S9flG+djL1Ev1+tzfxytIw1G
sDJFwvkp6GaD4pYp+8Q1jtyzcF0Z+5D/5/NW/UzHILgZkCkHQpDTSSoqXTxym3Ii
8mQAjnNkXfMmV5pX2ix6w8dNv98GBb7uuvcREU0A4MLKgORbkysbNYa0SxpRmWr7
AUyUhsStMg99MG4RcLhdVXjbHZXWwgR+kdXSRmLmKQKBgQDaQlW+/8J+b3jnMWAI
DSgAgFcrlSe6rYe1PC/mHU6Eu0bFtHk03A/C7RGCoCpKQi7FeVPTbznDztutGwew
SvKtWKVY1Ht6df1uk7zMpDLcYpUkz7Hi3bt/PBk6eN+uY6V+SNylVTT/NCYTAX4x
qXVYmVs2PoLY2L5sfbUA2/XXgwKBgQDI4D1G9KWoF0PP/1nt4tafG/ezxJQ7HquF
1QMAsvvSWg9JGyJaGWe03Jsct5kpP/RJuEi6PI0O5V37sStUtFI7WyzH7O9i1gNP
Zea2Ce0JCBQRm+VT4zqMhtR5lKmth7vJF7qh6NCxNVRug77E9KDxl/9u9F/j1X+1
sX5mGXd5hwKBgAkg3x826TaKiP76ZK7RhgvHUl4DRf8bxOJCmyo/rYoFnycjrjIU
xh/79FCHTF2AuR4PPf9I1pym6S8rQz4PVGkFnRzC/ksX5jqauTnB4FKxWNWKTkFT
zsS6ib+VUJ2lk0Vd3MSZdLb7wl/nHxUKplrHRzZUlPpmzkgRVeGsUXLrAoGBAJt/
WnAO+h2AxPHCTa8kpddNIxZ52fVZ7JURK93ir6VKKgMBijoM6IbNLxWv2lRgOY7H
pSTlspwRWgt4Pn63h+CC18t70mPEH5Pa4hmQ3XjcVAy9jWy+vZgC13+2YRL/u5IT
WFn1i3diPRW/znFQnTXn38fYTFJl9xKDb8FBfYcJAoGAAch2icgvEfLrZAME0k1I
5GVFP2yClxVHGhBwSRvNUigPmzLdnEfoLUJYEa+DmnLgLvVCsr3Db3MUIx0PSsXE
vTRnWGTp9Bi7eTCUxPcCR6zLf28j4a5bQo1P1862u/MAfUo4sg1CYWpIfKGJBTxs
x+9hDIvc8HfCIf999oHVg4A=
-----END PRIVATE KEY-----"""
	
	# header	= {'alg': 'RS256'}
	# payload	= {'sub': '123', 'name': 'spaiki007', 'exp': int(time.time()) + (60 * 10)}
	# encoded = jwt.encode(header, payload, secret)
		
encoded = jwt.encode({'sub': '123', 'name': 'John Doe', 'exp': str(int(time.time()) + (60 * 10))}, secret, algorithm='RS256')
print(type(encoded))
print(type(encoded.decode("utf-8")))