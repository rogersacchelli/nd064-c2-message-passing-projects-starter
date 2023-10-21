# Running the Project


## Installation
```bash
## 1. Install VM from vagrant file
vagrant up
	
## 2. Log into VM
vagrant ssh
# or

ssh vagrant@localhost -p 2000 
vagrant # password
	
#3. Copy k3s credentials to vagrant user

mkdir -p .kube
sudo cp -i /etc/rancher/k3s/k3s.yaml $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

export KUBECONFIG=~/.kube/config

```

## Deploymnent

```bash

# 1. Deploy Pods

kubectl apply -f ~/nd064-c2-message-passing-projects-starter/deployment

# 2. Init Postgres Tables

pod_name=$(kubectl get pods -o custom-columns=":metadata.name" --no-headers | grep '^postgres' | head -n 1)

bash scripts/run_db_command.sh $pod_name

```

## Postman

Project includes the postman.json file with methods defined to check project execution. Postman should be executed on host machine
since it references localhost and the exposed ports.

It was added a DELETE method for Person endpoint in order to fulfill project requirements, so postman is arragend to create and delete users by referencing the Id of the created user.