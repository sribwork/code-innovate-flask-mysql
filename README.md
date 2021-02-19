# Code Innovate - MySQL Flask App
---

## Directory Structure
```
$ tree
.
├── docker_img
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── k8s
│   ├── flask-app
│   │   ├── flask-mysql-svc.yaml
│   │   └── flask-mysql.yaml
│   └── mysql
│       ├── mysql-pvc.yaml
│       ├── mysql.yaml
│       └── sql-cmds.md
└── README.md
```

## Create Docker Flask Image

- Goto the docker_img directory
- Run the docker build with a tag for your repo
```
$ docker build . --no-cache -t iad.ocir.io/<tenancy-namespace>/<flask-mysql-proj>/<flask-mysql-app>:v1
```

## Push to Repo

- Push to the Repo 
```
$ docker login iad.ocir.io
username: <tenancy-namespace>/<user-id>
password: AuthKey
```

## Create MySQL deployment

- Goto k8s/mysql directory
- Create the PVC with storage class
```
kubectl -f mysql-pvc.yaml
```
- Create the MySQL Deployment (db password inside mysql.yaml)
```
kubectl -f mysql.yaml
```
- Login to MySQL with mysql-client and create db and tables and entries
```
kubectl run -it --rm --image=mysql:5.6 --restart=Never mysql-client -- mysql -h mysql -p'<password>'
```
- Look at k8s/mysql/sql-cmds.md file to db info and command
  - db name is `test_db`
  - table name is `test-table`
  - table with: id, firstname and lastname

## Create Flask App and Service

- Go to k8s/flask-app
- Create kubernetes OCI secret
```
$ kubectl create secret docker-registry ocirsecret --docker-server=<region-key>.ocir.io --docker-username='<tenancy-namespace>/<oci-username>' --docker-password='<oci-auth-token>' --docker-email='<email-address>'
```
- Deploy the App and Service
```
$ kubectl apply -f flask-mysql-svc.yaml -f flask-mysql.yaml
```
- Get the LB IP
```
$ kubectl get svc
```
- Test the output
  - Open Port 80 on the LB Public Subnet's Security List
```
curl <lb-public-ip>/users
```
  
