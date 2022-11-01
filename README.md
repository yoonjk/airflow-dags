# airflow-dags

helm repo add apache-airflow https://airflow.apache.org
helm upgrade --install airflow apache-airflow/airflow --namespace airflow 

helm upgrade \
    --install \
    -f values.yaml \
    --namespace airflow \
    --timeout 30m0s \
    --wait=false \
    --create-namespace \
    airflow \
    apache-airflow/airflow