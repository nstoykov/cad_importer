fields_pozemlimoti = {
    "IDENT": "Идентификатор на имот",
    "VIDT": "Вид територия",
    "VIDTOLD": "Вид територия (стара номенклатура)",
    "VIDS": "Вид собственост",
    "NTP": "Начин на трайно ползване",
    "NTPOLD": "Начин на трайно ползване (стара номенклатура)",
    "MESTNOST": "MESTNOSTI	Код на местност",
    "PARTIDA": "Номер на партида от ИР",
    "ADDRCODE": "ADDRESS	Адрес на имота",
    "NOMER1": "Стар планоснимачен номер",
    "KVARTAL": "Номер на квартал от регулационен план",
    "PARCEL": "Номер на парцел  от регулационен план с римски цифри",
    "GODCAD": "Година на стария кадастрален план",
    "GODREG": "Година на стария регулационен план",
    "CODZAP": "Код на последната заповед за одобряване",
    "ZACON": "Код на закон, по който са установени границите",
    "KAT": "Преобладаваща категория на земята",
    "NVAST": "Начин на възстановяване - от класификатора за начините на възстановяване",
    "VAVOD": "флаг за въвод във владение",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация",
}

fields_prava = {
    "IDENT": "Идентификатор на поземлен имот, сграда или самостоятелен обект в сграда",
    "VIDS": "Вид собственост",
    "PERSON": "PERSONS	ЕГН/Булстат на носителя на правото",
    "DOCCOD": "DOCS	Код на документ",
    "DOCID1": "Идеална част: стойност на числителя",
    "DOCID2": "Идеална част: знаменател, число на процента или площта в кв.м. площ (в зависимост от DOCID1)",
    "PLDOC": "Площ по документ",
    "PTYPE": "Начин на придобиване",
    "PRAVOVID": "Код на вида право",
    "SROK": "Крайна дата на правото когато правото е срочно",
    "DOCIDENT": "Номер на обекта по документ -свободен текст, например квартал и парцел, пл.сним. номер и т.н.",
    "DOP": "Флаг за допълнителнителен документ  (собственост); Т – допълнително, F – основен документ",
    "BEG_DATE": "Дата на регистрация на правото",
    "END_DATE": "Дата на прекратяване на правото",
    "END_TIME": "Време(момент) на прекратяване на правото"
}
fields_persons = {
    "PERSON": "ЕГН/БУЛСТАТ на соб¬стве¬ник (не се въвежда буква в кода по БУЛСТАТ)",
    "SUBTYPE": "Вид на субекта, код от номенклатура",
    "NAME": "Име на собственик",
    "NSTATE": "Адрес на собственика - буквен код на страна",
    "АDDRCODE": "Адрес на собственика - код на адрес",
    "ADDR": "Пълен адрес на собственика  - коментар",
    "ADDRET": "Адрес на собственика – етаж",
    "ADDRAP": "Адрес на собственика – апартамент",
    "FLAG": "Флаг за починал собственик",
    "SPERSON": "ЕГН на свързано лице (съпруг/съпруга или физическо лице за ЕТ)",
    "FIRMREG": "Данни за съдебна регистрация на фирма",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация"

}
fields_sgradi = {
    "IDENT": "Идентификатор на сграда",
    "VIDS": "Вид собственост",
    "CONST": "Конструкция на сградата",
    "VFUNC": "Функционално предназначение на сградата",
    "VFUNCOLD": "Функционално предназначение на сградата – (стара номенклатура)",
    "GOD": "Година на построяване на сградата",
    "PARTIDA": "Номер на партида от ИР",
    "NOMER1": "Стар планоснимачен номер",
    "ET": "Брой етажи на сградата",
    "ET1": "Брой допълнителни етажи",
    "BRPOM": "Брой самостоятелни обекти",
    "ADDRCODE": "Адрес – код",
    "LEGAL": "Флаг за законност",
    "LEGALDOC": "Описание на документите за законност",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация"
}

fields_aparts = {
    "IDENT": "Идентификатор на самостоятелен обект",
    "REM": "Описание на обекта",
    "PREDN": "Предназначение на самостоятелен обект",
    "VIDS": "Вид собственост",
    "PARTIDA": "Номер на партида от ИР",
    "ADDRCODE": "ADDRESS	Адрес – код",
    "ADDRET": "Адрес – етаж",
    "ADDRAP": "Адрес – апартамент",
    "PLDOC": "Площ по документ",
    "BRET": "Брой етажи на обекта",
    "DOPS": "Вид и площ на прилежащите помещения и общите части , които са неразделна част от обекта (свободен текст)",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация"

}

fields_ulici = {
    "NULIC": "Код на улица, квартал, ж.к.",
    "TYPE": "Тип улица, квартал, ж.к.",
    "NAME": "Име на улица, квартал, ж.к.",
    "EKATTE": "ЕКАТТЕ на населено място където е улицата",
    "GRAO": "Код по ГРАО",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация"

}
fields_address = {
    "ADDRCODE": "Код на адрес",
    "PCOD": "Пощенски код",
    "NULIC": "Улица, квартал, ж.к.",
    "ADDRNUM": "Номер",
    "ADDRSUB": "Подномер",
    "ADDRBLK": "Блок",
    "ADDRWH": "Вход",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация"

}

fields_mestnosti = {
    "MESTNOST": "Код на местност",
    "NAME": "Име на местност",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация"

}
fields_zapovedi = {
    "CODZAP": "Код на заповед",
    "NOMZAP": "Номер на влязлата в сила заповед",
    "DATAZAP": "Дата на заповедта",
    "IZDATEL": "Издател на заповедта",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация"
}
fields_izdateli = {
    "DOCIZD": "Код на издател",
    "IME": "Име на издател",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация"

}
fields_history = {
    "IDENT1": "Идентификатор на нов имот",
    "IDENT2": "Идентификатор на стар имот",
    "TYPE": "Начин на получаване",
    "REGDATE": "Дата на регистрация"

}

fields_servituti = {
    "IDENT1": "Идентификатор на господстващ имот",
    "IDENT2": "Идентификатор на служещ имот",
    "TYPE": "Тип на сервитута - от класификатора за сервитутите",
    "AREA": "Площ на сервитута",
    "WIDTH": "Широчина на сервитута",
    "DOCCOD": "Код на документ",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация"
}

fields_orgprimo = {
    "IDENT": "Идентификатор на имот",
    "TYPE": "Тип на ограничението - от класификатора за ограниченията за ползване",
    "DOCCOD": "Код на документ за ограничението",
    "DOCCOD1": "Код на документ за отмяна ограничението",
    "STATUS": "Състояние на ограничението 0 – в сила, 1 - проектно, 2 – отменено)",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на регистрация на отмяната"

}
fields_docs = {
    "DOCCOD": "Код на документа",
    "DOCVID": "Вид на документа",
    "DOCNOM": "Номер на документа",
    "DOCDATE": "Дата на документа",
    "DOCTOM": "Том на документа в службата по вписванията",
    "DOCREG": "Регистър на документа в службата по вписванията",
    "DOCDEL": "Дело на документа в службата по вписванията",
    "DOCIZD": "Издател",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на регистрация на отмяната"
}
fields_gorimoti = {
    "IDENT": "Идентификатор на имот",
    "DL": "Държавно лесничейство",
    "OTDEL": "Номер на отдел от лесоустройството",
    "PODOTDEL": "Номер на подотдел от лесоустройството",
    "AREA": "Площ на частта на подотдела в имота кв.м.",
    "BEG_DATE": "Дата на регистрация",
    "END_DATE": "Дата на отрегистрация"

}
vid_sobstvenost = {
    0: "Няма данни",
    1: "Държавна публична",
    2: "Държавна частна",
    3: "Общинска публична",
    4: "Общинска частна",
    5: "Частна",
    6: "Частна кооперативна",
    7: "Частна обществени организации",
    8: "Частна чужди физически и юридически лица",
    9: "Частна международни организации",
    10: "Частна религиозни организации",
    11: "Съсобственост",
    12: "Изключителна държавна собственост",
    97: "стопанисвана от държавата по чл.14а от ЗВСГЗГФ",
    98: "държавна собственост по чл.6 от ЗВСГЗГФ",
    99: "Стопанисвано от общината"
}

sg_pred = {
    100: "Жилищна сграда - еднофамилна",
    110: "Жилищна сграда - многофамилна",
    120: "Жилищна сграда със смесено предназначение",
    130: "Вилна сграда - еднофамилна",
    140: "Вилна сграда - многофамилна",
    150: "Общежитие",
    160: "Хотел",
    170: "Апартаментен хотел",
    180: "Постройка на допълващото застрояване",
    190: "Друг вид сграда за обитаване",
    200: "Сграда за тьрговия",
    210: "Сграда за обществено хранене",
    220: "Сграда за битови услуги",
    230: "Сграда за детско заведение",
    240: "Учебна сграда",
    250: "Здравно заведение",
    260: "Заведение за социални грижи",
    270: "Сграда за научна и проектантска дейност",
    280: "Сграда за културни и обществени дейности",
    290: "Спортна сграда, база",
    300: "Административна, делова сграда",
    310: "Курортна, туристическа сграда",
    320: "Сграда на транспорта",
    330: "Сграда на съобщенията",
    340: "Култова сграда",
    350: "Сграда - паметник на културата",
    360: "Друг вид обществена сграда",
    400: "Промишлена сграда",
    410: "Сграда за енергопроизводство",
    420: "Селскостопанска сграда",
    430: "Горскостопанска сграда",
    440: "Сграда за водоснабдяване и/или канализация",
    450: "Сграда със специално предназначение",
    460: "Складова база, склад",
    470: "Хангар, депо, гараж",
    480: "Друг вид производствена, складова, инфраструктурна сграда",
    490: "Сграда със смесено предназначение"
}