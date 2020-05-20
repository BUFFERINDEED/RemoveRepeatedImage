from PIL import Image

import os
import magic
import argparse
import imagehash

hashType_dict = {"ahash": imagehash.average_hash,
                 "phash": imagehash.phash,
                 "dhash": imagehash.dhash,
                 "whash": imagehash.whash}


def main():
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument(
        "--target_path",
        nargs=1,
        type=str,
        required=True,
        help="Target directory where the pictures store.",
    )
    parser.add_argument(
        "--hashType",
        nargs=1,
        type=str,
        required=True,
        help="hash method used to compare image"
    )

    args = parser.parse_args()
    if args.hashType[0] not in hashType_dict:
        print(f"Invalid hash type {args.hashType},"
              f"Please make sure you are use one of the follows:\n"
              f"{list(hashType_dict.keys())}")
        return

    hash_dict = {}
    target_path = args.target_path[0]
    print(target_path)
    file_list = [os.path.join(target_path, filename)
                 for filename in os.listdir(target_path)
                 if "image" in magic.from_file(os.path.join(target_path, filename))]

    for item in file_list:
        img = Image.open(item)
        hashvalue = str(hashType_dict[args.hashType[0]](img))
        if hashvalue in hash_dict:
            repeated_img = Image.open(hash_dict[hashvalue])
            if repeated_img.size > img.size:
                os.remove(item)
                print(f"removed file {item}")
                continue
            else:
                os.remove(hash_dict[hashvalue])
                print(f"removed file {hash_dict[hashvalue]}")
                hash_dict[hashvalue] = item
        else:
            hash_dict.update({hashvalue: item})


def get_hash_value(hashFunction, path):
    return str(hashFunction(Image.open(path)))


def SearchSameImage(path, searchedFilename, hashType="phash"):
    if hashType not in hashType_dict:
        print(f"Invalid hash type {hashType},"
              f"Please make sure you are use one of the follows:\n"
              f"{list(hashType_dict.keys())}")
        return

    hashvalue = get_hash_value(imagehash.phash, os.path.join(path, searchedFilename))

    file_list = [os.path.join(path, filename)
                 for filename in os.listdir(path)
                 if "image" in magic.from_file(os.path.join(path, filename))]

    for item in file_list:
        if hashvalue == get_hash_value(hashType_dict[hashType], item):
            print(item)


if __name__ == "__main__":
#    SearchSameImage("./test1",
#                    "photo_263@19-03-2018_16-58-04.jpg",
#                    "phash")

     main()
