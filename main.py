

import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
import time
import datetime
import config
import commands


vk = vk_api.VkApi(token = config.token)
longpoll = VkLongPoll(vk)

def get_keyboard(path):
    keyboard = open(f"keyboards/{path}.json", "r", encoding="utf-8").read()
    return keyboard

def send_msg(user_id, message, keyboard = None):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        print(msg, "-", user_id)
        if msg == 'хочу получить заём':
          send_msg(user_id, 'Вы хотели бы обратиться онлайн или офлайн?', get_keyboard('main'))
          for event in longpoll.listen():
              if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                  msg = event.text.lower()
                  if msg == 'онлайн':
                    send_msg(user_id, 'Обратите внимание, что онлайн Вы можете получить услугу только у МФК и МКК.', get_keyboard('online'))
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                            msg = event.text.lower()
                            if msg == 'я передумал(а), хочу офлайн':
                                send_msg(user_id,'Как часто Вы хотите пользоваться услугами? Если регулярно, то лучше стать членом КПК/СКПК и получать услугу в любой удобный момент!',get_keyboard('ofline'))
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                        msg = event.text.lower()
                                        if msg == 'регулярно':
                                            send_msg(user_id, 'Вы занимаетесь сельскохозяйственной деятельностью?',
                                                     get_keyboard('yesno'))
                                            for event in longpoll.listen():
                                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                                    msg = event.text.lower()
                                                    if msg == 'да':
                                                        send_msg(user_id, 'Информация о филиалах и режимах работы СКПК')
                                                        send_msg(user_id,
                                                                 'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт для дальнейших действий ссылка на сайт')
                                                    elif msg == 'нет':
                                                        send_msg(user_id, 'Информация о филиалах и режимах работы КПК')
                                                        send_msg(user_id,
                                                                 'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт для дальнейших действий ссылка на сайт')

                                        elif msg == 'пока разово':
                                            send_msg(user_id,
                                                     'Тогда предлагаю Вам воспользоваться услугами МФК, МКК или Ломбарда.\n\n Информация о филиалах и режимах работы')
                                            send_msg(user_id, 'Не хотели бы вы вступить в КПК/СКПК?',
                                                     get_keyboard('regulary'))
                                            for event in longpoll.listen():
                                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                                    msg = event.text.lower()
                                                    if msg == 'хотел(-а) бы':
                                                        send_msg(user_id,
                                                                 'Вы занимаетесь сельскохозяйственной деятельностью?',
                                                                 get_keyboard('yesno'))
                                                        for event in longpoll.listen():
                                                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                                                msg = event.text.lower()
                                                                if msg == 'да':
                                                                    send_msg(user_id,
                                                                             'Информация о филиалах и режимах работы СКПК')
                                                                    send_msg(user_id,
                                                                             'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт для дальнейших действий ссылка на сайт')
                                                                elif msg == 'нет':
                                                                    send_msg(user_id,
                                                                             'Информация о филиалах и режимах работы КПК')
                                                                    send_msg(user_id,
                                                                             'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт для дальнейших действий ссылка на сайт')

                                                    elif msg == 'не хотел(-а) бы':
                                                        send_msg(user_id,
                                                                 'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт для дальнейших действий ссылка на сайт')

                            elif msg == 'хорошо, продолжить':
                                send_msg(user_id,'Введите желаемую сумму',get_keyboard('skip'))
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                        msg = event.text.lower()
                                        send_msg(user_id, 'Введите желаемый процент', get_keyboard('skip'))
                                        for event in longpoll.listen():
                                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                                msg = event.text.lower()
                                                send_msg(user_id, 'Введите желаемый срок', get_keyboard('skip'))
                                                for event in longpoll.listen():
                                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                                        msg = event.text.lower()
                                                        send_msg(user_id, 'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт, где для Вас подобраны подходящие организации ссылка на сайт')


                  elif msg == 'офлайн':
                    send_msg(user_id, 'Как часто Вы хотите пользоваться услугами? Если регулярно, то лучше стать членом КПК/СКПК и получать услугу в любой удобный момент!',get_keyboard('ofline'))
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                            msg = event.text.lower()
                            if msg == 'регулярно':
                                send_msg(user_id,'Вы занимаетесь сельскохозяйственной деятельностью?',get_keyboard('yesno'))
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                        msg = event.text.lower()
                                        if msg == 'да':
                                            send_msg(user_id, 'Информация о филиалах и режимах работы СКПК')
                                            send_msg(user_id,
                                                     'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт для дальнейших действий ссылка на сайт')
                                        elif msg == 'нет':
                                            send_msg(user_id, 'Информация о филиалах и режимах работы КПК')
                                            send_msg(user_id,
                                                     'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт для дальнейших действий ссылка на сайт')

                            elif msg == 'пока разово':
                                send_msg(user_id,'Тогда предлагаю Вам воспользоваться услугами МФК, МКК или Ломбарда.\n\n Информация о филиалах и режимах работы')
                                send_msg(user_id,'Не хотели бы вы вступить в КПК/СКПК?', get_keyboard('regulary'))
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                        msg = event.text.lower()
                                        if msg == 'хотел(-а) бы':
                                            send_msg(user_id, 'Вы занимаетесь сельскохозяйственной деятельностью?', get_keyboard('yesno'))
                                            for event in longpoll.listen():
                                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                                    msg = event.text.lower()
                                                    if msg == 'да':
                                                        send_msg(user_id, 'Информация о филиалах и режимах работы СКПК')
                                                        send_msg(user_id, 'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт для дальнейших действий ссылка на сайт')
                                                    elif msg == 'нет':
                                                        send_msg(user_id, 'Информация о филиалах и режимах работы КПК')
                                                        send_msg(user_id,'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт для дальнейших действий ссылка на сайт')

                                        elif msg == 'не хотел(-а) бы':
                                            send_msg(user_id, 'На этом мои полномочия заканчиваются:( Предлагаю Вам перейти на наш сайт для дальнейших действий ссылка на сайт')


