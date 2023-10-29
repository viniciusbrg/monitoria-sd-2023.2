
# Execution

1. Create virtualenv 

`python3 -m venv venv`

2. Activate virtualenv 

`source venv/bin/activate`

3. Install protobuf tools

```bash
pip install grpcio
pip install grpcio-tools
```

To run the example, psutil is also needed: `pip install psutil`

4. Compile GRPC

At the python folder, execute
`python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. Sensors.proto` 

5. Run server

`python server.py`

6. Run client

`python client.py`