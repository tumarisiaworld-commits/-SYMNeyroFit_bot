import asyncio
import logging
from html import escape

from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    FSInputFile,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

# =====================================================================
# КОНФИГУРАЦИЯ
# =====================================================================
BOT_TOKEN = "8661354702:AAGKX1mPbjDPeTOAb3orPP1RctKlzg_EAbg"
ADMIN_CHAT_ID = 7237274092  # Ваш числовой Telegram ID
PERSONAL_ACCOUNT_LINK = "https://t.me/MiSsNur01"  # Ссылка для покупки

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


# =====================================================================
# ШАГ 1: СТАРТ И ВЫЗОВ БОЛИ (photo1.jpg)
# =====================================================================
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    caption = (
        "💭 <b>«Почему я пашу на тренировках, а желаемого рельефа и лёгкости всё нет?»</b>\n\n"
        "Знакомо ощущение, когда от силовой нагрузки в зале тело становится только тяжелее, "
        "а отеки и зажимы в пояснице не уходят?\n\n"
        "Всё дело в том, что стандартный фитнес часто перегружает суставы и зажимает лимфу. "
        "Если не дать телу правильную вытяжку и работу с осанкой, энергия просто уходит в слив.\n\n"
        "👇 <i>Нажмите кнопку ниже, чтобы увидеть, как работает эффективная система:</i>"
    )

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="▶️ Узнать секрет здорового тела", callback_data="step_2"
                )
            ]
        ]
    )

    try:
        photo = FSInputFile("photo1.jpg")
        await message.answer_photo(
            photo=photo, caption=caption, reply_markup=kb, parse_mode=ParseMode.HTML
        )
    except Exception:
        # Резервный вариант, если файла photo1.jpg нет в папке
        await message.answer(caption, reply_markup=kb, parse_mode=ParseMode.HTML)


# =====================================================================
# ШАГ 2: РЕЗУЛЬТАТ И ЖЕНСТВЕННОСТЬ (photo2.jpg)
# =====================================================================
@dp.callback_query(F.data == "step_2")
async def process_step_2(callback: types.CallbackQuery):
    await callback.answer()

    caption = (
        "✨ <b>Ровная осанка, подтянутый живот и свобода в каждом движении</b>\n\n"
        "Настоящая женская сексуальность и магнетизм начинаются не с изнуряющих диет, "
        "а с <b>раскрытия грудного отдела и здорового позвоночника</b>.\n\n"
        "Когда уходит зажатость, тело мгновенно меняется:\n"
        "• Исчезает выпирающий животик и отечность.\n"
        "• Появляется гибкость, грация и королевская осанка.\n"
        "• Вы чувствуете прилив сил и легкую энергию!"
    )

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔥 Хочу такую уверенность!", callback_data="step_3"
                )
            ]
        ]
    )

    try:
        photo = FSInputFile("photo2.jpg")
        await callback.message.answer_photo(
            photo=photo, caption=caption, reply_markup=kb, parse_mode=ParseMode.HTML
        )
    except Exception:
        await callback.message.answer(caption, reply_markup=kb, parse_mode=ParseMode.HTML)


# =====================================================================
# ШАГ 3: ЯРКАЯ ЖИЗНЬ И УВЕРЕННОСТЬ (photo3.jpg)
# =====================================================================
@dp.callback_query(F.data == "step_3")
async def process_step_3(callback: types.CallbackQuery):
    await callback.answer()

    caption = (
        "🔥 <b>Тело, которое притягивает взгляды и дает уверенность</b>\n\n"
        "Когда ваше тело работает как единая гармоничная система, вам больше не нужно «прятаться» под оверсайз-одеждой.\n\n"
        "Вы кайфуете от своего отражения в зеркале, легко носите открытые купальники и чувствуете себя "
        "на 100% уверенно в любой обстановке — на отдыхе, на пляже, в бизнесе и в жизни!"
    )

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⚡ В чем секрет методики?", callback_data="step_4"
                )
            ]
        ]
    )

    try:
        photo = FSInputFile("photo3.jpg")
        await callback.message.answer_photo(
            photo=photo, caption=caption, reply_markup=kb, parse_mode=ParseMode.HTML
        )
    except Exception:
        await callback.message.answer(caption, reply_markup=kb, parse_mode=ParseMode.HTML)


# =====================================================================
# ШАГ 4: ЭКСПЕРТНОСТЬ И НЕЙРО-ФИТНЕС (video1.mp4)
# =====================================================================
@dp.callback_query(F.data == "step_4")
async def process_step_4(callback: types.CallbackQuery):
    await callback.answer()

    caption = (
        "🧠 <b>Нейро-гимнастика & Умный фитнес: Работа на результат</b>\n\n"
        "Моя методика — это не просто качание пресса. Это система <b>SYM SPORT & Нейро-фитнеса</b>, "
        "основанная на профессиональном спортивном опыте и биомеханике:\n\n"
        "🔹 <b>Бережная растяжка</b> и глубокая проработка связок без боли.\n"
        "🔹 <b>Активация глубоких мышц-стабилизаторов</b> для плоского живота.\n"
        "🔹 <b>Снятие зажимов и отечности</b> через работу с лимфотоком.\n\n"
        "Достаточно 20–30 минут системных онлайн-занятий в день, чтобы запустить глубокую трансформацию!"
    )

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💎 Перейти к оформлению участия", callback_data="step_5"
                )
            ]
        ]
    )

    try:
        video = FSInputFile("video1.mp4")
        await callback.message.answer_video(
            video=video, caption=caption, reply_markup=kb, parse_mode=ParseMode.HTML
        )
    except Exception:
        await callback.message.answer(caption, reply_markup=kb, parse_mode=ParseMode.HTML)


# =====================================================================
# ШАГ 5: ПРОДАЖА И ПЕРЕАДРЕСАЦИЯ НА ЛИЧНЫЙ АККАУНТ (photo4.jpg)
# =====================================================================
@dp.callback_query(F.data == "step_5")
async def process_step_5(callback: types.CallbackQuery):
    await callback.answer()

    caption = (
        "🎯 <b>Готовы к первому шагу к телу мечты?</b>\n\n"
        "Забудьте про скучные тренировки и боли в спине. Начните заниматься по умной системе прямо из дома в удобное для вас время!\n\n"
        "🎁 <b>Для участников бота открыт доступ к персональным онлайн-занятиям и авторским Нейро-Протоколам.</b>\n\n"
        "👇 Нажмите кнопку ниже, чтобы перейти в личный чат со мной, задать вопросы и забронировать место на занятия:"
    )

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Купить онлайн-занятия (@MiSsNur01)",
                    url=PERSONAL_ACCOUNT_LINK,
                )
            ]
        ]
    )

    try:
        photo = FSInputFile("photo4.jpg")
        await callback.message.answer_photo(
            photo=photo, caption=caption, reply_markup=kb, parse_mode=ParseMode.HTML
        )
    except Exception:
        await callback.message.answer(caption, reply_markup=kb, parse_mode=ParseMode.HTML)

    # Уведомление вам администратору
    user_info = (
        f"@{callback.from_user.username}"
        if callback.from_user.username
        else "без username"
    )
    admin_alert = (
        "💰 <b>КЛИЕНТ ДОШЕЛ ДО ПОКУПКИ В БОТЕ!</b>\n\n"
        f"👤 <b>Пользователь:</b> {escape(callback.from_user.full_name)} ({user_info})\n"
        f"🆔 <b>ID:</b> <code>{callback.from_user.id}</code>\n"
        "Статус: Перенаправлен на покупку в личные сообщения."
    )

    try:
        await bot.send_message(ADMIN_CHAT_ID, admin_alert, parse_mode=ParseMode.HTML)
    except Exception as e:
        logging.error(f"Ошибка отправки уведомления: {e}")


# =====================================================================
# ЗАПУСК
# =====================================================================
async def main():
    print("Бот с продающей медиа-воронкой успешно запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())