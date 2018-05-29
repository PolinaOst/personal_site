# -*- coding: utf-8 -*-
import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import os.path


define("port", default=80, help="run on the given port", type=int)
# define("host", default="0.0.0.0")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", RootHandler),
            (r"/about", AboutHandler),
            (r"/education/basic", BasicEducationHandler),
            (r"/education/high", HighEducationHandler),
            (r"/contact", ContactHandler),
            (r"/interests", InterestsHandler),
            (r"/work", WorkHandler),
            (r"/views", ViewsHandler),
            (r"/feedback", FeedbackHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),

            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class BaseHandler(tornado.web.RequestHandler):
    pass


class RootHandler(BaseHandler):
    async def get(self):
        self.render("index.html")


class FeedbackHandler(BaseHandler):
    async def post(self, *args, **kwargs):
        try:
            with open("feedback.txt", "a") as f:
                text = "Имя: {0}\nПол: {1}\nОтзыв: {2}\n\n".format(self.get_argument("name"),
                                                                      self.get_argument("gender"),
                                                                      self.get_argument("feedback"))
                f.write(text)
        except:
            pass
        print()
        self.redirect("/")


class AboutHandler(BaseHandler):
    async def get(self):
        self.render("about.html")


class BasicEducationHandler(BaseHandler):
    async def get(self):
        self.render("basicedu.html")


class HighEducationHandler(BaseHandler):
    async def get(self):
        self.render("highedu.html")


class ContactHandler(BaseHandler):
    async def get(self):
        self.render("contact.html")


class InterestsHandler(BaseHandler):
    async def get(self):
        self.render("interests.html")


class WorkHandler(BaseHandler):
    async def get(self):
        self.render("work.html")


class ViewsHandler(BaseHandler):
    async def get(self):
        self.render("views.html")


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    print("listening...")
    main()
