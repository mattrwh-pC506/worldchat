cd api && docker build -t web . \
    && heroku container:push web -a vast-earth-99742 \
    && heroku container:release web -a vast-earth-99742 \
    && cd .. 

cd ui && docker build -t web . \
    && heroku container:push web -a guarded-plateau-50861 \
    && heroku container:release web -a guarded-plateau-50861 \
    && cd .. 

