import grpc
from google.protobuf.json_format import ParseDict

from src import twitter_pb2 as pb
from src import twitter_pb2_grpc as pb2_grpc


def run_twitter():
    channel = grpc.insecure_channel("[::]:50055")
    stub = pb2_grpc.twitterStub(channel)

    payload = {
        "keyword": "@hrdbacot",
        "search_type": "mention",
        "since": "2020-10-11",
        "until": "2020-10-26"
    }

    request = ParseDict(payload, pb.twitterRequest())
    stub.StreamRequest(request)



if __name__ == '__main__':
    run_twitter()
