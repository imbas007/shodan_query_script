import requests
import argparse
from colorama import Fore, Style
from shodan import Shodan
import urllib3

urllib3.disable_warnings()

SHODAN_API_KEY = 'YOUR_SHODAN_API_KEY'  # Replace with your Shodan API Key

def perform_shodan_query(api_key, query):
    try:
        api = Shodan(api_key)
        results = api.search(query)
        return results
    except Exception as e:
        print(Fore.RED + 'Error during Shodan query: {}'.format(e))
        return None

def save_results_to_file(results, filename='shodan_results.txt'):
    try:
        with open(filename, 'w') as file:
            for result in results['matches']:
                ip = str(result['ip_str']).replace("\n", "")
                port = str(result['port'])
                file.write(ip + ':' + port + '\n')
        print(Fore.GREEN + 'Results saved to {}'.format(filename))
    except Exception as e:
        print(Fore.RED + 'Error while saving results to file: {}'.format(e))

def bold_text(text):
    return Style.BRIGHT + text + Style.RESET_ALL

def main():
    parser = argparse.ArgumentParser(
        prog='Shodan Query and Save Results',
        description='Perform a Shodan query, display results, and save IP addresses with ports to a text file.',
        epilog='Please make sure that you are using a valid Shodan API Key')

    parser.add_argument('-q', '--query', required=True, help="Shodan query (e.g., 'http.favicon.hash:-1439222863 country:US')")
    parser.add_argument('-o', '--output', default='shodan_results.txt', help="Output file name (default: shodan_results.txt)")

    args = parser.parse_args()

    print("Performing Shodan query...")
    shodan_results = perform_shodan_query(SHODAN_API_KEY, args.query)

    if shodan_results:
        print("====================================================")
        print(Fore.BLUE + bold_text('Results for Shodan query: {}'.format(args.query)))
        print(Style.RESET_ALL)
        print("====================================================\n")

        for result in shodan_results['matches']:
            ip = str(result['ip_str']).replace("\n", "")
            port = str(result['port'])
            print(Fore.GREEN + ip + ':' + port)
            print(Style.RESET_ALL)

        print("====================================================\n")

        save_results_to_file(shodan_results, args.output)

if __name__ == "__main__":
    main()
