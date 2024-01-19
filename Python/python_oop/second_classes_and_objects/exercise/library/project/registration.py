from project.user import User
from project.library import Library


class Registration:
    def add_user(self, user: User, library: Library) -> None or str:
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        else:
            library.user_records.append(user)

    def remove_user(self, user: User, library: Library) -> None or str:
        if user in library.user_records:
            library.user_records.remove(user)

        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        for u in library.user_records:
            if u.user_id == user_id:
                if u.username != new_username:
                    old = u.username
                    u.username = new_username

                    if old in library.rented_books:
                        cur_dict = library.rented_books[old]
                        del library.rented_books[old]
                        library.rented_books[new_username] = cur_dict

                    return f"Username successfully changed to: {new_username} for user id: {user_id}"

                else:
                    return f"Please check again the provided username" \
                           f" - it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"
