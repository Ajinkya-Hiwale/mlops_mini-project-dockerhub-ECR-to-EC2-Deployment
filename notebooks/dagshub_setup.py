import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/campusx-official/mlops-mini-project.mlflow')
dagshub.init(repo_owner='Ajinkya-Hiwale', repo_name='mlops_mini-project-docker', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)