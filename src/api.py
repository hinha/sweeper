import os
from sanic import Sanic
from sanic import response

from .twitter import services

app = Sanic(__name__)
rpc_host = os.environ.get("RPC_HOST", "0.0.0.0")


@app.route("/", methods=["GET"])
async def index(request):
    return response.json({"msg": "ok"})


@app.route("/twitter", methods=["POST"])
async def twitter_rpc(request):
    payload = {
        "keyword": request.json.get("text", ""),
        "search_type": request.json.get("type", ""),
        "since": request.json.get("since", ""),
        "until": request.json.get("until", ""),
        "proxy": request.json.get("proxy", "")
    }
    client = services.Rpc(host=rpc_host, port="50081")
    responses = client.Stream(payload)

    return response.json(responses)


def rest_api(port: int, worker):
    app.run(host="0.0.0.0", port=port, workers=worker)
