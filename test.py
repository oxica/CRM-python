def test_main(user_ns):
    from unittest.mock import MagicMock

    main = user_ns["main"]
    app = user_ns["app"]
    app.run = MagicMock(return_value=None)
    try:
        main()
        try:
            app.run.assert_called_once()
        except AssertionError:
            raise AssertionError("Сервер не запуститься, якщо не викликати app.run")

        try:
            app.run.assert_called_once_with(host="0.0.0.0", port=8080)
        except AssertionError:
            raise AssertionError(
                "Сервер на запущено не порту 8080, або він не "
                "доступний всім комп'ютерам мережі."
            )
    except AssertionError:
        raise
    except Exception as exc:
        raise Exception(f"Виклик функції main призводить по помилки: {str(exc)}")
    return "Сервер доступний всім комп'ютерам в мережі на порту 8080"
