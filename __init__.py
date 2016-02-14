# -*- coding: utf-8 -*-
__author__ = 'alsbi'

from dockerlib import Base



# print Api.info()



# for i in  Base.show_container_all():
#    print i

# for i in  Base.show_images():
#    print i


for i in Base.show_images_history('8693db7e8a0084b8aacba184cfc4ff9891924ed2270c6dec6a9d99bdcff0d1aa'):
    print i

    # print Container(uid='')
