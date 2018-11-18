class DemoException(Exception):

    def demo_exc_handling(self):
        print('coroutine is starting')
        while True:
            try:
                x = yield
            except DemoException:
                print('demo exception handled')
            else:
                print('-> continuing received:{!r}'.format(x))
