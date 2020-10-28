from concurrent import futures

import grpc
import validators

from . import twitter_pb2 as pb2
from . import twitter_pb2_grpc as pb2_grpc
from orakarik.scrape.tweet_scrape import SnTweetScrape


class TwitterStream(pb2_grpc.twitterServicer):

    def StreamRequest(self, request, context):
        result = {'message': 'ok', 'updateAt': '123', 'items': []}
        keyword = validators.length(request.keyword, min=1, max=120)
        search_type = validators.length(request.search_type, min=1, max=25)
        since = validators.length(request.since, min=1, max=30)
        until = validators.length(request.until, min=1, max=30)

        if not keyword:
            result['message'] = f'keyword length must min {keyword.min} max {keyword.max}'
            return pb2.twitterResponse(**result)
        if not search_type:
            result['message'] = f'search_type length must min {search_type.min} max {search_type.max}'
            return pb2.twitterResponse(**result)
        if not since:
            result['message'] = f'since length must min {since.min} max {since.max}'
            return pb2.twitterResponse(**result)
        if not until:
            result['message'] = f'until length must min {until.min} max {until.max}'
            return pb2.twitterResponse(**result)

        if not keyword and not search_type and not since and not until:
            result['message'] = f'[keyword, search_type, since, until] required'
            return pb2.twitterResponse(**result)

        scrape = SnTweetScrape(request.since, request.until)
        if search_type == "account":
            items = scrape.tweetAccount(request.keyword.replace("@", ""))
        elif search_type == "mention":
            items = scrape.tweetSearch(request.keyword)
        elif search_type == "hashtag":
            items = scrape.tweetHashtag(request.keyword.replace("#", ""))
        else:
            items = scrape.tweetSearch(request.keyword)

        result['items'] = items
        return pb2.twitterResponse(**result)


def serve(ports):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    pb2_grpc.add_twitterServicer_to_server(TwitterStream(), server)
    port = server.add_insecure_port(f'[::]:{ports}')
    print("port at {}".format(port))
    server.start()
    server.wait_for_termination()
