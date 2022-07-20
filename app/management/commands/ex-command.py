from django.core.management.base import BaseCommand, CommandParser, CommandError
import re
import argparse

class Command(BaseCommand):

    help = 'test custom command called the custom django-admin command'
    
    def __check_org_code (self, i_org_code):
        if len(i_org_code) >2 or len(i_org_code) <=0:
            raise argparse.ArgumentTypeError('f{i_rog_code} is not a vliad code. Note that length of code is 2!')
        return i_org_code[:2]

    def __check_org_area (self, i_org_area):
        if not re.match('^[0-9]+$',i_org_area):
            raise argparse.ArgumentTypeError('f{i_org_area} is not a vliad area code. (only digit is allowed.')
        return i_org_area

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--name', 
                            #nargs='1', 
                            type=str, help='organization\' name')
        parser.add_argument('--id', 
                            #nargs='1', 
                            type=str, help='organization\' id')
        parser.add_argument('--path', help='file path')

        # TODO 2022.07.20 added by dsaint31!

        parser.add_argument("--org", type=str, default="KNU")
        parser.add_argument("--org_code", type=self.__check_org_code, default="ZZ", help="organization code, such as QH")
        parser.add_argument("--org_area", type=self.__check_org_area, default="00", help="organization area code, such as 02")

    def handle(self, *args, **options):
        print(args)
        print('-------------')
        print(options)
