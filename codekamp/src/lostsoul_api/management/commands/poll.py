from django.core.management import BaseCommand

from lostsoul_api.tasks import analyze_tweet


class Command(BaseCommand):

    def pollFacebook(self):
        print("polling facebook")

    def pollTwitter(self):
        analyze_tweet.delay(11)
        analyze_tweet.apply_async((99,), countdown=10)

    # def add_arguments(self, parser):
    #     parser.add_argument('parent_id', type=int)
    #     parser.add_argument('child_id', type=int)
    #     parser.add_argument('--something')
    #     parser.add_argument('--anything')

    def handle(self, *args, **options):
        # print(options["child_id"])
        # print(options["parent_id"])
        # print(options["something"])
        # print(options["anything"])
        self.pollFacebook()
        self.pollTwitter()


# https://github.com/conversationai/perspectiveapi/blob/master/quickstart.md
# https://www.perspectiveapi.com/#/

# https://github.com/BradWhittington/django-mailgun