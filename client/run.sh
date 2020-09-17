export FN_AUTH_REDIRECT_URI=http://127.0.0.1:8040/google/auth
export FN_BASE_URI=http://127.0.0.1:8040
export FN_CLIENT_ID=
export FN_CLIENT_SECRET=

export FLASK_APP=client/client.py
export FLASK_DEBUG=1
export FN_FLASK_SECRET_KEY=1234

python -m flask run -p 8040