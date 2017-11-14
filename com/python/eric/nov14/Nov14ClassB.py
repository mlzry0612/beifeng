class Run:
    def run(self):
        print("RUN")

class Jump:
    def jump(self):
        print("JUMP")


class  Sport(Run, Jump):
    pass


sport = Sport()
sport.jump()
sport.run()