from .page import * 

time.sleep(1)
def case_1_1(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 1_1 tvweb_new-1_1: Покупка фильма картой, регистрация по e-mail, проверка начисления 30р, удаление пользователя \n')
    
    email = self.page.rand_mail('3')[0]
    rand = self.page.rand_mail('3')[1]
    name = rand + '3 WebTvzavr'
    passw = '333333'

    email2 = self.page.rand_mail('2')[0]
    rand2 = self.page.rand_mail('2')[1]
    name2 = rand2 + '11 WebTvzavr'

    name_card = 'ALEKSEI BYKOV'
    
    film = 'Лунный камень'
    # emailgo = 'bykov.a@tvzavr.ru'
    # passok = 'tmW9HZvaksgc'

    self.page.click_f('Клик_Вход', 1)
    time.sleep(2)
    self.prof.click_f('Клик_Регистрация', 2)
    time.sleep(2)
    
    #self.page.send_f('Ввод_логина', email, 3)
    self.driver.find_element_by_xpath('.//input[@class="email-registration__address textbox"]').send_keys(email)
    time.sleep(2)
    
    #self.page.send_f('Ввод_пароля', passw, 4)
    self.driver.find_element_by_xpath('.//input[@class="email-registration__password textbox"]').send_keys(passw)
    time.sleep(2)
    self.prof.click_f('Клик_Зарегистрироваться', 5)
    time.sleep(3)

    self.page.waitForElementVisible('.//header[@class="page__header header"]', 30)
    self.prof.click_f('Клик_значок_нового_пользователя', 6)
    time.sleep(3)

    remember_name = self.driver.find_element_by_xpath("//div[@class='profile-menu__name __username']") # запоминание имени пользователя
    remember_name = remember_name.get_attribute('innerHTML')
    print(remember_name)
    text = remember_name
    time.sleep(2)

    self.page.waitForElementVisible('.//span[@class="__userbalance currency- currency currency-RUB"]', 30)  # Проверка начисления 30 р.
    resic = str(self.result.find_link("span", "__userbalance currency- currency currency-RUB"))
    assert ('30') in resic
    self.page.loger_info('Начисление 30 р. подтверждено')
    time.sleep(3)

    self.prof.click_f('Клик_значок_нового_пользователя', 7)
    time.sleep(2)
    
    self.page.send_f('Ввод_2_в_строку_поиска', film, 7)
    time.sleep(3)
    
    self.prof.click_f('Клик_поиска_Лупа', 7)
    time.sleep(2)
    
    self.page.waitForElementVisible('.//a[@href="/film/lunnyi-kamen/"]', 30)

    self.driver.find_element_by_xpath('.//a[@href="/film/lunnyi-kamen/"]').click()
    self.page.loger('Шаг 8. Клик на фильм "Лунный камень"')
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="clip__name heading-1"]', 30)  # Проверка перехода
    resic = str(self.result.find_link("h1", "clip__name heading-1"))
    assert ('Лунный камень') in resic # проверочное словосочетание надписи
    time.sleep(2)

    self.page.loger_info('Переход на карточку фильма "Лунный камень" подтвержден')
    time.sleep(2)
    
    self.driver.find_element_by_xpath('.//button[@id="clip-player-pay"]').click()
    self.page.loger('Шаг 10. Клик кнопки смотреть от 10 руб')
    time.sleep(4)

    self.driver.find_element_by_xpath('.//button[@class="tariffs__buy js-payment-info"]').click()
    self.page.loger('Шаг 11. Клик кнопки напрокат SD-10р')    
    time.sleep(3)

    self.page.input_card('5555555555554444', '8', '2020', name_card, '526')
    time.sleep(3)

    self.page.waitForElementVisible('.//div[@class="tvz-button tvz-bpb2"]', 30)
    
    self.card.click_f('Клик_Play', 13)
    time.sleep(6)  # Время на воспроизведение

    current_time1 = self.driver.find_element_by_xpath('.//span[@class="tvz-time_label tvz-timerow-current_time"]') # запоминание имени пользователя
    current_time1 = current_time1.get_attribute('innerHTML')
    self.page.loger(current_time1)
    time.sleep(5)
    current_time2 = self.driver.find_element_by_xpath('.//span[@class="tvz-time_label tvz-timerow-current_time"]') # запоминание имени пользователя
    current_time2 = current_time2.get_attribute('innerHTML')
    self.page.loger(current_time2)
    if current_time1 != current_time2:
        self.page.loger('Фильм воспроизводится')
        time.sleep(3)
    else:
        assert(), "Фильм не воспроизводится"
    
    # pyautogui.moveTo(1300, 460, duration = 1)   # двигаем, чтобы показались кнопки плеера
    # pyautogui.moveTo(1000, 600, duration = 1)
    #self.page.waitForElementVisible('.//span[@class="tvz-time_label tvz-timerow-current_time"]', 10) # наличие элемента воспроизведения времени
        
    self.prof.click_f('Клик_значок_нового_пользователя', 14)
    time.sleep(2)

    self.prof.click_f('Клик_мои_фильмы', 15)
    time.sleep(5)

    self.prof.click_f('Клик_крестик_всплывшего_окна_тройка', 16)
    time.sleep(2)
    
    self.page.waitForElementVisible('.//div[@class="card__title"]', 30)  # Проверка видимости элемента
    resic = str(self.result.find_link("div", "card__title"))
    assert ('Лунный камень') in resic # проверочное словосочетание надписи
    self.page.loger_info('Наличие фильма Лунный камень в купленных фильмах подтверждено')
    time.sleep(2)

    self.page.delete_uzer(remember_name) # Удаление пользователя
    self.page.loger('Пользователь ' + remember_name + ' удален')
    time.sleep(2)

    self.driver.close() # Закрыть вкладку
    self.driver.switch_to.window(self.driver.window_handles[-1]) # Переключиться на предыдущую вкладку
    time.sleep(3)

    self.prof.click_f('Клик_значок_нового_пользователя', 18)
    time.sleep(1)

    self.prof.click_f('Клик_Выйти', 19)
    time.sleep(3)

    self.driver.quit()