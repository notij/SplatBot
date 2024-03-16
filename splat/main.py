try:
    from splat.crawler import *
    from splat.renderer import *
    from splat.random import *
except:
    from crawler import *
    from renderer import *
    from random import *


class SplatBot():
    def __init__(self, URL):
        global images
        self.images = URL +"/splat/images/"
        self.data = URL + "/splat/data"
    
    def get_regular(self,tz = "东部"):
        update()
        li = parse_regular(tz)[:5*2]
        return render_battle(li, tz,self.images)

    def get_challenge(self, tz = "东部"):
        update()
        li = parse_challenge(tz)[:5*2]
        return render_zg(li, tz,self.images)

    def get_open(self, tz = "东部"):
        update()
        li = parse_open(tz)[:5*2]
        return render_zg(li, tz,"真格开放",self.images)

    def get_coop(self, tz:str = "东部"):
        tz = "东部"
        update()
        li = parse_coop(tz)
        return render_coop(li, tz,self.images)

    def get_x(self,tz = "东部"):
        update()
        li = parse_x(tz)[:5*2]
        return render_zg(li, tz, "X比赛",self.images)


    def get_random(self, arg):
        li = get_random(arg)
        return render_random(li)

