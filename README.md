# Auth Flow example


This repo is just an example of how to use [nginx](https://nginx.org/en/) with basic auth.


<!--ts-->
   * [Auth Flow example](#auth-flow-example)
      * [Structure](#structure)
      * [How To](#how-to)

<!-- Added by: jose, at: jue 26 ene 2023 18:09:47 CET -->

<!--te-->

## Structure

```bash
.
├── basic_server.py      # simple python server serving a form
├── docker-compose.yml   # compose with nginx and the python server
├── Makefile
├── nginx                # nginx configurations
│   ├── htpasswd         #  > user:pwd file. see `make gen-pwd`
│   └── local.conf       #  > nginx configuration
└── README.md
```

## How To

1. Generate a user and password for the basic auth:

```bash
make gen-pwd user=alice pwd=12345
```

2. Run both services: `make run`

3. Head to [localhost:8080](http://localhost:8080)
