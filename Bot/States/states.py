from telebot.asyncio_handler_backends import State, StatesGroup

class MyStates(StatesGroup):
    main_menu=State()

    manage_plans=State()
    load_cp_file=State()
    add_plan_position=State()
    del_plan_position=State()
    manualy_posting=State()

    content_plan_change=State()
    content_plan_change_title=State()
    content_plan_change_content=State()
    content_plan_change_image_status=State()
    content_plan_change_temperature=State()

    add_admin=State()
    reposting=State()