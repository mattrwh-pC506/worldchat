# World Chat

![demopic](https://github.com/mattrwh-pC506/worldchat/blob/master/demopic.png "Screenshot of Site")

A deployed version of this app can be found here: [World Chat Site](https://guarded-plateau-50861.herokuapp.com/login)

### Run tests (only a few, more to come)
```
. venv/bin/activate &&
pip install -r requirments.txt && 
cd api && 
pytest
```

### Run Locally via Docker + Docker Compose
```
# First, navigate to api/ip_locations/settings.py and set the following ENV Variables to your own keys
# SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'DUMMY_KEY') 
# GOOGLE_API_KEY = os.getenv('GOOGLE_SECRET_KEY', '') 
# RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY', '') 

docker-compose up -d

# Head to localhost:3000
```

### Play with Deployed site (heroku)
```
open https://guarded-plateau-50861.herokuapp.com/login
```
