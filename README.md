# Docker Swarm — Quick Notes
## Initialize a Swarm (create the first Manager node)
- Initialize: `docker swarm init [--advertise-addr <IP_ADDRESS>]`
    -  `--advertise-addr <IP_ADDRESS>` tells other nodes which IP to use to communicate with this node inside the cluster (helpful when the host has multiple interfaces).
- Get join tokens:
    - `docker swarm join-token worker`
    - `docker swarm join-token manager`
    - (Use the printed command on other hosts to join as a worker/manager.)
## Check node status
- `docker node ls`
### Running in Swarm mode: use services (not docker run)
- Swarm service: `docker service create --name web-demo --publish 8080:80 nginx`
- Plain Docker (single host): `docker run -d -p 8080:80 nginx`
### Scheduling (who decides where it runs?)
- When you `docker service create ...`, the Manager node schedules the tasks to run on an appropriate node (manager or worker), unless you add constraints.

### List services & understand replicas
- `docker service ls`
- `REPLICAS` shows `running/desired` : 
    - 1/1 → desired 1, running 1 ✅
    - 2/2 → desired 2, running 2 ✅
    - 0/1 → desired 1, running 0 ❌
    - 1/3 → desired 3, running 1 (insufficient nodes/resources or errors)

### Scale replicas
- `docker service scale <service_name>=<replica_count>`
    - e.g. `docker service scale web-demo=3`
- Inspect per-task placement: `docker service ps web-demo`

### Useful inspect/debug commands
- `docker service ps <service_name> --no-trunc    # show full details/history`
- `docker service logs -f <service_name>          # aggregated logs across replicas`

### Rolling update
1. Set safe update policy:

```bash
docker service update \
  --update-parallelism 1 \
  --update-delay 10s \
  --update-order start-first \
  web-demo
```
- `--update-parallelism 1` → update 1 replica at a time
- `--update-delay 10s` → wait 10s between batches
- `--update-order start-first` → start new before stopping old

2. Verify: `docker service inspect --pretty web-demo`
3. Update image: `docker service update --image <image>:<tag> web-demo`
    - `docker service ps web-demo` will show old/new task history.
4. Roll back if needed: `docker service rollback web-demo` or `docker service update --rollback web-demo`

### Service-to-service networking
- Create an overlay network (cross-node): `docker network create -d overlay --attachable app-net`
    - `--attachable` allows temporary containers to attach for testing.


### Stacks (Compose on Swarm)
- Deploy: `docker stack deploy -c docker-compose.yml <stack_name>`
    - `-c` (aka --compose-file) is like `-f` in regular Compose, but for Swarm/stack.
- List services in a stack: `docker stack services <stack_name>`
- Remove: `docker stack rm <stack_name>`


