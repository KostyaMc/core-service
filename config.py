from pydantic import BaseModel, field_validator


class TaskModel(BaseModel):
    id: int | None = None
    task: str

    @field_validator("task")
    @classmethod  # это метод класса, который работает по правилам чертежа, а не по конкретному экземпляру
    # @classmethod нужен потому, что Pydantic валидирует данные до создания экземпляра, и на этом этапе доступен только класс, а не объект.
    def check_string_len(cls, v):
        if not isinstance(v, str):
            raise ValueError("Задача должна быть строкой")
        if v.strip() == "":
            raise ValueError("Необходимо ввести задачу")
        return v


class TaskUpdate(BaseModel):
    task: str | None = None