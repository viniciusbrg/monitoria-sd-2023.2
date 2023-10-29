const protoLoader = require("@grpc/proto-loader");
const grpc = require("@grpc/grpc-js");

function loadStub() {
    var PROTO_PATH = 'Sensors.proto';
    // Suggested options for similarity to existing grpc.load behavior
    var packageDefinition = protoLoader.loadSync(
        PROTO_PATH,
        {keepCase: true,
            longs: String,
            enums: String,
            defaults: true,
            oneofs: true
        });
    var protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
    // The protoDescriptor object has the full package hierarchy

    var sensors = protoDescriptor.Sensors;

    return new sensors('localhost:15000', grpc.credentials.createInsecure());
}

const stub = loadStub()

function simpleRpc() {
    stub.getMeasure({ reqId: 1, sensorType: 1 }, function (err, result) {
        console.log(err)
        console.log(result)
    })
}

function serverStreamingRpc() {
    var call = stub.getMeasuresStream({ calls: 10, sensorType: 0 });

    call.on('data', function(data) {
        console.log(data)
    });
    call.on('end', function() {
        console.log("done")
    });
    call.on('error', function(e) {
        // An error has occurred and the stream has been closed.
    });
    call.on('status', function(status) {
        // process status
    });
}

// simpleRpc()
serverStreamingRpc()