import re


class NameTooShortError(Exception):
    pass


class MustContainAsSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGTH = 4

VALID_DOMAINS = ['.com', 'bg.', '.org', '.net']

pattern_name = r'\w+'
pattern_domain = r'\.[a-z]+'

email = input()

while email != 'End':

    if email.count('@') > 1:
        raise MoreThanOneAtSymbolError('Email should contain only onw @ symbol')
    if len(email.split('@')[0]) < MIN_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters')
    if re.findall(pattern_name, email)[0] != email.split('@')[0] != email.split('@')[0]:
        raise InvalidNameError('Name can contain only letters, digits and underscores!')
    if re.findall(pattern_domain, email)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    email = input()
    print('Email is valid')
