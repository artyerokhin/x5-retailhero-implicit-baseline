# x5-retailhero-implicit-baseline
Implicit baseline for https://retailhero.ai/c/recommender_system/overview

# Baseline задачи рекомендаций с библиотекой implicit

## Как запускать?
1. Если совсем лень - [скачайте](https://drive.google.com/file/d/1-Qw2HNgPQZgcGFNjunzpoObLDhry5fLs/view?usp=sharing) архив;
2. Если хочется свое, то:
  - клонируйте репозиторий
  - обучаете модель с помощью implicit_baseline_model.ipynb модель
  - добавляете в архив папку с pkl моделью, server.py, helpers.py, metadata.json
  - если нужно поменять докер - дейлайте свой образ
3. Для запуска используется свой образ с implicit: artyerokhin/x5_contest_implicit
4. Проверка точно такая же, как и в основном репозитории, только меняется образ docker на образ выше

## Каковы результаты?
1. локальная валидация:
  - average_precision_at_k: 0.021
  - average_normed_precision_at_k: 0.099
2. платформа:
  - check: 0.0938
  - public: 0.0908

## Дополнительно:
1. В этом репозитории сделана валидация, похожая на соревнование - часть пользователей скрыты, у них дополнительно скрыта последняя сессия;
2. На 29.12.2019 baseline дает 11 место на лидерборде
