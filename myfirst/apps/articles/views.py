# # # myfirst/apps/articles/views.py
# # from django.shortcuts import render
# # from .models import MyProfile

# # def about_me(request):
# #     # Явно берем самую первую запись из таблицы MyProfile
# #     profile = MyProfile.objects.all().first()
    
# #     # Если Django всё ещё не видит запись, проверим её наличие
# #     if not profile:
# #         my_data = {
# #             "name": "Данные не заполнены",
# #             "role": "Зайдите в /admin/",
# #             "bio": "Создайте запись в панели управления Django, чтобы она появилась здесь.",
# #             "skills": [],
# #             "github": "#",
# #             "telegram": "#"
# #         }
# #     else:
# #         # Превращаем строку навыков в красивый список, убирая лишние пробелы
# #         skills_list = [s.strip() for s in profile.skills.split(',')] if profile.skills else []
        
# #         my_data = {
# #             "name": profile.name,
# #             "role": profile.role,
# #             "bio": profile.bio,
# #             "skills": skills_list,
# #             "github": profile.github,
# #             "telegram": profile.telegram
# #         }

# #     return render(request, 'articles/index.html', {'user': my_data})

# # myfirst/apps/articles/views.py
# from django.shortcuts import render
# from .models import MyProfile

# def about_me(request):
#     # Запрашиваем абсолютно все записи из таблицы профилей
#     all_profiles = MyProfile.objects.all()
    
#     # Считаем, сколько записей реально лежит в базе данных
#     profiles_count = all_profiles.count()
    
#     if profiles_count == 0:
#         # Если в базе пусто, мы выведем это прямо на экран!
#         my_data = {
#             "name": f"В базе 0 записей!",
#             "role": "Проверьте админку",
#             "bio": "Вы сохранили профиль, но база данных пуста. Зайдите в /admin/ и нажмите Добавить.",
#             "skills": ["Ошибка"],
#             "github": "#",
#             "telegram": "#"
#         }
#     else:
#         # Если записи есть, берем самую последнюю измененную
#         profile = all_profiles.last()
        
#         skills_list = [s.strip() for s in profile.skills.split(',')] if profile.skills else []
        
#         my_data = {
#             "name": profile.name,
#             "role": profile.role,
#             "bio": profile.bio,
#             "skills": skills_list,
#             "github": profile.github,
#             "telegram": profile.telegram
#         }

#     return render(request, 'articles/index.html', {'user': my_data})


# myfirst/apps/articles/views.py
from django.shortcuts import render

def about_me(request):
    my_data = {
        "name": "Никулина Нелли Витальевна",  
        "role": "Python Разработчик",
        "bio": "Я успешно настроила бэкенд на Django и подключила стили Tailwind!",
        "skills": ["Python", "Django", "Git", "HTML", "CSS"],
        "github": "https://github.com/mayfau",
        "telegram": "https://t.me/eclipseij"
    }
    return render(request, 'articles/index.html', {'user': my_data})
