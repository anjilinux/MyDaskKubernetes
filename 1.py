from dask_kubernetes.operator import KubeCluster
cluster = KubeCluster(name="my-dask-cluster", image='ghcr.io/dask/dask:latest')
cluster.scale(10)
