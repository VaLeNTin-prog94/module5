import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return self.password


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode




class UrTube:
    def __init__(self):
        self.current_time_now = None
        self.current_duration = None
        self.get_video = None
        self.verify_user = None
        self.user = None
        self.age = None
        self.password = None
        self.nickname = None
        self.my_search_list = None
        self.search_video = None
        self.videos1 = []
        self.users = []
        self.videos = []
        self.current_user = None

    def add(self, *args):
        video = []
        videos1 = []
        check_video = False
        for i in args:
            video = i.title
            video1 = [i.title, i.duration, i.adult_mode]
            if not self.videos:
                self.videos.append(video)
                self.videos1.append(video1)
            else:
                for j in self.videos:
                    if i.title != j[0]:
                        check_video = True
                    else:
                        check_video = False
                        break
                if check_video:
                    self.videos.append(video)
                    self.videos1.append(video1)
                else:
                    print(f'Фильм {i.title} уже существует!!!')

    def get_videos(self, search_video):
        self.search_video = search_video
        self.my_search_list = []
        for i in self.videos:
            if search_video.lower() in i.lower():
                self.my_search_list.append(i)
        return self.my_search_list

    def watch_video(self, get_video):
        self.get_video = get_video
        if self.current_user is None:
            print('Войдите в аккаунт для просмотра видео')
        else:
            if self.current_user is not None:
                for i in self.videos1:
                    if i[0] == self.get_video and i[2]:
                        self.current_duration = i[1]
                        if self.age > 18:
                            print(f'Воспроизводится :{self.get_video}')
                            for j in range(1,self.current_duration+1):
                                self.current_time_now = j
                                print(end=" ")
                                print(self.current_time_now, sep=" ", end=" ")
                            time.sleep(1)
                            print('Конец видео')
                            time.sleep(2)
                        else:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')

    def log_out(self,current_user):
        self.current_user=None
    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        self.user = [self.nickname, self.password, self.age]
        self.verify_user = 0
        for i in self.users:
            if i[0] == self.nickname:
                self.log_in(self.nickname, self.password)
        if self.verify_user == 0:
            self.users.append(self.user)
            self.current_user = self.nickname
        elif self.verify_user == 1:
            print(f"Пользователь {self.nickname} авторизован")
        elif self.verify_user == 2:
            print(f'Пользователь {self.nickname} уже существует')

    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = password
        for i in self.users:
            if i[0] == self.nickname and i[1] == self.password:
                self.current_user = self.nickname
                self.verify_user = 1
            elif i[0] == self.nickname and i[1] != self.password:
                self.verify_user = 2


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')