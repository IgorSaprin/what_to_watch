from flask import render_template

from . import app, db


@app.errorhandler(500)
def internal_error(error):
    # Ошибка 500 возникает в нештатных ситуациях на сервере.
    # Например, провалилась валидация данных.
    # В таких случаях можно откатить изменения, не зафиксированные в БД,
    # чтобы в базу не записалось ничего лишнего.
    db.session.rollback()
    # Пользователю вернётся страница, сгенерированная на основе
    # шаблона 500.html и код HTTP-ответа 500.
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(error):
    # При ошибке 404 в качестве ответа вернётся страница, созданная
    # на основе шаблона 404.html, и код HTTP-ответа 404:
    return render_template('404.html'), 404
