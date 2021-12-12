from enum import Enum,unique,auto


@unique
class DataLakeColumns(Enum):

    masai_trans_id = auto()
    id = auto()
    masai_VERSION_id = auto()


if __name__ == "__main__":

    print("Hello")

