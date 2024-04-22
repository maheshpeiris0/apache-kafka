
### Step 1: Create the Network
Before running the Docker Compose file, you need to manually create the network named `kafka-network` if it hasn't been created yet. You can do this using the following Docker command:

```bash
docker network create kafka-network
```

This creates a new network using the default `bridge` driver, which is suitable for a setup where containers need to communicate on the same Docker host.

### Step 2: Verify Network Creation
After running the command to create the network, verify that it has been successfully created by listing all networks:

```bash
docker network ls
```

Look for `kafka-network` in the list. If it's there, you're ready to proceed.

### Step 3: Rerun Docker Compose
With the network created, you can now run your Docker Compose file. Navigate to the directory containing your `docker-compose.yml` file and run:

```bash
docker-compose up
```

This should start your services without the network error you encountered previously.

### Troubleshooting

- **Persistent Errors**: If the error persists despite the network being listed in `docker network ls`, double-check the spelling and consistency of the network name in your Docker Compose file.
- **Network Visibility**: Ensure that there are no typos or mismatches in how the network is referenced as `external` in the Docker Compose files of different services that are supposed to connect to this network.
- **Permissions**: Sometimes, permissions or Docker daemon issues can prevent proper network creation or usage. Restarting the Docker service or checking the permissions might help.

### Final Check
Make sure your Docker Compose file correctly declares the network as external if it is indeed managed outside of any individual Docker Compose configuration:

```yaml
networks:
  kafka-network:
    external: true
```

This declaration tells Docker Compose that the network is managed externally and should not attempt to create or remove it when bringing services up or down. By following these steps, you should be able to resolve the network-related error and get your services running as expected.
