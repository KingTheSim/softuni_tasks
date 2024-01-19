class Storage:
    def __init__(self) -> None:
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        for c in self.categories:
            if c.id == category_id:
                c.edit(new_name)
                break

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        for t in self.topics:
            if t.id == topic_id:
                t.edit(new_topic, new_storage_folder)
                break

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        for d in self.documents:
            if d.id == document_id:
                d.edit(new_file_name)
                break

    def delete_category(self, category_id: int) -> None:
        for c in self.categories:
            if c.id == category_id:
                self.categories.remove(c)
                break

    def delete_topic(self, topic_id: int) -> None:
        for t in self.topics:
            if t.id == topic_id:
                self.topics.remove(t)
                break

    def delete_document(self, document_id: int) -> None:
        for d in self.documents:
            if d.id == document_id:
                self.documents.remove(d)
                break

    def get_document(self, document_id: int) -> str:
        for d in self.documents:
            if d.id == document_id:
                return f"{d}"

    def __repr__(self) -> str:
        result = []
        for d in self.documents:
            result.append(f"{d}")

        result = "\n".join(result)
        return result
