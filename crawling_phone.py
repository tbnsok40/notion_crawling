from selenium import webdriver

def get_browser(url):
    # chromedriver 설치 후 루트 디렉토리에 배
    browser = webdriver.Chrome('./chromedriver')
    browser.get(url)
    browser.implicitly_wait(10)

    box = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div[19]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]').text # 와 텍스트 안붙여서 헤맨거야?

    return get_name_phone(browser, box)

def get_name_phone(browser, box):
    result = []
    try:
        for i in range(3, 3 + int(box)):
            # 왜 23부터 못읽는지 -> time.sleep()이 충분히 길지 않아서
            name = browser.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div[19]/div[2]/div/div/div[2]/div[1]/div[' + str(
                    i) + ']/a/div/div[2]/div').text  # 왜 됐다 안됐다 하노,,,
            phone = browser.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div[19]/div[2]/div/div/div[2]/div[1]/div[' + str(
                    i) + ']/a/div/div[3]/div/a/div/span').text
            result.append((name, phone))
        return result

    except IndexError:
        return result

url = "크롤링 할 노션 페이지 url"
print(get_browser(url))