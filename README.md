# MyDaskKubernetes

My Dask Kubernetes


## 1.py

(venv) devops@Brians-MBP MyDaskKubernetes % /Users/devops/Code/MyDaskKubernetes/venv/bin/python /Users/devops/Code/MyDaskKubernetes/1.py
╭─────────────────── Creating KubeCluster 'my-dask-cluster' ───────────────────╮
│                                                                              │
│   DaskCluster                                                      Running   │
│   Scheduler Pod                                                    Running   │
│   Scheduler Service                                                Created   │
│   Default Worker Group                                             Created   │
│                                                                              │
│ ⠦ Getting dashboard URL                                                      │
╰──────────────────────────────────────────────────────────────────────────────╯

## Dask Helm chart

```bash
devops@Brians-MBP MyDaskKubernetes % helm install --version 2023.1.0 myrelease dask/dask
NAME: myrelease
LAST DEPLOYED: Mon Apr 24 09:03:32 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Thank you for installing DASK, released at name: myrelease.

To learn more about the release, try:

  $ helm status myrelease  # information about running pods and this message
  $ helm get all myrelease     # get full Kubernetes specification

This release includes a Dask scheduler, 3 Dask workers, and  Jupyter servers.

The Jupyter notebook server and Dask scheduler expose external services to
which you can connect to manage notebooks, or connect directly to the Dask
cluster. You can get these addresses by running the following:

  export DASK_SCHEDULER="127.0.0.1"
  export DASK_SCHEDULER_UI_IP="127.0.0.1"
  export DASK_SCHEDULER_PORT=8080
  export DASK_SCHEDULER_UI_PORT=8081
  kubectl port-forward --namespace default svc/myrelease-dask-scheduler $DASK_SCHEDULER_PORT:8786 &
  kubectl port-forward --namespace default svc/myrelease-dask-scheduler $DASK_SCHEDULER_UI_PORT:80 &

  export JUPYTER_NOTEBOOK_IP="127.0.0.1"
  export JUPYTER_NOTEBOOK_PORT=8082
  kubectl port-forward --namespace default svc/myrelease-dask-jupyter $JUPYTER_NOTEBOOK_PORT:80 &

  echo tcp://$DASK_SCHEDULER:$DASK_SCHEDULER_PORT               -- Dask Client connection
  echo http://$DASK_SCHEDULER_UI_IP:$DASK_SCHEDULER_UI_PORT     -- Dask dashboard
  echo http://$JUPYTER_NOTEBOOK_IP:$JUPYTER_NOTEBOOK_PORT       -- Jupyter notebook

NOTE: It may take a few minutes for the LoadBalancer IP to be available. Until then, the commands above will not work for the LoadBalancer service type.
You can watch the status by running 'kubectl get svc --namespace default -w myrelease-dask-scheduler'

NOTE: It may take a few minutes for the URLs above to be available if any EXTRA_PIP_PACKAGES or EXTRA_CONDA_PACKAGES were specified,
because they are installed before their respective services start.

NOTE: The default password to login to the notebook server is `dask`. To change this password, refer to the Jupyter password section in values.yaml, or in the README.md.
```
