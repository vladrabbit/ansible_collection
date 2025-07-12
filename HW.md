# Домашнее задание к занятию 6 «Создание собственных модулей»


## Основная часть

**Результат** В ответ необходимо прислать ссылки на collection и tar.gz архив, а также скриншоты выполнения пунктов 4, 6, 15 и 16.


---


## Результат + Скриншоты выполнения шагов 4, 6 ,15 ,16

**Шаг 4.** Проверьте module на исполняемость локально.
           Выполнение производилось на удаленном хосте YC

![Выполнение модуля](https://github.com/vladrabbit/ansible_collection/blob/main/.sh/module-1.png)

**Шаг 6.** Проверьте через playbook на идемпотентность. 

![Идемпотентность](https://github.com/vladrabbit/ansible_collection/blob/main/.sh/mod-2.png)

**Шаг 15.** Установите collection из локального архива: `ansible-galaxy collection install <archivename>.tar.gz`.

![Установка](https://github.com/vladrabbit/ansible_collection/blob/main/.sh/mod-3.1.png)

**Шаг 16.** Запустите playbook, убедитесь, что он работает.

![Запуск playbook](https://github.com/vladrabbit/ansible_collection/blob/main/.sh/mod-3.png)
---