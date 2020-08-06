import requests

STATES = "states.txt"


def downlaod_file(url):
    r = requests.get(url, allow_redirects=True)
    print(r.content)
    return r.content

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
    file_name = prefix + "_" + state_fips + '_' + state_code.lower() + '_' + postfix
    return file_name


def retrieve_and_persist_fips_county(file_name):
    pass


def process_states(file_name):
    lines = load_states_master_file_as_lines(file_name)
    for line in lines: 
        row_list = line.strip().split('|')
        state_fips = row_list[0]
        state_code = row_list[1]
        print(construct_countystate_fips_file_name(state_fips, state_code))


if __name__ == "__main__":
    retrieve_and_persist_fips_states(STATES)
    process_states(STATES)