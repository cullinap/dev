import operator


PEOPLE = [
    {'first':'Reuven','last':'Lerner','email':'reuven@lerner.co.il'},
    {'first':'Donald','last':'Trump','email':'president@whitehouse.gov'},
    {'first':'Vladimir','last':'Putin','email':'president@kremvax.ru'}
]


def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, 
                  key=lambda x: x['last'])
           



print(alphabetize_names(PEOPLE))
