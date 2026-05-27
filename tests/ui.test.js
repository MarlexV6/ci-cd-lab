const { Builder, By } = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');

let driver;

beforeAll(async () => {
    let options = new firefox.Options().addArguments('-headless');

    driver = await new Builder()
        .forBrowser('firefox')
        .setFirefoxOptions(options)
        .setFirefoxService(
            new firefox.ServiceBuilder('/usr/local/bin/geckodriver')
        )
        .build();

    await driver.get('file://' + __dirname + '/../index.html');
});

afterAll(async () => {
    if (driver) await driver.quit();
});

test('Проверка заголовка', async () => {

    const title = await driver
        .findElement(By.id('title'))
        .getText();

    expect(title).toBe('Форма входа');
});

test('Проверка кнопки', async () => {

    const button = await driver
        .findElement(By.id('btn'));

    const text = await button.getText();

    expect(text).toBe('Отправить');
});