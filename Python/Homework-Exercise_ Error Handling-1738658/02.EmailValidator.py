
class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidCharacterError(Exception):
    pass


MIN_LENGTH = 4
VALID_DOMAINS = (".com", ".bg", ".org", ".net")
INVALID_SYMBOLS = "!?#$"

while True:
    email = input()
    if email == "End":
        break

    index_name = email.find("@")
    index_domain = email.rfind('.')
    domain_name = email[index_domain:]
    if index_name == -1:
        raise MustContainAtSymbolError("Email must contain @")
    elif email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email must contain only one @")
    elif index_name < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    elif not (domain_name in VALID_DOMAINS) or (index_domain - index_name == 1):  # "abc@.com" is not valid mail too
        raise InvalidDomainError("Domain must be one of the following: *.com, *.bg, *.org, *.net")
    elif set(email).intersection(INVALID_SYMBOLS):
        raise InvalidCharacterError("Contains invalid character/s")
    else:
        print("Email is valid")


