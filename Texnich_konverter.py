import tkinter
from tkinter import ttk


def converters(event):
    conv_etr1.delete(0, tkinter.END)  # очищаем поле Entry
    conv_etr2.delete(0, tkinter.END)
    if converter.get() == "массовый расход":
        conv_lable.config(text="Расход, м3/ч: \n\nПлотность, кг/м3: \n\nРезультат: т/ч:")
        conv_etr2.config(state="normal")
    elif converter.get() == "объемный расход":
        conv_lable.config(text="Расход, т/ч: \n\nПлотность, кг/м3: \n\nРезультат: м3/ч:")
        conv_etr2.config(state="normal")
    elif converter.get() == "л/сек в м3/ч":
        conv_lable.config(text="Расход, л/сек: \n\n\n\nРезультат: м3/ч:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "м3/ч в л/сек":
        conv_lable.config(text="Расход, м3/ч: \n\n\n\nРезультат: л/сек:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "л/мин в м3/ч":
        conv_lable.config(text="Расход, л/мин: \n\n\n\nРезультат: м3/ч:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "м3/ч в л/мин":
        conv_lable.config(text="Расход, м3/ч: \n\n\n\nРезультат: л/мин:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "кг/ч в м3/ч":
        conv_lable.config(text="Расход, кг/ч: \n\nПлотность, кг/м3: \n\nРезультат: м3/ч:")
        conv_etr2.config(state="normal")
    elif converter.get() == "м3/ч в кг/ч":
        conv_lable.config(text="Расход, м3/ч: \n\nПлотность, кг/м3: \n\nРезультат: кг/ч:")
        conv_etr2.config(state="normal")
    elif converter.get() == "кинематич. в динамич. вязкость":
        conv_lable.config(text="Кин. вяз., мм2/с(сСт): \n\nПлотность, кг/м3: "
                               "\n\nРезультат: Дин. вяз. сП(мПа*с):")
        conv_etr2.config(state="normal")
    elif converter.get() == "динамич. в кинематич. вязкость":
        conv_lable.config(text="Дин. вяз., сП(мПа*с): \n\nПлотность, кг/м3: "
                               "\n\nРезультат: Кин. вяз. мм2/с(сСт):")
        conv_etr2.config(state="normal")
    elif converter.get() == "атмосферы в метры":
        conv_lable.config(text="Давление, атм.: \n\n\n\nРезультат: Давление, м.:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "метры в атмосферы":
        conv_lable.config(text="Давление, м.: \n\n\n\nРезультат: Давление, атм.:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "атмосферы в кгс":
        conv_lable.config(text="Давление, атм.: \n\n\n\nРезультат: Давление, кгс/см2:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "кгс в атмосферы":
        conv_lable.config(text="Давление, кгс/см2: \n\n\n\nРезультат: Давление, атм.:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "атмосферы в МПа":
        conv_lable.config(text="Давление, атм.: \n\n\n\nРезультат: Давление, МПа:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "МПа в атмосферы":#
        conv_lable.config(text="Давление, МПа: \n\n\n\nРезультат: Давление, атм.:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "физ. атм в техническую атм":
        conv_lable.config(text="Физ. атмосфера, атм.: \n\n\n\nРезультат: Тех. атм., ат.:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "техническую атм в физ. атм":
        conv_lable.config(text="Тех. атмосфера, ат.: \n\n\n\nРезультат: Физ. атм., атм.:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "техническую атм в МПа":
        conv_lable.config(text="Тех. атмосфера, ат.: \n\n\n\nРезультат: Давление, МПа:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "МПа в техническую атм":
        conv_lable.config(text="Давление, МПа: \n\n\n\nРезультат: Тех. атмосфера, ат.:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "МПа в кгс/см2":
        conv_lable.config(text="Давление, МПа: \n\n\n\nРезультат: Давление, кгс/см2:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "кгс/см2 в МПа":
        conv_lable.config(text="Давление, кгс/см2: \n\n\n\nРезультат: Давление, МПа:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "ккал в Дж":
        conv_lable.config(text="Энергия(Работа), ккал.: \n\n\n\nРезультат: Энергия(Работа), Дж:")
        conv_etr2.config(state="disabled")
    elif converter.get() == "Дж в ккал":
        conv_lable.config(text="Энергия(Работа), Дж.: \n\n\n\nРезультат: Энергия(Работа), ккал:")
        conv_etr2.config(state="disabled")


def resultat():
    if converter.get() == "массовый расход":
        conv_lable.config(text=f"Расход, м3/ч: \n\nПлотность, кг/м3: \n\nРезультат: т/ч: "
                               f"\t{(float(conv_etr1.get().replace(",", ".")) * float(conv_etr2.get().replace(",", "."))) / 1000}")
    elif converter.get() == "объемный расход":
        conv_lable.config(text=f"Расход, т/ч: \n\nПлотность, кг/м3: \n\nРезультат: м3/ч: "
                               f"\t{(float(conv_etr1.get().replace(",", ".")) / float(conv_etr2.get().replace(",", "."))) * 1000}")
    elif converter.get() == "л/сек в м3/ч":
        conv_lable.config(text=f"Расход, л/сек: \n\n\n\nРезультат: м3/ч: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * 3.6}")
    elif converter.get() == "м3/ч в л/сек":
        conv_lable.config(text=f"Расход, м3/ч: \n\n\n\nРезультат: л/сек: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / 3.6}")
    elif converter.get() == "л/мин в м3/ч":
        conv_lable.config(text=f"Расход, л/мин: \n\n\n\nРезультат: м3/ч: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * 0.06}")
    elif converter.get() == "м3/ч в л/мин":
        conv_lable.config(text=f"Расход, м3/ч: \n\n\n\nРезультат: л/мин: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / 0.06}")
    elif converter.get() == "кг/ч в м3/ч":
        conv_lable.config(text=f"Расход, кг/ч: \n\nПлотность, кг/м3: \n\nРезультат: м3/ч: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / float(conv_etr2.get().replace(",", "."))}")
    elif converter.get() == "м3/ч в кг/ч":
        conv_lable.config(text=f"Расход, м3/ч: \n\nПлотность, кг/м3: \n\nРезультат: кг/ч: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * float(conv_etr2.get().replace(",", "."))}")
    elif converter.get() == "кинематич. в динамич. вязкость":
        conv_lable.config(text=f"Кин. вяз., мм2/с(сСт): \n\nПлотность, кг/м3: \n\nРезультат: "
                               f"Дин. вяз. сП(мПа*с): "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * 
                                    float(conv_etr2.get().replace(",", ".")) / 1000}")
    elif converter.get() == "динамич. в кинематич. вязкость":
        conv_lable.config(text=f"Дин. вяз., сП(мПа*с): \n\nПлотность, кг/м3: \n\nРезультат: "
                               f"Кин. вяз. мм2/с(сСт): "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / float(conv_etr2.get().replace(",", ".")) * 1000}")
    elif converter.get() == "атмосферы в метры":
        conv_lable.config(text=f"Давление, атм.: \n\n\n\nРезультат: Давление, м.: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * 10.33227}")
    elif converter.get() == "метры в атмосферы":
        conv_lable.config(text=f"Давление, м.: \n\n\n\nРезультат: Давление, атм.: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / 10.33227}")
    elif converter.get() == "атмосферы в кгс":
        conv_lable.config(text=f"Давление, атм.: \n\n\n\nРезультат: Давление, кгс/см2: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * 1.0332275652715683}")
    elif converter.get() == "кгс в атмосферы":
        conv_lable.config(text=f"Давление, кгс/см2: \n\n\n\nРезультат: Давление, атм.: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / 1.0332275652715683}")
    elif converter.get() == "атмосферы в МПа":
        conv_lable.config(text=f"Давление, атм.: \n\n\n\nРезультат: Давление, МПа: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * 0.101325}")
    elif converter.get() == "МПа в атмосферы":
        conv_lable.config(text=f"Давление, МПа: \n\n\n\nРезультат: Давление, атм.: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / 0.101325}")
    elif converter.get() == "физ. атм в техническую атм":
        conv_lable.config(text=f"Физ. атмосфера, атм.: \n\n\n\nРезультат: Тех. атм., ат.: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * 1.0332274528}")
    elif converter.get() == "техническую атм в физ. атм":
        conv_lable.config(text=f"Тех. атмосфера, ат.: \n\n\n\nРезультат: Физ. атм., атм.: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / 1.0332274528}")
    elif converter.get() == "техническую атм в МПа":
        conv_lable.config(text=f"Тех. атмосфера, ат.: \n\n\n\nРезультат: Давление, МПа: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * 0.0980665}")
    elif converter.get() == "МПа в техническую атм":
        conv_lable.config(text=f"Давление, МПа: \n\n\n\nРезультат: Тех. атмосфера, ат.: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / 0.0980665}")
    elif converter.get() == "МПа в кгс/см2":
        conv_lable.config(text=f"Давление, МПа: \n\n\n\nРезультат: Давление, кгс/см2: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * 10.1971621297793}")
    elif converter.get() == "кгс/см2 в МПа":
        conv_lable.config(text=f"Давление, кгс/см2: \n\n\n\nРезультат: Давление, МПа: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / 10.1971621297793}")
    elif converter.get() == "ккал в Дж":
        conv_lable.config(text=f"Энергия(Работа), ккал.: \n\n\n\nРезультат: Энергия(Работа), Дж: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) * 4186.8}")
    elif converter.get() == "Дж в ккал":
        conv_lable.config(text=f"Энергия(Работа), Дж.: \n\n\n\nРезультат: Энергия, ккал: "
                               f"\t{float(conv_etr1.get().replace(",", ".")) / 4186.8}")


window = tkinter.Tk()

WIDTH = (window.winfo_screenwidth() // 2) - 250
HEIGHT = (window.winfo_screenheight() // 2) - 250

window.geometry(f"400x220+{WIDTH}+{HEIGHT}")
window.iconbitmap("convert.ico")
window.title("Конвертер")
window.resizable(False, False)

converter = ttk.Combobox(window, values=["Выберите вид конвертации", "массовый расход", "объемный расход",
                                         "л/сек в м3/ч", "м3/ч в л/сек", "л/мин в м3/ч", "м3/ч в л/мин", "кг/ч в м3/ч",
                                         "м3/ч в кг/ч", "кинематич. в динамич. вязкость",
                                         "динамич. в кинематич. вязкость", "атмосферы в метры",
                                         "метры в атмосферы", "атмосферы в кгс", "кгс в атмосферы",
                                         "атмосферы в МПа", "МПа в атмосферы", "физ. атм в техническую атм",
                                         "техническую атм в физ. атм", "техническую атм в МПа",
                                         "МПа в техническую атм", "МПа в кгс/см2", "кгс/см2 в МПа", "ккал в Дж",
                                         "Дж в ккал"], justify=tkinter.CENTER, font=("Arial", 10), state="readonly")
converter.current(0)
converter.place(x=165, y=20, width=220, height=20)

window.bind("<<ComboboxSelected>>", converters)

conv_lable = tkinter.Label(window, justify=tkinter.LEFT, font=("Arial", 10, "bold"))
conv_lable.place(x=10, y=60)

conv_etr1 = tkinter.Entry(window, font=("Arial", 10))
conv_etr1.place(x=165, y=60, width=220, height=20)

conv_etr2 = tkinter.Entry(window, font=("Arial", 10))
conv_etr2.place(x=165, y=93, width=220, height=20)

btn = tkinter.Button(window, text="Расчитать", font=("Arial", 12), command=resultat)
btn.place(x=140, y=170, width=120, height=30)

window.mainloop()
