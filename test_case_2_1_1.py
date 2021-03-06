from .page import *

time.sleep(2)
def case_2_1_1(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 2_1_1 tvweb_new-2_1_1: Проверка фильтров поиска на странице Каталог(Жанры)')
    
    time.sleep(1)
        
    self.page.click_f('Клик_Каталог', 1)
    time.sleep(3)

    self.page.click_f('Клик_Жанры', 2)
    time.sleep(1)

    b = random.randint(0, 44)

    self.driver.find_elements_by_xpath('.//li[@data-filter-type="genres"]')[b].click()
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 4)
    time.sleep(1)

    genre1 = self.driver.find_element_by_xpath('.//button[@class="filter__item filter__item_genres"]')
    genre1text = genre1.text
    self.page.loger('Выбранный жанр: ' + genre1text)
    time.sleep(1)

    m = self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')   # считает количество фильмов
    print(len(m))  

    while (len(m)) < 1:
        self.driver.find_element_by_xpath('.//button[@class="filter__reset js-filter-reset"]').click() # Клик сбросить
        time.sleep(3)

        self.page.click_f('Клик_Каталог', 1)
        time.sleep(3)

        self.page.click_f('Клик_Жанры', 2)
        time.sleep(1)

        b = random.randint(0, 44)

        self.driver.find_elements_by_xpath('.//li[@data-filter-type="genres"]')[b].click()
        time.sleep(2)
        self.page.click_f('Клик_применить_фильтр', 4)
        time.sleep(1)

        genre1 = self.driver.find_element_by_xpath('.//button[@class="filter__item filter__item_genres"]')
        genre1text = genre1.text
        self.page.loger('Выбранный жанр: ' + genre1text)
        time.sleep(1)

        m = self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')   # считает количество фильмов
        print(len(m))  

    p = random.randint(0, (len(m) - 1))
    self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[p].click()
    time.sleep(3)

    res_txt = str(self.result.find_link("h1", "clip__name heading-1").text)  # название фильма
    self.page.loger('Название фильма: ' + res_txt.strip())
    time.sleep(1)  

    genre2 = self.driver.find_element_by_xpath('.//div[@class="clip__genres"]')
    genre2text = genre2.text
    self.page.loger('Жанры в карточке фильма: ' + genre2text)
    time.sleep(2)

    assert (genre1text) in genre2text  # проверочное словосочетание надписи
    self.page.loger('Наличие жанра ' + genre1text + ' в карточке фильма подтверждено')
    time.sleep(1)

    self.driver.quit()