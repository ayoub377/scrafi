from ScraFi.modules.cih import CIHModule
from woob.core import Woob


def main():
    # Initialize the Woob instance
    woob_instance = Woob()

    # Create an instance of the CIH module with the configuration
    cih_module = CIHModule(woob_instance, 'cih', config={
        'login': '3329473001',
        'password': '392781',
    })

    # Create a browser instance after configuring the module
    browser = cih_module.create_default_browser()

    try:
        # Login to the website
        browser.do_login()
        # Get the accounts
        accounts = browser.get_accounts()
        # Print the accounts
        for account in accounts:
            print(account)
    except Exception as e:
        print(f"Error during login: {e}")
        raise  # Raise the exception to see the full traceback


if __name__ == "__main__":
    main()
