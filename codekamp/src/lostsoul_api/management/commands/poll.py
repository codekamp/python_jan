from django.core.management import BaseCommand


class Command(BaseCommand):

    def pollFacebook(self):
        print("polling facebook")

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


# https://github.com/conversationai/perspectiveapi/blob/master/quickstart.md
# https://www.perspectiveapi.com/#/

# https://github.com/BradWhittington/django-mailgun