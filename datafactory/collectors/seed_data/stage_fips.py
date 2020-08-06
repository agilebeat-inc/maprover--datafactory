import requests
import os

STATES_FN = "states.csv"
STATES_COUNTIES_FN = 'st00_all_cou.csv'


def downlaod_file(url):
    print("Dwonloading: {}".format(url))
    try:
        r = requests.get(url, allow_redirects=True)
        if r.status_code == 200:
            return r.content
        print("Request for the url: {} has returned status: {}".format(url, r.status_code))
        return b''
    except requests.exceptions.RequestException as e:
        print(e)
    return b''


def persist_in_file(file_name, content):
    with open(file_name, 'wb') as fa:
        fa.write(content)


def append_to_file(file_name, content):
    with open(file_name, 'ab') as fa:
        fa.write(content)


def retrieve_and_persist_fips_states(file_name):
    state_url = 'http://www2.census.gov/geo/docs/reference/state.txt?#'
    content = downlaod_file(state_url)
    persist_in_file(file_name, content)


def load_states_master_file_as_lines(file_name):
    with open(file_name) as fr:
        lines = fr.readlines()
    return lines


def construct_countystate_fips_file_name(state_fips, state_code):
    prefix = 'st'
    postfix = 'cou.txt'
    file_name = prefix + state_fips + '_' + state_code.lower() + '_' + postfix
    return file_name


def retrieve_and_persist_fips_countyper_state(state_fips, state_code, file_name):
    remote_fname = construct_countystate_fips_file_name(state_fips, state_code)
    url = 'https://www2.census.gov/geo/docs/reference/codes/files/' + remote_fname
    content = downlaod_file(url)
    append_to_file(file_name, content)
    if len(content) > 0 and content[len(content)-1] != '\n':
        append_to_file(file_name, b'\n')


def process_states(file_name):
    lines = load_states_master_file_as_lines(file_name)
    state_cnt = 0
    for line in lines:
        state_cnt+=1
        if state_cnt == 1:
            continue 
        row_list = line.strip().split('|')
        state_fips = row_list[0]
        state_code = row_list[1]
        retrieve_and_persist_fips_countyper_state(state_fips, state_code, STATES_COUNTIES_FN)

def clean_files():
    try:
        os.remove(STATES_COUNTIES_FN)
        os.remove(STATES_FN)
    except Exception:
        print("Swolled file cleanup exception")

if __name__ == "__main__":
    clean_files()
    retrieve_and_persist_fips_states(STATES_FN)
    process_states(STATES_FN)