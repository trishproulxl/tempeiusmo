def start_driver(account):
    """
    Start the driver and return a handle to it.

    Args:
        account (str): The account ID to use.

    Returns:
        webdriver.Remote: A handle to the driver.
    """

    # The URL to use depends on whether the account is on the legacy or
    # modern infrastructure.
    if account.startswith("A"):
        url = "https://www.example.com    else:
        url = "https://www.example.com    # Download the driver.
    response = requests.get(url, stream=True)
    with open("/tmp/chromedriver.zip", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    # Unzip the driver.
    with zipfile.ZipFile("/tmp/chromedriver.zip", "r") as zip_ref:
        zip_ref.extractall("/tmp")

    # Start the driver.
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--disable-infobars")
    options.add_argument("--log-level=3")
    options.add_argument("--output=/tmp/chromedriver.log")

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options,
    )

    return driver  
