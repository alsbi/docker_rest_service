Service allows you to manage the container: start, stop , view logs

By default:

- used docker
- socket transport
- without authorization

# Usage
run packages docker_rest_service 

## Use non-docker engine
- Create custom transport class from service.engine.transport
- Add you custom class to service.engine (Service_name, Container_name), 
inherit you new class from  dockerlib.base.BaseService and dockerlib.container.BaseContainer
- Create instance CurrentEngine(you Base_class)
